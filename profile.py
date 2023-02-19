class ChatProfile:
    def __init__(self, engine, max_token=512, temperature=0.5):
        self.engine = engine
        self.max_token = max_token
        self.temperature = temperature
