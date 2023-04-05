import pytest
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@pytest.fixture
def products_list():
    return [
        {
            "id": 1,
            "nome_do_produto": "MESA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-05-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
        },
        {
            "id": 2,
            "nome_do_produto": "Coca-cola",
            "nome_da_empresa": "Coca-cola",
            "data_de_fabricacao": "2023-01-04",
            "data_de_validade": "2023-05-09",
            "numero_de_serie": "5449000000996",
            "instrucoes_de_armazenamento": "na geladeira",
        },
        {
            "id": 3,
            "nome_do_produto": "Cadeira",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-05-03",
            "data_de_validade": "2025-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
        },
    ]


def test_decorar_relatorio(products_list):
    report = ColoredReport(SimpleReport).generate(products_list)

    report_texts = [
        "Data de fabricação mais antiga:",
        "Data de validade mais próxima:",
        "Empresa com mais produtos:",
    ]

    report_dates = [
        "2022-05-03",
        "2023-05-09"
    ]

    company = "Forces of Nature"

    assert report == (
        f"\033[32m{report_texts[0]}\033[0m \033[36m{report_dates[0]}\033[0m\n"
        f"\033[32m{report_texts[1]}\033[0m \033[36m{report_dates[1]}\033[0m\n"
        f"\033[32m{report_texts[2]}\033[0m \033[31m{company}\033[0m"
    )
