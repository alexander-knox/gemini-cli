# gemini-cli

Use Google's Gemini-Pro at the command line!

## Prerequisites

**A Google AI Studio API Key is required to run this script.** 

You can get one [here](https://makersuite.google.com/app/apikey). 

Once you have a key, create a file named .env inside of the gemini-cli directory. 

Inside of .env, initialize a variable named KEY with your API key as the value.

> cd /path/to/gemini-cli \\
> && touch .env \\
> && echo KEY=123yourAPIkey > .env

Now, aside from the required packages, you should be ready to run.

## Usage

This script was built on Ubuntu 22.04.3 using Python 3.10.12.

You can probably get this running on Ubuntu or another Linux distro, but I have no idea about Windows or MacOS, sorry.

To run it, clone the repo and navigate to the directory.

> cd path/to/gemini-cli/script/

Then, use Python3 to execute the script.

>python3 gemini.py

It will run in your current terminal session, and you will see a prompt for your text input, like this:

> User:   

Type whatever you want and now you're talking to Gemini over the command line!

When you are done, and want to exit the script, type:

> exit

This will return you to the command line.
