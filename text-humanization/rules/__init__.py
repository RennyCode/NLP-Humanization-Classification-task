"""
Rules package for text humanization.
"""

from rules.rule_capitalization import fix_capitalization, score_capitalization
from rules.rule_emojis import fix_emojis, score_emojis
from rules.rule_punctuation import fix_punctuation_spacing, score_punctuation_spacing
from rules.rule_markdown import fix_remove_markdown, score_remove_markdown
from rules.rule_sentence_length import fix_sentence_length, score_sentence_length
from rules.rule_fillers import fix_fillers, score_fillers
from rules.rule_contractions import fix_contractions, score_contractions
from rules.rule_typos import fix_typos, score_typos
from rules.rule_casual_language import fix_casual_language, score_casual_language
from rules.rule_sentence_structure import fix_sentence_structure, score_sentence_structure
from rules.rule_exclamations import fix_exclamations, score_exclamations
from rules.rule_interjections import fix_interjections, score_interjections
from rules.rule_personal_pronouns import fix_personal_pronouns, score_personal_pronouns
from rules.rule_acronyms import fix_acronyms, score_acronyms
from rules.rule_slang import fix_slang, score_slang
from rules.rule_fragmentation import fix_fragmentation, score_fragmentation
from rules.rule_verbosity import fix_verbosity, score_verbosity
from rules.rule_ai_mentions import fix_ai_mentions, score_ai_mentions
from rules.rule_tone_warmth import fix_tone_warmth, score_tone_warmth
# Import other rules as they are created

# List of all rules with their fix functions, score functions, and parameters
rules = [
    # Rule structure: (rule_name, fix_function, score_function, parameters, weight)
    # Weight determines the likelihood of the rule being applied (0.0 to 1.0)
    ("AI Mention Removal Rule", fix_ai_mentions, score_ai_mentions, {}, 1),
    ("Capitalization Variation Rule", fix_capitalization, score_capitalization, {"variation_level": 0.6}, 0.8),
    ("Emoji Injection Rule", fix_emojis, score_emojis, {"injection_probability": 0.2}, 0.7),
    ("Punctuation Spacing Rule", fix_punctuation_spacing, score_punctuation_spacing, {}, 0.9),
    ("Remove Markdown Formatting Rule", fix_remove_markdown, score_remove_markdown, {}, 1.0),
    ("Sentence Length Variation Rule", fix_sentence_length, score_sentence_length, {"merge_probability": 0.15}, 0.6),
    ("Fillers Injection Rule", fix_fillers, score_fillers, {"filler_probability": 0.1}, 0.5),
    ("Contraction Usage Rule", fix_contractions, score_contractions, {}, 0.9),
    ("Minor Typos Introduction Rule", fix_typos, score_typos, {"typo_probability": 0.05}, 0.3),
    ("Casual Language Substitution Rule", fix_casual_language, score_casual_language, {}, 0.7),
    ("Sentence Structure Variation Rule", fix_sentence_structure, score_sentence_structure, {}, 0.6),
    ("Exclamation Mark Variation Rule", fix_exclamations, score_exclamations, {"variation_factor": 0.15}, 0.5),
    ("Interjection Insertion Rule", fix_interjections, score_interjections, {"interjection_probability": 0.15}, 0.4),
    ("Personal Pronoun Emphasis Rule", fix_personal_pronouns, score_personal_pronouns, {}, 0.8),
    ("Acronym and Abbreviation Rule", fix_acronyms, score_acronyms, {}, 0.7),
    ("Slang Substitution Rule", fix_slang, score_slang, {}, 0.5),
    ("Sentence Fragmentation Rule", fix_fragmentation, score_fragmentation, {"fragmentation_probability": 0.1}, 0.4),
    ("Verbosity Reduction Rule", fix_verbosity, score_verbosity, {}, 0.6),
    ("Tone Warmth Adjustment Rule", fix_tone_warmth, score_tone_warmth, {}, 0.8),
] 