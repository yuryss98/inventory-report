import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def get_reports(path_file, type_report):
    get_file_extension = path_file[-4:].lower()

    files_extensions = {
        ".csv": InventoryRefactor(CsvImporter),
        ".xml": InventoryRefactor(XmlImporter),
        "json": InventoryRefactor(JsonImporter),
    }

    return files_extensions[get_file_extension].import_data(
        path_file, type_report
    )


def main():
    try:
        _, path_file, type_report = sys.argv

        print(get_reports(path_file, type_report), end="")

    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
