import pdfplumber

class PDFDocument:

    def __init__(self, path):
        self.__path = path;
        self.__first_page = None;
        self.__all_text = None;
        #self.__file_name = None;
    
    def getFileName(self):
        return self.__path;
    
    def getAllText(self):
        if self.__all_text is None:
            with pdfplumber.open(self.__path) as pdf:

                textos = []

                for pagina in pdf.pages:
                    texto = pagina.extract_text()
                    if texto:
                        textos.append(texto);

                self.__all_text = "\n".join(textos);
                
                return self.__all_text;
        else:
            return self.__all_text;

    def getFirstPage(self):
        if self.__first_page is None:
            with pdfplumber.open(self.__path) as pdf:
                self.__first_page = pdf.pages[0].extract_text();
                return self.__first_page;
        else:
            return self.__first_page;

    firstPage = property(getFirstPage);
    allText = property(getAllText);
    fileName = property(getFileName);
   