from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order

def make_contract(symbol, sec_type, exch, prim_exch, curr):

    Contract.m_symbol = symbol
    Contract.m_secType = sec_type
    Contract.m_exchange = exch
    Contract.m_primaryExch = prim_exch
    Contract.m_currency = curr
    return Contract

def make_order(action,quantity, price = None):

    if price is not None:
        order = Order()
        order.m_orderType = 'LMT'
        order.m_totalQuantity = quantity
        order.m_action = action
        order.m_lmtPrice = price

    else:
        order = Order()
        order.m_orderType = 'MKT'
        order.m_totalQuantity = quantity
        order.m_action = action

        
    return order


cid = 303

while __name__ == "__main__":

    conn = Connection.create(port=7497, clientId=9898)
    conn.connect()
    oid = cid
    cont = make_contract('APLE', 'STK', 'SMART', 'SMART', 'USD')
    offer = make_order('BUY', 1, 200)
    conn.placeOrder(oid, cont, offer)
    offer_2 = make_order('SELL', 1, 200)
    conn.placeOrder(oid, cont, offer_2)


    cont = make_contract('EUR', 'STK', 'IDEALPRO', 'IDEALPRO', 'USD')
    offer = make_order('BUY', 1, 200)
    conn.placeOrder(oid, cont, offer)
    conn.disconnect()
    x = input('enter to resend')
    cid += 1