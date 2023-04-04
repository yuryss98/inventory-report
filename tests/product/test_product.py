from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        9,
        'Testing',
        'Test',
        '2023-04-03',
        '2030-04-03',
        '2UA449P',
        'deve passar'
    )

    assert new_product.id == 9
    assert new_product.nome_do_produto == 'Testing'
    assert new_product.nome_da_empresa == 'Test'
    assert new_product.data_de_fabricacao == '2023-04-03'
    assert new_product.data_de_validade == '2030-04-03'
    assert new_product.numero_de_serie == '2UA449P'
    assert new_product.instrucoes_de_armazenamento == 'deve passar'
