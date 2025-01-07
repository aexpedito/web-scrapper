"""
Some file web scrapper description.
"""
import sys

import pandas as pd
import requests
from bs4 import BeautifulSoup

from src.web_scrapper import Web_Scrapper, Web_Scrapper_Factory


class Arxiv_Web_Srapper(Web_Scrapper):
    """
    Abstract class for a Web Scrapper and Singleton.

    Attributes
    ----------
    url : str
        A URL utilizada para scrapping.
    encoding : str
        O encoding da pagina.
    skip : int
        Relacionado a paginação da web page.
    show : int
        A quantidade de articles da pagina.
    data : pandas.Dataframe
        O Dataframe contendo os dados.
    max_articles : int
        Numero maximo de articles para salvar.

    Methods
    --------
    config()
        Configura o web scrapper.
    grab()
        Captura os dados para web scrapper.
    persist()
        Persiste os dados capturados
    scrapping()
        Roda o grab() e o persist()
    """
    def config(self, url, encoding, skip, show, max_articles) -> None:
        """
        Configure web scrapper parameters.

        Parameters
        ----------
        url : str
            Url for web page.
        encoding : str
            Web page encoding.
        skip : int
            Initial step to skip.
        show : int
            How many items to display in page.
        max_articles : int
            Number of articles to save in .csv.
        """
        self.url = url
        self.encoding = encoding
        self.skip = skip
        self.show = show
        self.data = None
        self.max_articles = max_articles

    def grab(self) -> None:
        """
        Abstract class for a Web Scrapper.
        """
        i = 0
        max_articles = self.max_articles
        skip = self.skip
        show = self.show

        # salva no arquivo
        titles = []
        authors = []
        subjects = []

        while skip < max_articles:
            tmp_url = self.url + "?skip={}&show={}".format(skip, show)
            html = requests.get(tmp_url)
            soup = BeautifulSoup(html.text, "html.parser")
            articles_dl = soup.find_all("dd")

            for article in articles_dl:
                title = article.find(class_="list-title")
                titles.append(title.text)

                author = article.find(class_="list-authors")
                authors.append(author.text)

                subject = article.find(class_="list-subjects")
                subjects.append(subject.text)
                i += 1
                if i >= max_articles:
                    skip = max_articles
                    break
            skip += show


        df = pd.DataFrame(columns=['title', 'authors', 'subject'])
        df['title'] = titles
        df['authors'] = authors
        df['subject'] = subjects
        self.data = df


    def persist(self) -> None:
        """
        Persist data to a csv.
        """
        self.data.to_csv('output.csv')



class Arxiv_Scrapper_Factory(Web_Scrapper_Factory):
    """
    Abstract class for a Web Scrapper and Singleton.
    """
    def create(self) -> Web_Scrapper:
        """
        Abstract class for a Web Scrapper.

        Returns
        -------
        Web_Scrapper
            Return a web scrapper.
        """
        return Arxiv_Web_Srapper()


"""
Start function
"""
if __name__ == "__main__":
    """
    In order to run first parameter is max_articles to grab from given URL.
    """
    url = "https://arxiv.org/list/cs.AI/recent" #?skip=0&show=100
    encoding = "utf-8"
    skip = 0
    show = 100
    max_articles = int(sys.argv[1])
    print("Scrapping {} articles ...".format(max_articles))

    web_scrapper = Arxiv_Scrapper_Factory().create()
    web_scrapper.config(url, encoding, skip, show, max_articles)
    web_scrapper.grab()
    web_scrapper.persist()
