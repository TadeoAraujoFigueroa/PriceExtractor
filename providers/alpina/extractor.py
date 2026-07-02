
import re 
from core.extractor_base import BaseExtractor

class AlpinaExtractor(BaseExtractor):
    
    NAME = "ALPINA";

    KEYWORDS = ["ALPINA", "Lista de Precios", "LISTA: VIP"];

    __datos = []

    #Esta función se encarga de obtener los datos pertinentes a partir del texto
    #extraído del PDF
    def extract(self, pdf):



        texto = pdf.allText;

        lineas = texto.split("\n")

        for linea in lineas:

            linea = linea.strip()
            print(repr(linea));
         
            # Buscar:
            # primer número = código
            # último número = precio

            numeros = self.__obtener_numeros(linea);
            
            if len(numeros) >= 2:

                codigo = numeros[0]
                precio = numeros[-1]
        
                # evitar líneas basura
                if len(codigo) <= 5 and len(precio) >= 3:

                    self.__datos.append({
                        "codigo": codigo,
                        "precio": precio,

                    })

        return self.__datos

    def __obtener_numeros(self, linea):
        return re.findall(r"\d+", linea);
    
   