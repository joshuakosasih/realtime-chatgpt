from typing import List

from crawler import extract_content_from_google
from openaiclient import generate_text
from settings import ModelProfile


def generate_keywords(text: str, profile: ModelProfile) -> List[str]:
    """
    Use GPT to generate Google search keywords.

    Args:
        text (str): The text to generate keywords for.
        profile (ModelProfile): The model profile to use for text generation.

    Returns:
        List[str]: The generated search keywords.
    """
    prompt = "Generate Google search keywords (in bullet points) for the following text:\n\n" + text
    response = generate_text(prompt, profile)

    # Parse bullet points and collect each keyword
    keywords = []
    for bullet in response.split('\n'):
        if bullet.startswith('• '):
            keyword = bullet[2:].strip()
            keywords.append(keyword)

    return keywords[:2]

def get_search_results(queries: List[str]) -> List[str]:
    """
    Get search results from Google and extract content from the top 5 results.

    Args:
        queries (List[str]): The list of search queries to perform.

    Returns:
        List[str]: The extracted contents from the search results.
    """
    contents = []
    for query in queries:
        contents.extend(extract_content_from_google(query))

    return contents


def summarize_contents(contents: List[str], profile: ModelProfile) -> str:
    """
    Use GPT to summarize the contents.

    Args:
        contents (List[str]): The contents to be summarized.
        profile (ModelProfile): The model profile to use for text generation.

    Returns:
        str: The summarized text.
    """
    prompt = 'Summarize the following contents as short as possible:\n\n'
    for content in contents:
        prompt += f'{content}\n'
    return generate_text(prompt, profile)


def process_input(text: str, profile: ModelProfile) -> str:
    """
    Extract the user's real prompt and summarize the associated contents.

    Args:
        text (str): The user's input.
        profile (ModelProfile): The model profile to use for text generation.

    Returns:
        List[str]: The summarized contents generated from the input.
    """
    prompt = text[6:].strip()

    # Generate search keywords and search for contents
    keywords = generate_keywords(prompt, profile)
    contents = get_search_results(keywords)

    # Summarize the contents and return them to be used to append context
    return summarize_contents(contents, profile)
