from context import ContextKeeper
from profile import ModelProfile
from realtime import process_input


def main():
    # Create a ContextKeeper instance with a GPT engine
    engine = "davinci"
    context_keeper = ContextKeeper(engine)
    model_profile = ModelProfile()

    # Start the conversation loop
    while True:
        # Prompt the user for input
        user_input = input("> You: ")
        if user_input.startswith('!real '):
            context_keeper.add_context(process_input(user_input, model_profile))
            user_input = user_input[6:]

        # Add the user input to the context and generate a response
        response = context_keeper.add_turn(user_input)

        # Print the response
        print(f"Bot: {response}")


if __name__ == '__main__':
    main()

