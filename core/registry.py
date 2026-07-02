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
               package = importlib.import_module(package_name)
          
               # Recorremos todos los módulos en el paquete y los importamos   
               for _, module_name, _ in pkgutil.iter_modules(package.__path__):
                    module = importlib.import_module(f"{package_name}.{module_name}.extractor")
          
                    # Buscar clases que hereden de BaseExtractor y agregarlas a la lista
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                         if issubclass(obj, BaseExtractor) and obj is not BaseExtractor:
                              cls.extractorList.append(obj)
          except Exception as e:
               print(f"Error al inicializar el registro de extractores: {e}");
     
    @classmethod
    def define_extractor(cls, texto):    
          print(f"ExtractorList: {cls.extractorList}");       
          for extractor in cls.extractorList:

                 if extractor.matches(texto):
                      return extractor();




