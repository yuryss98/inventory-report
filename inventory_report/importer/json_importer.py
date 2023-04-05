from importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.lower().endswith(".json"):
            raise ValueError("Arquivo inválido")
