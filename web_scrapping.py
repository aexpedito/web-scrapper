"""
Some file web scrapping description.
"""
import requests
from bs4 import BeautifulSoup

from src.web_scrapper import Web_Scrapper, Web_Scrapper_Factory
import pandas as pd


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
        max_articles = 852
        skip = self.skip
        show = self.show

        # salva no arquivo
        titles = []
        authors = []
        subjects = []

        while i < max_articles:
            i = skip
            tmp_url = self.url + "?skip={}&show={}".format(skip, show)
            html = requests.get(tmp_url)
            soup = BeautifulSoup(html.text, "html.parser")
            articles_dl = soup.find_all("dd")
            skip += show

            for article in articles_dl:
                title = article.find(class_="list-title")
                titles.append(title.text)

                author = article.find(class_="list-authors")
                authors.append(author.text)

                subject = article.find(class_="list-subjects")
                subjects.append(subject.text)


        df = pd.DataFrame(columns=['title', 'authors', 'subject'])
        df['title'] = titles
        df['authors'] = authors
        df['subject'] = subjects
        return df


    def persist(self, data) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                Web_Scrapper
        """
        data.to_csv('output.csv')

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
    data_df = web_scrapper.grab()
    web_scrapper.persist(data_df)

