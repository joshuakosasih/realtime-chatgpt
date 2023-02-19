import openai
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_text(prompt: str, engine_model: str, max_tokens: int = 1024, temperature: float = 0.5) -> str:
    """
    Generate text using OpenAI's GPT-3 API.

    Args:
        prompt (str): The input prompt or text that the GPT-3 model will use to generate new text.
        engine_model (str): The name of the OpenAI engine and model to use for generating text.
        max_tokens (int): The maximum number of tokens to generate in the output text.
        temperature (float): Controls the randomness and creativity of the generated text.

    Returns:
        str: The generated text as a string.
    """
    try:
        response = openai.Completion.create(
            prompt=prompt,
            engine=engine_model,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].text.strip()
    except:



# example usage with context
'''
model = "text-davinci-002"
prompt = "Hi, how do I bake a potato?"
result = generate_text(prompt, model, temperature=0.5, max_tokens=1024)
print(result)
'''