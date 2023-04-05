from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if not file_name.lower().endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(file_name, "r") as file:
            report_reader = csv.DictReader(file)

            return list(report_reader)
