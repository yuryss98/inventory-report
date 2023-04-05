from inventory_report.reports import simple_report, complete_report
from inventory_report.importer import csv_importer, json_importer, xml_importer


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        reports = []

        if path.lower().endswith("csv"):
            reports = csv_importer.CsvImporter.import_data(path)
        elif path.lower().endswith("xml"):
            reports = xml_importer.XmlImporter.import_data(path)
        else:
            reports = json_importer.JsonImporter.import_data(path)

        if type_report == "simples":
            return simple_report.SimpleReport.generate(reports)
        else:
            return complete_report.CompleteReport.generate(reports)
