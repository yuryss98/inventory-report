from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, reports):
        partial_report = super().generate(reports)
        total_products_by_companies = super().get_total_products_by_companies(
            reports
        )

        partial_report += "\nProdutos estocados por empresa:\n"

        for company, quantity in total_products_by_companies.items():
            partial_report += f"- {company}: {quantity}\n"

        return partial_report
