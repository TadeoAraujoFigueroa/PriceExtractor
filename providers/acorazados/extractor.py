import re 
from core.extractor_base import BaseExtractor

class AcorazadosExtractor(BaseExtractor):
    
    NAME = "ACORAZADOS";

    KEYWORDS = ["LISTA-ACORAZADOS", "CUIDADO DE LA COCINA"];

    __datos = []

    #Esta función se encarga de obtener los datos pertinentes a partir del texto
    #extraído del PDF
    def extract(self, pdf):

        texto = pdf.allText;

        lineas = texto.split("\n")

        for linea in lineas:


            linea = linea.strip(); 
            # Buscar:
            # primer número = código
            # último número = precio

            numeros = self.__obtener_numeros(linea);
            precios = self.__obtener_precio(linea);

            if len(numeros) >= 2:

                codigo = numeros[0]
                precio = precios[-1]
                descripcion = self.__obtener_descripcion(linea, codigo, numeros[1]);
                # evitar líneas basura
                if len(codigo) >= 4 and len(precio) >= 3:

                    self.__datos.append({
                        "codigo": codigo,
                        "precio": precio,
                        "descripcion": descripcion
                    })

        return self.__datos

    def __obtener_numeros(self, linea):
        return re.findall(r"\d+\w?", linea);
    
    def __obtener_precio(self, linea):
        # Buscar el último número en la línea
        return re.findall(r"\d+\.?\d*\,*\d*", linea)

    def __obtener_descripcion(self, linea, codigo):
        linea_nueva = linea.removeprefix(codigo);
        # Eliminar el EAN de la línea
        linea_nueva_dos = linea_nueva.removeprefix(f" {ean}");
        match = re.search(r"^(.*?)\s*\d+\.?\d*\,?\d*", linea_nueva_dos)
        if match:
            descripcion = match.group(1)
        else:
            descripcion = ""
        return descripcion;