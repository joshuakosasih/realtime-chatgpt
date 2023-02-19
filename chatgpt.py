import openai
import os

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_text(prompt, model, max_tokens=1024, temperature=0.5):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

# example usage with context
model = "text-davinci-002"
prompt = "Hi, how do I bake a potato?"
result = generate_text(prompt, model, temperature=0.5, max_tokens=1024)
print(result)

