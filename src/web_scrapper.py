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

        Args:
            None
        Returns:
            None
    """
    @abstractmethod
    def config(self) -> None:
        """
            Abstract method to config a Web Scrapper.

            Args:
                url: base URL for web page
                encoding: page encoding, UTF-8
            Returns:
                None
        """
        raise NotImplementedError

    @abstractmethod
    def grab(self) -> None:
        """
            Abstract method to grab data to a Web Scrapper.

            Args:
                None
            Returns:
                None
        """
        raise NotImplementedError

    @abstractmethod
    def persist(self) -> None:
        """
            Abstract method to persist data from grab for a Web Scrapper.

            Args:
                None
            Returns:
                None
        """
        raise NotImplementedError

    def scrapping(self) -> None:
        """
            Abstract method for Scrapping.

            Args:
                None
            Returns:
                None
        """
        self.grab()
        self.persist()


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
                Web_Scrapper
        """
        raise NotImplementedError
