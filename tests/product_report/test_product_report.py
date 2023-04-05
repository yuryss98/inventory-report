from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        9,
        'Coca-cola',
        'Coca-cola',
        '2023-01-03',
        '2023-05-03',
        '5449000000996',
        'na geladeira'
    )

    assert new_product.__repr__() == (
        "O produto Coca-cola"
        " fabricado em 2023-01-03"
        " por Coca-cola com validade"
        " até 2023-05-03"
        " precisa ser armazenado na geladeira."
    )
