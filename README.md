# gemini-cli

Use Google's Gemini-Pro at the command line!

## Prerequisites

This script was built on Ubuntu 22.04.3 using Python 3.10.12.

You can probably get this running on Ubuntu or another Linux distro, but I have no idea about Windows or MacOS, sorry & good luck.

**A Google AI Studio API Key is required to run this script.** 

You can get one [here](https://makersuite.google.com/app/apikey). 

Once you have your key, you can build the .env file via a terminal command, or you can run the config.py script.

There are also some required packages that I am working on listing here:

## Configuration

To build the .env file through the config.py script, you can navigate to the project's root directory and execute config.py, shown below:

> cd /your/path/to/gemini-cli && python3 config.py

If you prefer to build the file by command, you can copy this command modify it to reflect your actual path and api key, and run it:

> cd /your/path/to/gemini-cli && touch .env && echo KEY=123yourAPIkey > .env

Soon, the config.py script will allow reconfiguration of the pre-prompt.json file.

Currently, as long as you follow JSON syntax, you can modify pre-prompt.json manually. It is fed to the model as plain text since that is all it can interpret, *but* the gemini.py script can not read the file if there are syntax errors.

Aside from downloading the required packages, once you've completed these steps you should be ready to run gemini.py.

## Usage

To run it, navigate to the directory.

> cd path/to/gemini-cli/

Then, use Python3 to execute the script.

> python3 gemini.py

It will run in your current terminal session, and you will see a prompt for your text input, like this:

> User:   

Type whatever you want, and now you're talking to Gemini over the command line!

When you are done, and want to exit the script, type:

> exit

This will return you to the command line.
