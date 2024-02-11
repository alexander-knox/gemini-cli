import os
global env_exists
global env_file
global api_key
env_file = '.env'

print("\nWelcome to the Gemini-CLI configuration script.\n\n> Checking .env file.")

def check_env():

    env_exists = False
    while env_exists == False:

        if os.path.exists(env_file):

            print('\n> .env file found.\n\n> Searching for key.')

            with open ('.env', 'r') as f:

                env_content = f.read()

                if len(env_content) > 0:

                    print(f'\n> Key found.\n\n> Please confirm: {env_content} | [y/n]')
                    key_validation = input()

                    if key_validation.lower() == 'y':

                        print('\n> Key validated.\n')
                        env_exists = True
                        build_preprompt()
                        # I know this is not great but im working on it
                    else:

                        build_env()
                        break
                else:

                    print('\n> Key not found.')
                    build_env()
                    break   
        else:

            print('\n> .env file not found.')
            build_env()
            break

    return env_exists

def build_env():

    env_exists = False
    while env_exists == False:

        print('\n> Submit Google AI Studio API Key.\n')
        api_key = input('KEY=')
        print(f'\n> Key received.\n\n> Please confirm: KEY={api_key} | [y/n]')
        key_validation = input()

        if key_validation.lower() == 'y':

            env_exists = True
            print('\n> Key validated.\n')
            with open ('.env', 'w') as f:

                f.write(f'KEY={api_key}')

            break

        else:

            build_env()
            break

def build_preprompt():
    print('> Checking preprompt.json\n')
    print('> Function under construction.\n\n> Exiting...')

check_env()