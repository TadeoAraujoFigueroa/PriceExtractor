import pdfplumber

class PDFDocument:

    def __init__(self, path):
        self.path = path;
        self._text = None;
    

    def get_first_page(self):
        if self._text is None:
            with pdfplumber.open(self.path) as pdf:
                self._text = pdf.pages[0].extract_text();
                return self._text;
        else:
            return self._text;

   