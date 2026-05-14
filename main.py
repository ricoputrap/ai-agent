import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API key is not found.")


def main():
    print("Hello from ai-agent!")
    client = genai.Client(api_key=api_key)
    PROMPT = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    )
 
    usage = response.usage_metadata
    if usage is None:
        raise RuntimeError("ERROR: Failed to getting response from AI.")

    print(f"User prompt: {PROMPT}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
