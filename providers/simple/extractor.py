import re
from core.extractor_base import BaseExtractor

class SimpleExtractor(BaseExtractor):

    NAME = "SIMPLE";

    KEYWORDS = ["SIMPLE"];

    __datos = []

    def extract(self, pdf):

        texto = pdf.allText;

        lineas = texto.split("\n");

        for linea in lineas:
            
            linea = linea.strip(); 
            # Buscar:
            # primer número = código
            # último número = precio

            numeros = self.__obtener_numeros(linea);
            precios = self.__obtener_precio(linea);

            

            if len(numeros) >= 2 and len(precios) >= 1:

                codigo = numeros[0]
                precio = precios[-1]
                descripcion = self.__obtener_descripcion(linea, codigo);
                print(f"Codigo: {codigo}, Precio: {precio}, Descripcion: {descripcion}");
                # evitar líneas basura
                if len(codigo) >= 4 and len(precio) >= 3:

                    self.__datos.append({
                        "codigo": codigo,
                        "precio": precio,
                        "descripcion": descripcion
                    })

        return self.__datos
        
    def __obtener_numeros(self, linea):
        return re.findall(r"\d+", linea);
    
    def __obtener_precio(self, linea):
        # Buscar el último número en la línea
        return re.findall(r"\$+\d+\,?\d*\.*\d*", linea);
    
    def __obtener_descripcion(self, linea, codigo):
        linea_nueva = linea.removeprefix(codigo);
        match = re.search(r"^(.*?)\s+\d+\s+\$", linea_nueva)
        if match:
            descripcion = match.group(1)
        else:
            descripcion = ""
        return descripcion

    