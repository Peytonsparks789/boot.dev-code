import os
from enum import Enum
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions


load_dotenv()


class ResponseTypes(Enum):
    TEXT = "text"
    FUNCTION = "function"


def setup_environment():
    return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def extract_function_call(response):
    candidate = response.candidates[0]

    for part in candidate.content.parts:
        if getattr(part, "function_call", None):
            return part.function_call

    return None


def validate_response(response):
    if response is None:
        raise RuntimeError("Model returned no response")

    if not hasattr(response, "candidates") or not response.candidates:
        raise RuntimeError("Response has no candidates")

    candidate = response.candidates[0]

    if not hasattr(candidate, "content") or not candidate.content:
        raise RuntimeError("Candidate has no content")

    content = candidate.content

    has_text = any(part.text for part in content.parts if hasattr(part, "text"))

    if not has_text and not extract_function_call(response):
        raise RuntimeError("Response contains neither text nor function call")


def resolve_response_type(response):
    function_call = extract_function_call(response)

    if function_call:
        return ResponseTypes.FUNCTION, function_call

    return ResponseTypes.TEXT, None


def process_response(response):
    validate_response(response)

    response_type, function_call = resolve_response_type(response)

    if response_type == ResponseTypes.FUNCTION:
        return response_type, function_call

    return response_type, response

def retrieve_candidates(response, messages):
    if not response.candidates:
        raise RuntimeError("No candidates found in response")

    for candidate in response.candidates:
        messages.append(candidate.content)

    return messages



class Client:
    def __init__(self):
        self.client = setup_environment()
        self.model = os.environ.get("GEMINI_MODEL")

    def call_model(self, messages):
        response = None

        for retry in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=messages,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=0,
                        tools=[available_functions],
                    ),
                )
                break
            except TimeoutError as e:
                if retry == 2:
                    raise e

        return response