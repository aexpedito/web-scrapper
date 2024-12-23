"""
Some file web scrapping description
"""
import requests
from bs4 import BeautifulSoup

"""
Start function
"""
if __name__ == "__main__":
    """
    Beggining
    """
    url = "https://arxiv.org/list/cs.AI/recent"
    html = requests.get(url)

    soup = BeautifulSoup(html.text, "html.parser")
