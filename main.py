from context import ContextKeeper
from realtime import process_input

def main():
    # Create a ContextKeeper instance with a GPT engine
    engine = "gpt2"
    context_keeper = ContextKeeper(engine)

    # Start the conversation loop
    while True:
        # Prompt the user for input
        user_input = input("> You: ")
        if user_input.startswith('!real '):
            context_keeper.add_context(process_input(user_input))

        # Add the user input to the context and generate a response
        response = context_keeper.add_turn(user_input)

        # Print the response
        print(f"Bot: {response}")


if __name__ == '__main__':
    main()

