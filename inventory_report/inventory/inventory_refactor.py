from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, classImporter):
        self.importer = classImporter
        self.data = []

    def import_data(self, path, type_report):
        self.data += self.importer.import_data(path)

        types_of_reports = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }

        return types_of_reports[type_report].generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
