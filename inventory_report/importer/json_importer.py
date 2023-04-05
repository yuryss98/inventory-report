from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.lower().endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(file_name) as file:
            return json.load(file)
