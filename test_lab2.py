import logging
import ecommerce_form
import pytest

logging.basicConfig(
    level=logging.DEBUG,
    filename = 'test.log',
    filemode = 'w'
    )

@pytest.fixture
def system():
    return ecommerce_form.OnlinePurchase()

@pytest.mark.parametrize('quantity, expected', [(8, True), (0, False), (-1, False), (.8, False)])
@pytest.mark.unit
def test_validate_quantity_component(system, quantity, expected):
    result = system.validate_quantity(quantity)
    assert result == expected

@pytest.mark.parametrize('coupon, expected', [('DISCOUNT10', True), ('DISCOUNT20', True), ('DISCOUNT30', False), ('DISCOUNT40', False)])
@pytest.mark.unit
def test_validate_quantity_component(system, coupon, expected):
    result = system.validate_coupon(coupon)
    assert result == expected

@pytest.mark.parametrize('address, expected', [('Av patria', True), ('tres', False), ('223345', False)])
@pytest.mark.wip
def test_validate_address(system, address, expected):
    result = system.validate_address(address)
    assert result == expected

@pytest.mark.system
def test_item_invalid():
    logging.info('TEST CASE 1:RF1(NEGATIVE)')

    system = ecommerce_form.OnlinePurchase()

    cart = {
        'Laptop': 0,
        'Mouse': 2
    }
    coupon = 'DISCOUNT10'
    address = 'Av. Patria '
    result = system.process_purchase(cart, coupon, address)
    logging.info(f'The Purchase result is:{result}')

    assert 'greater than 0' in result 

@pytest.mark.system
def test_invalid_coupon():
    logging.info('TEST CASE 2:RF3(NEGATIVE)')

    system = ecommerce_form.OnlinePurchase()

    cart = {
        'Laptop': 1,
        'Mouse': 2
    }
    coupon = 'DISCOUNT30'
    address = 'Av. Patria '
    result = system.process_purchase(cart, coupon, address)

    logging.info(f'The Purchase result is:{result}')

    assert 'code is not valid' in result 

@pytest.mark.system
def test_check_descount():
    logging.info('TEST CASE 3:RF9(POSITIVE)')

    system = ecommerce_form.OnlinePurchase()

    cart = {
        'Laptop': 1,   #1000
        'Mouse': 2     #50
    }
    coupon = 'DISCOUNT10'
    address = 'Av. Patria '
    result = system.process_purchase(cart, coupon, address)

    logging.info(f'The Purchase result is:{result}')

    assert '990' in result 

if __name__ == '__main__':


    logging.info('START')

