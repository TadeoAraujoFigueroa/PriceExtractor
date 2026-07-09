import pkgutil;
import importlib;
import inspect;
from core.extractor_base import BaseExtractor;

class RegistryExtractor:

    extractorList = [
    ]

  
    @classmethod
    def initialize(cls):
          try:
               # Cargar todos los módulos de extractores en el paquete "providers"
               package_name = "providers"
               package = importlib.import_module(package_name) #función que permite importar módulos de manera dinámica en tiempo de ejecución
          
               # Recorremos todos los módulos en el paquete y los importamos   
               for _, module_name, _ in pkgutil.iter_modules(package.__path__): #iter_modules devuelve un generador que produce una tupla con información sobre cada módulo encontrado en el paquete especificado
                    module = importlib.import_module(f"{package_name}.{module_name}.extractor") #una vez que tenemos el nombre del módulo, lo importamos dinámicamente utilizando importlib.import_module. Esto nos permite cargar el módulo en tiempo de ejecución y acceder a sus clases y funciones.
          
                    # Buscar clases que hereden de BaseExtractor y agregarlas a la lista
                    for name, obj in inspect.getmembers(module, inspect.isclass): # inspect.getmembers devuelve una lista de tuplas que contienen el nombre y el objeto de cada miembro del módulo que cumple con el predicado especificado (en este caso, inspect.isclass, que verifica si el miembro es una clase). Esto nos permite filtrar solo las clases definidas en el módulo.
                         if issubclass(obj, BaseExtractor) and obj is not BaseExtractor:
                              cls.extractorList.append(obj)

                    print(f"Se han cargado {len(cls.extractorList)} extractores: {[extractor.NAME for extractor in cls.extractorList]}");
          except Exception as e:
               print(f"Error al inicializar el registro de extractores: {e}");
     
    @classmethod
    def define_extractor(cls, texto):          
          for extractor in cls.extractorList:

                 if extractor.matches(texto):
                      return extractor();




