from customer import Customers
from invoice import Invoices
from items import Items
from util import Utils

class InvoiceMainClient:
    def __init__(self,customer=None,invoice=None,item=None):
        self.customer=Customers()
        self.invoice=Invoices()
        self.item=Items()

