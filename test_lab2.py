import logging
import ecommerce_form

logging.basicConfig(
    level=logging.DEBUG,
    filename = 'test.log',
    filemode = 'w'
    )




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

