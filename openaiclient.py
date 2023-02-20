import openai
import os

from settings import ModelProfile

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_text(prompt: str, profile: ModelProfile, stop="Human:") -> str:
    """
    Generate text using OpenAI's GPT-3 API.

    Args:
        prompt (str): The input prompt or text that the GPT-3 model will use to generate new text.
        profile (Profile): The profile object containing the OpenAI API key, engine ID, and other generation parameters.
        stop (str): The stop token
    Returns:
        str: The generated text as a string.
    """
    try:
        response = openai.Completion.create(
            prompt=prompt,
            engine=profile.engine,
            max_tokens=profile.max_token,
            temperature=profile.temperature,
            stop=stop  # if not given, gpt will continue talking to itself
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Sorry, failed to generate response, error: {e}"


# example usage with context
'''
model = "text-davinci-002"
prompt = "Hi, how do I bake a potato?"
result = generate_text(prompt, model, temperature=0.5, max_tokens=1024)
print(result)
'''
