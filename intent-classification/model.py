import os
from enum import Enum
from typing import List
from pydantic import BaseModel, Field
from openai import OpenAI

# Initialize OpenAI client
openai_client = None 

def get_openai_client():
    """ Lazily initializes and returns a single OpenAI client instance. """
    global openai_client
    if openai_client is None:  
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Error: OPENAI_API_KEY environment variable is not set.")
        
        openai_client = OpenAI(api_key=api_key)  
    return openai_client


class Intent(str, Enum):
    # Conversation starters and general
    START_CONVERSATION = "startConversation"
    END_CONVERSATION = "endConversation"
    GREET = "greet"
    THANK = "thank"
    CONFIRM = "confirm"
    DENY = "deny"
    
    # Questions and information seeking
    ASK_GENERAL_QUESTION = "askGeneralQuestion"
    ASK_TECHNICAL_SUPPORT = "askForTechnicalSupport"
    ASK_FOR_INFORMATION = "askForInformation"
    ASK_FOR_CLARIFICATION = "askForClarification"
    ASK_FOR_OPINION = "askForOpinion"
    ASK_ABOUT_FEATURES = "askAboutFeatures"
    ASK_ABOUT_PRICING = "askAboutPricing"
    
    # Actions and requests
    REQUEST_ASSISTANCE = "requestAssistance"
    REQUEST_FEATURE = "requestFeature"
    REQUEST_CALLBACK = "requestCallback"
    REQUEST_HUMAN = "requestHuman"
    REQUEST_DOCUMENT = "requestDocument"
    PROVIDE_FEEDBACK = "provideFeedback"
    REPORT_ISSUE = "reportIssue"
    SUBMIT_COMPLAINT = "submitComplaint"
    
    # Account and user related
    CREATE_ACCOUNT = "createAccount"
    UPDATE_ACCOUNT = "updateAccount"
    DELETE_ACCOUNT = "deleteAccount"
    RESET_PASSWORD = "resetPassword"
    CHECK_STATUS = "checkStatus"
    CHECK_BALANCE = "checkBalance"
    MANAGE_SUBSCRIPTION = "manageSubscription"
    UPGRADE_PLAN = "upgradePlan"
    DOWNGRADE_PLAN = "downgradePlan"
    
    # Commerce related
    PLACE_ORDER = "placeOrder"
    CANCEL_ORDER = "cancelOrder"
    TRACK_ORDER = "trackOrder"
    REQUEST_REFUND = "requestRefund"
    CHECK_INVENTORY = "checkInventory"
    INQUIRE_SHIPPING = "inquireShipping"
    INQUIRE_RETURN_POLICY = "inquireReturnPolicy"
    
    # Scheduling and appointments
    BOOK_APPOINTMENT = "bookAppointment"
    CANCEL_APPOINTMENT = "cancelAppointment"
    RESCHEDULE_APPOINTMENT = "rescheduleAppointment"
    CHECK_AVAILABILITY = "checkAvailability"
    
    # Other common intents
    SHARE_LOCATION = "shareLocation"
    SEARCH_PRODUCT = "searchProduct"
    COMPARE_PRODUCTS = "compareProducts"
    GET_RECOMMENDATIONS = "getRecommendations"
    EXPRESS_DISSATISFACTION = "expressDissatisfaction"
    EXPRESS_SATISFACTION = "expressSatisfaction"
    MAKE_SMALL_TALK = "makeSmallTalk"
    TELL_JOKE = "tellJoke"
    UNRECOGNIZED = "unrecognized"

class IntentClassification(BaseModel):
    """Classification of user intent based on conversation context"""
    explanation: str = Field(..., description="Brief explanation of why this intent was detected")
    intent: Intent = Field(..., description="The intent detected in the message")


def classify_intent(conversation: List[dict]) -> IntentClassification:
    """
    Classify the intent of a conversation using OpenAI.
    
    Args:
        conversation: A list of message dictionaries in OpenAI format [{role: str, content: str}, ...]
    
    Returns:
        IntentClassification object containing the detected intent and explanation
    """
    # Create system prompt instructing the model how to classify intents
    system_prompt = """
    You are an intent classification system. Analyze the conversation provided and determine the user's primary intent.
    Choose the most appropriate intent category from the available options. Consider the full context of the conversation, 
    especially focusing on the user's latest message and their overall goal.
    
    Guidelines for specific intent classifications:
    
    1. Conversation starters and general:
       - Use START_CONVERSATION when users explicitly introduce themselves as new users or clearly indicate they're initiating a new conversation thread (e.g., "Hi there! I'm new to your service and just wanted to introduce myself")
       - Use END_CONVERSATION when users explicitly ask to end or terminate the conversation
       - Use GREET for simple greetings like "hello", "hi", "good morning" without additional context
       - Use THANK when users express gratitude or appreciation (e.g., "thank you for your help")
       - Use CONFIRM when users are affirming, agreeing, or confirming something (e.g., "yes, that's correct", "can you confirm my booking?")
       - Use DENY when users are explicitly rejecting, disagreeing, or denying something (e.g., "I did not make those purchases", "I absolutely did not authorize those charges")
    
    2. Questions and information seeking:
       - Use ASK_GENERAL_QUESTION for broad, open-ended questions that don't fit other specific categories
       - Use ASK_TECHNICAL_SUPPORT when users describe technical problems they need help with or ask for technical assistance
       - Use ASK_FOR_INFORMATION for general knowledge queries that don't fit into more specific categories
       - Use ASK_FOR_CLARIFICATION when users need additional explanation or clarification about something previously discussed
       - Use ASK_FOR_OPINION when users ask for subjective views or opinions about THEIR OWN ideas, projects, or work
       - Use ASK_ABOUT_FEATURES when users inquire about product/service features, capabilities, or functionalities
       - Use ASK_ABOUT_PRICING when the primary focus is on cost information, pricing plans, or fees AS THE MAIN GOAL of the conversation
    
    3. Actions and requests:
       - Use REQUEST_ASSISTANCE for general help requests that don't fit more specific categories
       - Use REQUEST_FEATURE when users suggest or ask for new features to be added to a product/service
       - Use REQUEST_CALLBACK when users ask to be contacted later by phone or other means
       - Use REQUEST_HUMAN when users ask to speak with a real person, representative, or human agent
       - Use REQUEST_DOCUMENT when users ask for documentation, forms, or specific documents
       - Use PROVIDE_FEEDBACK when users want YOU to give feedback on THEIR ideas, products, or services
       - Use REPORT_ISSUE when users are primarily notifying about a bug or problem without asking for help
       - Use SUBMIT_COMPLAINT when users want to formally register a complaint or grievance about a service they received
    
    4. Account and user related:
       - Use CREATE_ACCOUNT when users explicitly want to sign up, register, or create a new account (not just asking for help with the process)
       - Use UPDATE_ACCOUNT when users want to modify their account information or settings
       - Use DELETE_ACCOUNT when users want to remove or deactivate their account
       - Use RESET_PASSWORD when users mention forgotten passwords or need to change/reset their password
       - Use CHECK_STATUS when users want to know the status of something (e.g., order, application, request)
       - Use CHECK_BALANCE when users want to know their account balance, credits, or remaining funds
       - Use MANAGE_SUBSCRIPTION for subscription changes (starting, modifying, or canceling subscriptions)
       - Use UPGRADE_PLAN when users specifically want to move to a higher-tier plan or service
       - Use DOWNGRADE_PLAN when users specifically want to move to a lower-tier plan or service
    
    5. Commerce related:
       - Use PLACE_ORDER when users want to make a purchase or place a new order
       - Use CANCEL_ORDER when users want to cancel a product/merchandise order (not for subscriptions)
       - Use TRACK_ORDER when users want to know the whereabouts or delivery status of their order
       - Use REQUEST_REFUND when users want their money back for a purchase or transaction
       - Use CHECK_INVENTORY when users want to know if a product is in stock or available for purchase, or when they're asking about future stock availability
       - Use INQUIRE_SHIPPING when users ask about shipping methods, costs, or delivery timeframes
       - Use INQUIRE_RETURN_POLICY when users ask about return processes, policies, or how to return items
    
    6. Scheduling and appointments:
       - Use BOOK_APPOINTMENT when users want to schedule a new appointment or meeting
       - Use CANCEL_APPOINTMENT when users want to cancel an existing appointment
       - Use RESCHEDULE_APPOINTMENT when users want to change the date/time of an existing appointment
       - Use CHECK_AVAILABILITY when users want to know available time slots or dates for appointments
    
    7. Other common intents:
       - Use SHARE_LOCATION when users ask about physical location or address information of a business or service
       - Use SEARCH_PRODUCT when users explicitly want to find or look for specific products in a catalog or website
       - Use COMPARE_PRODUCTS when users want to evaluate differences between multiple products, plans, or services
       - Use GET_RECOMMENDATIONS when users ask for suggestions or recommendations
       - Use EXPRESS_DISSATISFACTION when users communicate unhappiness or disappointment
       - Use EXPRESS_SATISFACTION when users communicate happiness or contentment with a product/service
       - Use MAKE_SMALL_TALK when users engage in casual, non-goal-oriented conversation beyond simple greetings (e.g., talking about weather, sports, or asking "how's your day?")
       - Use TELL_JOKE when users specifically ask for humor or jokes
       - Use UNRECOGNIZED only when the user's intent truly doesn't match any other category
    
    Important distinctions and priority rules:
    
    1. When messages contain multiple intents:
       - Prioritize the overall conversation goal over the specific phrasing of the latest message
       - Look at the entire conversation flow to determine the primary intent, not just the most recent message
       - When a conversation starts with comparing products/plans and then asks about pricing, maintain COMPARE_PRODUCTS as the intent
       - When a user asks for help finding a specific product, use SEARCH_PRODUCT, not REQUEST_ASSISTANCE
    
    2. Conversation flow considerations:
       - Consider the entire conversation context, not just the latest message
       - If the conversation started with one intent (e.g., COMPARE_PRODUCTS) and later moved to related topics (e.g., pricing), 
         maintain the original intent if it represents the user's primary goal
       - Look for intent shifts where the user clearly changes their objective
    
    3. Common confusion points to avoid:
       - "Hello there! How are you doing today?" is MAKE_SMALL_TALK, not just GREET
       - "I'm trying to figure out if it's worth upgrading. What's the difference between plans?" is COMPARE_PRODUCTS, even if they later ask about pricing
       - "I've been working on this project and could use a second opinion" is PROVIDE_FEEDBACK, not ASK_FOR_OPINION
       - "I'm trying to find your store location" is SHARE_LOCATION, not ASK_FOR_INFORMATION
       - "I did not authorize those charges" is DENY, not SUBMIT_COMPLAINT
       - "Can you help me create an account?" is CREATE_ACCOUNT, even if they're asking for assistance with the process
       - "That item shows as out of stock. Will you get more?" is CHECK_INVENTORY, not ASK_FOR_INFORMATION
       - "I'm new to your service and wanted to introduce myself" is START_CONVERSATION, not GREET
    
    Provide a brief explanation for your classification that references specific parts of the conversation.
    """
    
    # Prepare messages for the API call
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    # Add the conversation context
    messages.extend(conversation)
    
    # Call the OpenAI API with structured output
    client = get_openai_client()
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=messages,
        response_format=IntentClassification,
        temperature=0,
        seed=42,
    )
    
    # Return the parsed response
    return completion.choices[0].message.parsed

# Example usage
if __name__ == "__main__":
    # Example conversation
    sample_conversation = [
        {"role": "user", "content": "Hi there! Can you help me with my account?"},
        {"role": "assistant", "content": "Of course! I'd be happy to help with your account. What kind of help do you need?"},
        {"role": "user", "content": "I'm having trouble logging in. I think I forgot my password."}
    ]
    
    # Classify the intent
    result = classify_intent(sample_conversation)
    print(f"Explanation: {result.explanation}")
    print(f"Intent: {result.intent}")
