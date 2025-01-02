"""
Singleton module for package.
"""

class Singleton(object):
    """
    Singleton class for web-scrapper.
    """

    def __new__(cls):
        """
        Singleton module for package.

        Returns
        -------
        object
            Return a single instance of web scrapper.
        """

        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
