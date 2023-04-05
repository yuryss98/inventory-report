import datetime


class SimpleReport:
    @classmethod
    def get_company_with_more_products(cls, reports):
        companies = {}

        for report in reports:
            if report["nome_da_empresa"] in companies:
                companies[report["nome_da_empresa"]] += 1
            else:
                companies[report["nome_da_empresa"]] = 1

        return max(companies, key=companies.get)

    @classmethod
    def get_old_manufacturing_date(cls, reports):
        return min(report["data_de_fabricacao"] for report in reports)

    @classmethod
    def get_the_closest_expiration_date(cls, reports):
        return min(
            report["data_de_validade"]
            for report in reports
            if datetime.datetime.strptime(
                report["data_de_validade"], "%Y-%m-%d"
            )
            > datetime.datetime.now()
        )

    @classmethod
    def generate(cls, reports):
        next_expiration_date = cls.get_the_closest_expiration_date(reports)
        old_manufacturing_date = cls.get_old_manufacturing_date(reports)
        company_with_more_products = cls.get_company_with_more_products(
            reports
        )

        return (
            f"Data de fabricação mais antiga: {old_manufacturing_date}\n"
            f"Data de validade mais próxima: {next_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
