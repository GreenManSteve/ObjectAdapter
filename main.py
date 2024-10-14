from adapter.adapter import VendAdapter
from vendor.vendor import Vendor

MOCKVENDOR = (VendAdapter(Vendor('London Stock Exchange', 46, 'City of London, Great Britain N1 4BU')),
              VendAdapter(Vendor('NYSE', 10, 'Broad Street'))
              )

CUSTOMER = MOCKVENDOR

def main():
    for cust in CUSTOMER:
        print('Customer name:{} *|* Address:{}'.format(cust.name, cust.address))


if __name__ == '__main__':
    main()
