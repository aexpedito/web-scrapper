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
    def config(self, url, encoding, skip, show) -> None:
        """
        Abstract class for a Web Scrapper.

        Parameters
        -----------
        url: str
            Url for web page.
        encoding: str
            Web page encoding.
        skip: int
            Initial step to skip.
        show: int
            How many items to display in page.
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
    def persist(self, data) -> None:
        """
        Abstract class for a Web Scrapper.

        Parameters
        ------------
        data: Dataframe
            pd.Dataframe to persist

        Returns
        ------------
        None
            Nao retorna nada
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
