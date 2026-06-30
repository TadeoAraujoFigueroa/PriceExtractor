from abc import ABC, abstractmethod

class BaseExtractor(ABC):

    NAME = "";

    KEYWORDS = [];

    @classmethod
    def matches(cls, text):
        text = text.upper();
    
        return any(
            keyword.upper() in text
            for keyword in cls.KEYWORDS
        )
    
    @abstractmethod
    def extract(self, pdf_path):
        raise NotImplementedError()