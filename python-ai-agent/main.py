import sys
import os
from google.genai import types
from client.call_model import Client, ResponseTypes, process_response, retrieve_candidates
from utils.cli import retrieve_cli_args
from functions.call_function import call_function


def main(client, cli_args):
    messages = [
        types.Content(
            role="user", 
            parts=[
                types.Part(text=cli_args.user_prompt)
                ]
            )
        ]
    response_type, result, response = None, None, None

    # Iterate response, limited to 20 times
    for _ in range(20):
        response = client.call_model(messages)
        messages = retrieve_candidates(response, messages)
        response_type, result = process_response(response)

        if response_type == ResponseTypes.FUNCTION:
            function_result = call_function(result)

            messages.append(
                types.Content(
                    role="user",
                    parts=function_result.parts
                )
            )

        elif response_type == ResponseTypes.TEXT:
            break
    else:
        sys.exit(1)

    if cli_args.verbose and response_type == ResponseTypes.FUNCTION:
        print(f"-> {result}")
    elif response_type == ResponseTypes.TEXT:
        print(response.text)
    else:
        raise RuntimeError("Unknown response type")

    if cli_args.verbose:
        print(f"User prompt: {cli_args.user_prompt}")

        if hasattr(response, "usage_metadata") and response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    # Get environment variables
    client = Client()

    # Parse arguments for a given command
    args = retrieve_cli_args()

    # Generate user response
    main(client, args)
