from providers.alpina.extractor import AlpinaExtractor
class RegistryExtractor:

    extractorList = [
         AlpinaExtractor
    ]

    @classmethod
    def define_extractor(cls, texto):         
            for extractor in cls.extractorList:
                 print(f"[REGISTRY] Probando {extractor.NAME}")
                 print(extractor.KEYWORDS);

                 if extractor.matches(texto):
                      print(f"[REGISTRY] Coincidencia encontrada: {extractor.NAME}")
                      return extractor();




