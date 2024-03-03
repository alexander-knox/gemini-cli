# gemini-cli

Use Google's Gemini-Pro at the command line!

## Prerequisites

**A Google AI Studio API Key is required to run this script.** 

You can get one [here](https://makersuite.google.com/app/apikey). 

Once you have your key, create a keys.py file and containing your api key in a global variable, like this:

> google_ai_key = '123yourapikey'

For this projects dependencies, please refer to the requirements.txt file.

After you clone this repository to your system, navigate to it's parent directory and create a Python virtual environment in this project's directory like this:

> python3 -m venv gemini-cli

Then, navigate into the gemini-cli directory and activate the venv:

> source bin/activate

And finally, install the packages enumerated in the requirements.txt file.

> pip install -r requirements.txt

Once that is done, your venv should be all set to run gemini.py

## Configuration

Coming Soon!

## Usage

Sometimes Gemini will start responding in JSON syntax due to the way input is fed to it. You can usually get it to stop by telling or asking it to stop.

Logging the conversation and model instructions in a JSON file that I feed to the model on every message was necessary to maintain a sense of one continuous conversation.

**Without the preprompt.json file, Gemini has no memory of previous messages.**

Feel free to experiment with the model instructions found in prepompt.json to modify or alter Gemini's behavior.

Now,

To run gemini.py, navigate to the directory that contains it & use Python3 to execute the script.

> cd path/to/gemini-cli/

> python3 gemini.py

It will run in your current terminal session, and you will see a prompt for your text input, like this:

> User:   

Type whatever you want, and now you're talking to Gemini over the command line!

When you are done, and want to exit the script, you can type:

> exit

This will return you to the command line.