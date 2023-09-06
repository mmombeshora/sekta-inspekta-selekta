import requests
from bs4 import BeautifulSoup


def scrape_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(para.text for para in paragraphs)

        return text

    except requests.RequestException:
        return None
