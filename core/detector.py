# este código será el encargado de detectar a qué proveedor pertenece el archivo PDF para delegarlo
# a su extractor correspondiente
import pdfplumber 
from core.registry import RegistryExtractor;

class FirstDetector:
    #el detector recibe la primera página del PDF y se la envía al registro
    #para que corrobore a quien le pertenece
    @classmethod
    def detect(cls, texto): 
         print("[DETECTOR] Analizando primera página...")
         return RegistryExtractor.define_extractor(texto);

