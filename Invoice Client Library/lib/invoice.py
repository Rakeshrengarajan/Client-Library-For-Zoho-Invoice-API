# coding: utf-8

# Module Dependencies
from response import Response

class Invoices:
    def __init__(self):
        self.url="https://invoice.zoho.in/api/v3/invoices/"
        self.res=Response()
           
    #To create a new invoice
    def createInvoice(self, parameters):
        return self.res.getResposnse("post", self.url, parameters)

    #To get the invoice by ID
    def getInvoiceById(self, invoice_id):
        return self.res.getResposnse("get", self.url+invoice_id)

    #To get all the invoice data
    def getinvoiceData(self):
        return self.res.getResposnse("get", self.url)

    #To update a invoices data
    def updateInvoice(self, invoice_id, parameters):
        return self.res.getResposnse("put", self.url+invoice_id, parameters)
    
    #To delete a invoice
    def deleteInvoice(self, invoice_id):
        return self.res.getResposnse("delete", self.url+invoice_id)
