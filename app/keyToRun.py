import os
import openai
import argparse
import re

def main():
    print("Running keyToRun.py")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    branding_result = generate_branding_snippet(user_input)
    keywords_result = generate_keywords(user_input)
    print(branding_result)
    print(keywords_result)

def generate_keywords(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate related branding keywords for {prompt}: "
    response = openai.Completion.create(model="text-davinci-003", prompt=enriched_prompt, temperature=0.1, max_tokens=64)

    #extract output text.
    keywords_text: str = response["choices"][0]["text"]
    #strip whitespace
    keywords_text = keywords_text.strip()
 
    return keywords_text


def generate_branding_snippet(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate upbeat branding snippet for {prompt}: "
    response = openai.Completion.create(model="text-davinci-003", prompt=enriched_prompt, temperature=0.1, max_tokens=200)
    
    #extract output text.
    branding_text: str = response["choices"][0]["text"]

    #strip whitespace
    branding_text = branding_text.strip()
    # add ... to truncated statements
    last_char = branding_text[-2]
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    return branding_text

if __name__ == "__main__":
    main()