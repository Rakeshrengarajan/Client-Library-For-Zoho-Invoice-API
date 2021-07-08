# coding: utf-8

# Module Dependencies
import os
import util
from dotenv import load_dotenv
import requests

load_dotenv()

class Invoices:
    def __init__(self,url=None,authcode=None,organizationId=None):
        self.url="https://invoice.zoho.in/api/v3/"
        self.organizationId=os.getenv('organizationId')
        code=util.Utils()
        self.authcode=code.refreshaccessToken()
   
    
    #To create a new invoice
    def createInvoice(self, parameters):
        newurl=self.url+"invoices"
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        value={'JSONString':str(parameters)}
        res = requests.post(newurl, headers = custom_header, params=value)
        return res.json()

    #To get the invoice by ID
    def getInvoiceById(self, invoice_id):
        newurl=self.url+"invoices/"+invoice_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.get(newurl,headers=custom_header)
        return res.json()

    #To get all the invoice data
    def getinvoiceData(self):
        newurl=self.url+"invoices"
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.get(newurl,headers=custom_header)
        return res.json()

    #To update a invoices data
    def updateInvoice(self, invoice_id, parameters):
        newurl=self.url+"contacts/"+invoice_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        value={'JSONString':str(parameters)}
        res = requests.put(newurl, headers = custom_header, params=value)
        return res.json()
    
    #To delete a invoice
    def deleteInvoice(self, invoice_id):
        newurl=self.url+"contacts/"+invoice_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.delete(newurl,headers=custom_header)
        return res.json()
