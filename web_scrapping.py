"""
Some file web scrapping description.
"""
import requests
from bs4 import BeautifulSoup

from src.web_scrapper import Web_Scrapper, Web_Scrapper_Factory


class Arxiv_Web_Srapper(Web_Scrapper):
    """
        Abstract class for a Web Scrapper and Singleton.

        Args:
            None
        Returns:
            None
    """
    def config(self, url: str, encoding: str, skip: int, show: int) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                url: url for web page
                encoding: web page encoding
                skip: initial step to skip
                show: how many items to display in page
            Returns:
                Web_Scrapper
        """
        self.url = url
        self.encoding = encoding
        self.skip = skip
        self.show = show


    def grab(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                Web_Scrapper
        """
        i = 0
        max_articles = 839
        skip = self.skip
        show = self.show

        while i < max_articles:
            tmp_url = self.url + "?skip={}&show={}".format(skip, show)
            html = requests.get(tmp_url)
            soup = BeautifulSoup(html.text, "html.parser")
            articles_dl = soup.find_all("dd")
            skip += show
            i+=1


    def persist(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                Web_Scrapper
        """
        pass

    def scrapping(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                None
        """
        pass


class Arxiv_Scrapper_Factory(Web_Scrapper_Factory):
    """
        Abstract class for a Web Scrapper and Singleton.

        Args:
            None
        Returns:
            None
    """
    def create(self) -> Web_Scrapper:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                Web_Scrapper: return a web scrapper
        """
        return Arxiv_Web_Srapper()


"""
Start function
"""
if __name__ == "__main__":
    """
    Beggining
    """
    url = "https://arxiv.org/list/cs.AI/recent" #?skip=0&show=100
    encoding = "utf-8"
    skip = 0
    show = 100
    #html = requests.get(url)
    #soup = BeautifulSoup(html.text, "html.parser")

    web_scrapper = Arxiv_Scrapper_Factory().create()
    web_scrapper.config(url, encoding, skip, show)
    web_scrapper.grab()
