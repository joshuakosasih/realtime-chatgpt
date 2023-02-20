import re
from openaiclient import generate_text
from collections import deque

from settings import ModelProfile


class ContextKeeper:
    """
    ContextKeeper keeps track of a conversation's context.

    Methods:
        add_context(text: str) -> None: Add a new turn to the context.
        summarize_context() -> None: Summarize the context using OpenAI API.
        get_context() -> str: Return the full context as a string.
        add_turn(text: str) -> str: Add a user's turn to the context and generate a response.

    Attributes:
        context (List[str]): A list of conversation contexts.
        max_context_turns (int): The maximum number of turns to keep in the context.
        max_context_size (int): The maximum number of characters to keep in the context.
        profile (ModelProfile): An instance of the ModelProfile class that holds the GPT model configuration.
    """

    def __init__(self, max_context_turns=50, max_context_size=1024, profile=None):
        """
        Initialize the ContextKeeper object.

        Args:
        - max_context_turns (int): The maximum number of turns to store in the context.
        - max_context_size (int): The maximum number of tokens to store in the context.
        - profile (ModelProfile): The profile containing the settings for the language model.
        """
        self.context = deque()
        self.max_context_turns = max_context_turns
        self.max_context_size = max_context_size
        self.profile = profile
        if self.profile is None:
            self.profile = ModelProfile()
        self.reset_context()

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

    def reset_context(self) -> None:
        self.context.clear()
        self.add_context("The following is a conversation with an AI assistant. "
                         "The assistant is helpful, creative, clever, and very friendly.")
        self.add_context("Human: Hello, who are you?")
        self.add_context("AI: I am an AI created by OpenAI. How can I help you today?")

    def summarize_context(self) -> None:
        """
        Summarize the context using OpenAI API.
        """
        # Use OpenAI API to summarize the context
        prompt = 'Summarize the following conversation between a human and an AI as short as possible:\n\n'
        self.context.popleft()
        for turn in self.context:
            prompt += f'{turn}\n'
        response = generate_text(prompt, self.profile, None)

        # Remove the entire context and replace it with the summary
        self.reset_context()
        self.context.append(response)

    def get_context(self) -> str:
        """
        Return the full context as a string.

        Returns:
            str: The full context.
        """
        return '\n'.join(self.context)

    def add_turn(self, text: str) -> str:
        """
        Add a turn to the conversation and return the bot's response.

        Args:
            text (str): The user's text.

        Returns:
            str: The bot's response.
        """
        prompt = self.get_context() + "\nHuman: " + text + "\nAI:"
        response = generate_text(prompt, self.profile)
        self.add_context("Human: " + text + "\nAI: " + response + "\n")

        return response


class ContextManager:
    def __init__(self, model, temperature=0.5):
        self.model = model
        self.temperature = temperature
        self.contexts = {}

    def get_context(self, context_name):
        if context_name not in self.contexts:
            self.contexts[context_name] = ContextKeeper()
        return self.contexts[context_name]
