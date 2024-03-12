# gemini-cli

Use Google's Gemini-Pro at the command line!

## Prerequisites

**A Google AI Studio API Key is required to run this script.** 

You can get one [here](https://makersuite.google.com/app/apikey). 

Once you have your key, create a keys.py file to contain your api key in a global variable, like this:

> touch key.py

> echo google_ai_key = '123yourapikey' > keys.py

For this project's dependencies, refer to the requirements.txt file.

To get this script running, after you clone the repository to your system, navigate to it's parent directory and create a Python virtual environment in the project's directory:

> python3 -m venv gemini-cli

Then, navigate into the gemini-cli directory and activate the venv:

> source bin/activate

Finally, install the packages enumerated in the requirements.txt file.

> pip install -r requirements.txt

Once this is done, your venv should be all set to run gemini.py

## Configuration

Coming Soon!

## Usage

Sometimes Gemini will start responding in JSON due to the way I feed input to it. You can usually get it to stop by telling it to stop, or asking it to stop.

Logging the conversation and model instructions in a JSON file that I feed to the model on every message was necessary to maintain a sense of one continuous conversation.

**Without the preprompt.json file, Gemini has no memory of previous messages.**

Feel free to exercise your LLM jailbreaking techniques ans prompt engineering strategies by experimenting directly with the model instructions located in preprompt.json

Once you've cloned the repo, created the venv and installed the dependencies, you're ready to run gemini.py. Navigate to the directory that contains the script & use Python3 to execute the script.

> cd path/to/gemini-cli/

> python3 gemini.py

It will run in your current terminal session, and you will be prompted to input text:

> User:

Type whatever you want, and now you're talking to Gemini over the command line!

When you want to exit the script, type:

> exit

This will return you to the command line.

Have fun!
