# Python AI Agent
> _**DISCLAIMER:**_ This project is purely for academic purposes and does not have the proper security measures to ensure that this agent is 100% safe. Please do not use this within any production environment.

## Project Structure
Below is a high-level overview of the projejct structure
```
python_ai_agent/
├── calculator/      # Calculator tool logic. Used for testing purposes
├── client/          # Gemini API client wrapper
├── functions/       # Tool/Function declarations for the agent
├── utils/           # CLI and helper utilities
├── main.py          # Application entry point
├── config.py        # Global configurations
├── prompts.py       # System instructions/prompts
└── tests/           # Test suite for functions
```

## Model
Currently, the code provided was built using the Gemini API. Gemini 2.5 Flash was used when testing application functionality.

## Setup
To begin using this toy agent, ensure a .env file is set up with the following params.
- GEMINI_API_KEY
  - The api key generated from the Google AI Studio dashboard.
- GEMINI_MODEL
  - Gemini-2.5-Flash was used when testing the agent.

## CLI
To interact with the agent, argparser was used to handle basic inputs. The CLI for this application is extremely primitive and takes two primary inputs for args.
- user_prompt
  - String input that acts as the message that we are directing to the agent.
- --verbose
  - Basic boolean value that dictates whether more in-depth logging should be printed with the agents output.

## Available Agent Functions
- get_files_info
  - Retrieves a list of files in a given directory.
- get_file_content
  - Retrieves and reads the contents of a file.
- run_python_file
  - Runs a specified python file.
- write_file
  - Edits the content of a specified file.