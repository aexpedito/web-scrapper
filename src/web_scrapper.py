"""
Some docstring for validation pass.
This is a web_scrapper for.
"""
from abc import abstractmethod

from singleton import Singleton


#
class Web_Scrapper(Singleton):
    """
        Abstract class for a Web Scrapper.

        Args:
            None
        Returns:
            None
    """
    @abstractmethod
    def config(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                a
            Returns:
                None
        """
        raise NotImplementedError

    @abstractmethod
    def grab(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                None
        """
        raise NotImplementedError

    @abstractmethod
    def persist(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                None
        """
        raise NotImplementedError

    def scrapping(self) -> None:
        """
            Abstract class for a Web Scrapper.

            Args:
                None
            Returns:
                None
        """
        self.captar()
        self.persist()


class Web_Scrapper_Factory(Singleton):
    """
        Abstract class for a Web Scrapper.

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
