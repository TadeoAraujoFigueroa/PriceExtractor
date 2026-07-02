import re 
from core.extractor_base import BaseExtractor

class CitricExtractor(BaseExtractor):
    
    NAME = "CITRIC";

    KEYWORDS = ["VENDOR", "CITRIC"];

    __datos = []

    #Esta función se encarga de obtener los datos pertinentes a partir del texto
    #extraído del PDF
    def extract(self, pdf):


        texto = pdf.allText;

        lineas = texto.split("\n")

        for linea in lineas:

            linea = linea.strip()

         
            # Buscar:
            # primer número = código
            # último número = precio

            numeros = self.__obtener_numeros(linea);
            precios = self.__obtener_precios(linea);


            if len(precios) < 7:
                continue
            else:   
                codigo = numeros[0]
                costo = precios[5] 
                costo_sugerido = precios[6]
                descripcion = self.__obtener_descripcion(linea, codigo);

                # evitar líneas basura
                if codigo and len(codigo) <= 4 and costo and len(costo) >= 3:

                    self.__datos.append({
                        "codigo": codigo,
                        "costo": costo,
                        "costo_sugerido": costo_sugerido,
                        "descripcion": descripcion
                    })
        return self.__datos

    def __obtener_numeros(self, linea):
        return re.findall(r"\d+", linea);
    
    def __obtener_precios(self, linea):
        return re.findall(r"\d[\d\s,.]*", linea)
        
    def __obtener_descripcion(self, linea, codigo):
        linea = linea.removeprefix(codigo);
        match = re.search(r"^(.*?)\s+\d+\s*\$", linea)
        if match:
            descripcion = match.group(1)
        else:
            descripcion = ""
        return descripcion;
