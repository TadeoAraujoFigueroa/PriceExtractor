class BaseExtractor:

    NAME = "";

    KEYWORDS = [];

    @classmethod
    def matches(cls, text):
        text = text.upper();
    
        return any(
            keyword.upper() in text
            for keyword in cls.KEYWORDS
        )
    
    def extract(self, pdf_path):
        raise NotImplementedError()