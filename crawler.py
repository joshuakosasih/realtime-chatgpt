import requests
import re
from bs4 import BeautifulSoup
from googlesearch import search

def extract_content_from_google(query):
    results = []
    for url in search(query, num_results=5):
        try:
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

            # Find the main content of the web page
            content = soup.find('main') or soup.find('article') or soup

            # Remove unnecessary elements such as header, footer, ads, etc.
            for element in content(['header', 'footer', 'nav', 'aside']):
                element.decompose()

            text = content.get_text()

            # Remove repeated newline characters
            text = re.sub(r'\n{2,}', '\n', text)

            results.append(text)
        except:
            pass
    return results

