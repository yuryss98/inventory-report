from inventory_report.reports import simple_report, complete_report
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def open_json(cls, path):
        with open(path) as file:
            return json.load(file)

    @classmethod
    def open_csv(cls, path):
        with open(path, "r") as file:
            report_reader = csv.DictReader(file)

            return list(report_reader)

    @classmethod
    def open_xml(cls, path):
        with open(path) as file:
            report_reader = xmltodict.parse(file.read())

            return report_reader["dataset"]["record"]

    @classmethod
    def import_data(cls, path, type_report):
        reports = []

        if path.lower().endswith("csv"):
            reports = cls.open_csv(path)
        elif path.lower().endswith("xml"):
            reports = cls.open_xml(path)
        else:
            reports = cls.open_json(path)

        if type_report == "simples":
            return simple_report.SimpleReport.generate(list(reports))
        else:
            return complete_report.CompleteReport.generate(list(reports))
