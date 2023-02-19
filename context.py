import openai
import re

class ContextKeeper:
    def __init__(self, model, initial_prompt="", temperature=0.5):
        self.model = model
        self.prompt = initial_prompt
        self.temperature = temperature
        self.reset()
    
    def reset(self):
        self.context = ""
    
    def generate_text(self, prompt):
        full_prompt = self.prompt + " " + prompt
        response = openai.Completion.create(
            engine=self.model,
            prompt=full_prompt,
            temperature=self.temperature,
            max_tokens=1024,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0
        )
        self.prompt = full_prompt
        text = response.choices[0].text
        text = re.sub('[\n]{3,}', '\n\n', text)
        self.context += full_prompt + text
        return text
    
class ContextManager:
    def __init__(self, model, temperature=0.5):
        self.model = model
        self.temperature = temperature
        self.contexts = {}
        
    def get_context(self, context_name):
        if context_name not in self.contexts:
            self.contexts[context_name] = ContextKeeper(self.model, "", self.temperature)
        return self.contexts[context_name]
