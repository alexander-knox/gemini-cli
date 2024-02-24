# Import necessary libraries
import os
import pathlib
import textwrap
import json
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown

# -----------------------------------------------------------------------

# Get API Key from .env
load_dotenv()
key = os.getenv("KEY")

# Set API key and select model
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')

# Initialize preprompt & feedback file names as variables
preprompt_file = "preprompt.json"
feedback_file = "feedback.txt"

# Markdown function Google told me I needed.
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# -----------------------------------------------------------------------

def user_input():
    # Pass the user input through a variety of built in string methods to improve consistency and reduce risk of violating JSON syntax.
    raw_prompt = input("User: ")
    cleaned_prompt = raw_prompt.lower().strip().replace(':','').replace('"','').replace('{', '').replace('}', '').replace("'",'')
    current_prompt = cleaned_prompt
    return (current_prompt)
    #print(current_prompt)

def manipulate_json():
    pass

def model_output():
    pass

user_input()