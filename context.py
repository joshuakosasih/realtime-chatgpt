import re
from openaiclient import generate_text
from collections import deque


class ContextKeeper:
    """
    ContextKeeper keeps track of a conversation's context.

    Methods:
        add_context(text: str) -> None: Add a new turn to the context.
        summarize_context() -> None: Summarize the context using OpenAI API.
        get_context() -> str: Return the full context as a string.
        add_turn(text: str) -> str: Add a user's turn to the context and generate a response.

    Attributes:
        engine (str): The name of the GPT engine to be used.
        max_context_turns (int): The maximum number of turns to keep in the context.
        max_context_size (int): The maximum number of characters to keep in the context.
        max_token (int): The maximum number of tokens to generate a response.
        temperature (float): The sampling temperature to generate a response.
    """

    def __init__(self, engine: str, max_context_turns: int = 50, max_context_size: int = 1024,
                 max_token: int = 512, temperature: float = 0.5) -> None:
        """
        Initialize the ContextKeeper object.

        Args:
            engine (str): The name of the GPT engine to be used.
            max_context_turns (int): The maximum number of turns to keep in the context.
            max_context_size (int): The maximum number of characters to keep in the context.
            max_token (int): The maximum number of tokens to generate a response.
            temperature (float): The sampling temperature to generate a response.
        """
        self.engine = engine
        self.context = deque()
        self.max_context_turns = max_context_turns
        self.max_context_size = max_context_size
        self.max_token = max_token
        self.temperature = temperature

    def add_context(self, text: str) -> None:
        """
        Add a new turn to the context.

        Args:
            text (str): The text to be added to the context.
        """
        # Clean and sanitize the input text
        text = re.sub('\s+', ' ', text.strip())

        # Append the input text to the context deque
        self.context.append(text)

        # Summarize the context and remove older turns if it becomes too large
        if len(self.context) >= self.max_context_turns or len(self.get_context()) >= self.max_context_size:
            self.summarize_context()

    def summarize_context(self) -> None:
        """
        Summarize the context using OpenAI API.
        """
        # Use OpenAI API to summarize the context
        prompt = 'Summarize the following conversation:\n\n'
        for turn in self.context:
            prompt += f'{turn}\n'
        response = self.try_generate(prompt)

        # Remove the entire context and replace it with the summary
        self.context.clear()
        self.context.append(response)

    def get_context(self) -> str:
        """
        Return the full context as a string.

        Returns:
            str: The full context.
        """
        return ' '.join(self.context)

    def add_turn(self, text: str) -> str:
        """
        Add a turn to the conversation and return the bot's response.

        Args:
            text (str): The user's text.

        Returns:
            str: The bot's response.
        """
        prompt = self.get_context() + "User: " + text + "\nBot:"
        response = self.try_generate(prompt)
        self.add_context("User: " + text + "\nBot: " + response + "\n")

        return response

    def try_generate(self, prompt: str) -> str:
        """
        Tries to generate a response based on the given prompt and returns the response text.

        Args:
            prompt (str): The input prompt to generate a response from.

        Returns:
            str: The generated response text.

        If an error occurs during response generation, this method returns a string indicating that
        the response generation failed.
        """
        try:
            return generate_text(prompt, self.engine, self.max_token, self.temperature)
        except:
            return "Sorry, failed to generate response"


class ContextManager:
    def __init__(self, model, temperature=0.5):
        self.model = model
        self.temperature = temperature
        self.contexts = {}

    def get_context(self, context_name):
        if context_name not in self.contexts:
            self.contexts[context_name] = ContextKeeper(self.model, self.temperature)
        return self.contexts[context_name]
