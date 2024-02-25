# Libraries

import os
import pathlib
import textwrap
import json
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown

# -----------------------------------------------------------------------

# Boilerplate

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

def get_user_input():

    # Pass the user input through a variety of built in string methods to improve consistency and reduce risk of violating JSON syntax.
    raw_prompt = input("User: ")
    cleaned_prompt = raw_prompt.lower().strip().replace(':','').replace('"','').replace('{', '').replace('}', '').replace("'",'')
    current_prompt = cleaned_prompt

    # Pass the sanitized user input to the io_handler, unless the user is trying to exit the script.
    if current_prompt == "exit":
        return
    else:
        log_user_input(current_prompt)

# -----------------------------------------------------------------------

def log_user_input(inputs):
        
        # Set inputs to current prompt
        current_prompt = inputs

        # Load the pre-prompt file in preparation for inserting user input
        with open(preprompt_file, "r") as f:
            preprompt = json.load(f)

        # Set value of current prompt in JSON file as the user input && add to context
        preprompt["current_prompt"]["current_prompt"] = current_prompt
        preprompt["context"]["context"].append({"message": f"User: {current_prompt}"})

        with open(preprompt_file, "w") as f:
            json.dump(preprompt, f, indent=4)

        send_model_input()

# -----------------------------------------------------------------------

def send_model_input():

        # Open the pre-prompt file in preparation for feeding to the model
    with open(preprompt_file, "r") as f:
        preprompt = json.load(f)
    
    # Initialize variable for prompt as raw text
    prompt = json.dumps(preprompt, indent=None)

    # Feed prompt to the model && print the response for the user && collect API feedback
    response = model.generate_content(prompt)
    feedback = response.prompt_feedback

    log_model_output(response,feedback,preprompt)

# -----------------------------------------------------------------------

def log_model_output(response,feedback,preprompt):

    # Append model response to context in preprompt file
    preprompt["context"]["context"].append({"message": f"Gemini: {response.text}"})
    with open(preprompt_file, "w") as f:
        json.dump(preprompt, f, indent=4)

    with open(feedback_file, "w") as f:
        f.write(str(feedback))

    print(f"\nGemini: {response.text}\n")

    get_user_input()

# -----------------------------------------------------------------------

get_user_input()