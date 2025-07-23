import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verboseFlag = False

    inputs = sys.argv[1:]

    if not inputs:
        raise Exception("Program requires a prompt.\nPlease use format: python main.py \"your prompt here\"\nExample: python main.py \"What is the meaning of life?\"")

    messages = [
        types.Content(role="user", parts=[types.Part(text=inputs[0])]),
    ]

    if "--verbose" in inputs:
        verboseFlag = True

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)
    if verboseFlag:
        print(f"User prompt: {inputs[0]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
