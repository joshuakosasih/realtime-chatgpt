from crawler import extract_content_from_google

def generate_keywords(text):
    # Use GPT to generate Google search keywords
    prompt = "Generate Google search keywords for the following text:\n\n" + text
    return context_keeper.try_generate(prompt)


def get_search_results(queries):
    # Get search results from Google and extract content from the top 5 results
    contents = []
    for query in queries:
        contents.extend(extract_content_from_google(query))

    return contents


def summarize_contents(contents):
    # Use GPT to summarize the contents
    prompt = 'Summarize the following contents:\n\n'
    for content in contents:
        prompt += f'{content}\n'
    return context_keeper.try_generate(prompt)


def process_input(text):
    # Extract the user's real prompt
    prompt = text[6:].strip()

    # Generate search keywords and search for contents
    keywords = generate_keywords(prompt)
    contents = get_search_results(keywords)

    # Summarize the contents and append them as context
    summary = summarize_contents(contents)
    context_keeper.add_context(summary)

    # Return the response for the user's prompt
    return context_keeper.add_turn(prompt)
