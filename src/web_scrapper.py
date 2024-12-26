from abc import ABC, abstractmethod
from singleton import Singleton

#
class Web_Scrapper(Singleton):

    """
        Abstract class for a Web Scrapper

        Args:
            a
        Returns:
            None
    """
    @abstractmethod
    def config(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def grab(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def persist(self) -> None:
        raise NotImplementedError

    def scrapping(self) -> None:
        self.captar()
        self.persist()


class Web_Scrapper_Factory(Singleton):

    @abstractmethod
    def create(self) -> Web_Scrapper:
        raise NotImplementedError
