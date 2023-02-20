
class ModelProfile:
    """
    A class representing the profile of a GPT model, which includes the OpenAI engine ID to use, the maximum number of
    tokens to generate, and the temperature of the generated text.

    Attributes:
        engine (str): The ID of the OpenAI engine to use for generating text.
        max_token (int): The maximum number of tokens to generate in the generated text.
        temperature (float): The temperature to use when generating text. Higher temperatures will result in more
            diverse and creative text, while lower temperatures will result in more predictable and conservative text.
    """
    def __init__(self, engine="text-davinci-003", max_token=512, temperature=0.5):
        self.engine = engine
        self.max_token = max_token
        self.temperature = temperature
