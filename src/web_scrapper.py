"""
Some docstring for validation pass.
This is a web_scrapper for Arxiv.
"""
from abc import abstractmethod

from src.singleton import Singleton


#
class Web_Scrapper(Singleton):
    """
    Abstract class for a Web Scrapper and Singleton.
    """
    @abstractmethod
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
        raise NotImplementedError

    @abstractmethod
    def grab(self) -> None:
        """
        Abstract class for a Web Scrapper.
        """
        raise NotImplementedError

    @abstractmethod
    def persist(self) -> None:
        """
        Abstract class for a Web Scrapper.
        """
        raise NotImplementedError



class Web_Scrapper_Factory(Singleton):
    """
        Abstract class for a Web Scrapper Factory pattern.

        Args:
            a
        Returns:
            None
    """
    @abstractmethod
    def create(self) -> Web_Scrapper:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                Web_Scrapper: return a web scrapper
        """
        raise NotImplementedError
