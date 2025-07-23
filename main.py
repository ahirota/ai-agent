import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose_flag = False

    inputs = sys.argv[1:]

    if not inputs:
        raise Exception("Program requires a prompt.\nPlease use format: python main.py \"your prompt here\"\nExample: python main.py \"What is the meaning of life?\"")

    if "--verbose" in inputs:
        verbose_flag = True

    args = []
    for arg in inputs:
        if not arg.startswith("--"):
            args.append(arg)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)
    if verbose_flag:
        print(f"User prompt: {inputs[0]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
