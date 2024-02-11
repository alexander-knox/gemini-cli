# Import necessary libraries
import os
import pathlib
import textwrap
import json
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown

# Get API Key from .env
load_dotenv()
key = os.getenv("KEY")


# Uncomment to verify key import
# print(key)
# print(os.environ)


# Markdown function Google told me I needed.
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Set API key and select model
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')

# Initialize preprompt & feedback file names as variables
preprompt_file = "preprompt.json"
feedback_file = "feedback.txt"

# Initiate while loop for continous chat 
# Input 'exit' to break loop
while True:

    # Accept current_prompt
    current_prompt = input("User: ")
        
    # Load the pre-prompt file in preparation for inserting user input
    with open(preprompt_file, "r") as f:
        preprompt = json.load(f)
    # Check preprompt payload
    # print(preprompt)

    # Set value of current prompt in JSON file as the user input && add to context
    preprompt["current_prompt"]["current_prompt"] = current_prompt
    preprompt["context"]["context"].append({"message": f"User: {current_prompt}"})

    with open(preprompt_file, "w") as f:
        json.dump(preprompt, f, indent=4)

    # Open the pre-prompt file in preparation for feeding to the model
    with open(preprompt_file, "r") as f:
        preprompt = json.load(f)
    
    # Initialize variable for prompt as raw text
    prompt = json.dumps(preprompt, indent=None)

    # print(prompt)

    # Feed prompt to the model && print the response for the user && collect API feedback
    response = model.generate_content(prompt)
    feedback = response.prompt_feedback
    print(response)
    # print response
    print(f"\nGemini: {response.text}\n")

    # Append model response to context in preprompt file
    preprompt["context"]["context"].append({"message": f"Gemini: {response.text}"})
    with open(preprompt_file, "w") as f:
        json.dump(preprompt, f, indent=4)

    with open(feedback_file, "w") as f:
        f.write(str(feedback))
    
    # Loop break
    if current_prompt.lower() == "exit":
        break
