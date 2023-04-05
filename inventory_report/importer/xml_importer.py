from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.lower().endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(file_name) as file:
            report_reader = xmltodict.parse(file.read())

            return report_reader["dataset"]["record"]
