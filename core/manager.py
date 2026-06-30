# Cerebro del proceso de extracción.
# Llama al detector, localiza el proveedor, busca el extractor, lo ejecuta, muestra el resultado

from core.detector import FirstDetector;
from core.export import Export;
from core.pdf_document import PDFDocument;
class Manager:

    @classmethod
    def process(cls, pdf_path):

        print("[MANAGER] Iniciando proceso");

        pdfDocument = PDFDocument(pdf_path);

        print("[MANAGER] Detectando proveedor...");

        #acá recibe la instancia del extractor determinado por el PDF
        extractor = FirstDetector.detect(pdfDocument.firstPage);

        print(f"[MANAGER] Proveedor detectado: {extractor.NAME}")
        
        #acá recibe los datos extraídos en formato JSON
        resultado = extractor.extract(pdfDocument);
        #acá exporta los datos a un Excel listo para su importación al sistema determinado

        if(Export.export_to_excel(resultado, pdf_path) == 1):
            return 1;
        
        else:
            return 0;
        



