import sys
import os

# Add the parent directory to the path so we can import the rules package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 