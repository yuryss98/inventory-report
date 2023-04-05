from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path: str, type_report):
        get_file_extension = path[-4:].lower()

        files_extensions = {
            ".csv": CsvImporter,
            ".xml": XmlImporter,
            "json": JsonImporter,
        }

        types_of_reports = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }

        reports = files_extensions[get_file_extension].import_data(path)

        return types_of_reports[type_report].generate(reports)
