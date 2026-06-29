from ..providers.alpina.extractor import AlpinaExtractor
class RegistryExtractor:

    extractorList = [AlpinaExtractor]

    @classmethod
    def define_extractor(cls, texto):

        for extractor in extractorList:

            if extractor.matches(texto):

                return extractor();




