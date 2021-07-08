# coding: utf-8

# Module Dependencies
import os
import util
from dotenv import load_dotenv
import requests

load_dotenv()

class Customers:
    def __init__(self,url=None,authcode=None,organizationId=None):
        self.url="https://invoice.zoho.in/api/v3/"
        self.organizationId=os.getenv('organizationId')
        code=util.Utils()
        self.authcode=code.refreshaccessToken()
   
    #To create a new customer
    def createCustomer(self, parameters):
        newurl=self.url+"contacts"
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        value={'JSONString':str(parameters)}
        res = requests.post(newurl, headers = custom_header, params=value)
        return res.json()

    #To get the customer by ID
    def getCustomerById(self, customer_id):
        newurl=self.url+"contacts/"+customer_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.get(newurl,headers=custom_header)
        return res.json()

    #To get all the customer data
    def getCustomerData(self):
        newurl=self.url+"contacts"
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.get(newurl,headers=custom_header)
        return res.json()

    #To update a customer data
    def updateCustomer(self, customer_id, parameters):
        newurl=self.url+"contacts/"+customer_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        value={'JSONString':str(parameters)}
        res = requests.put(newurl, headers = custom_header, params=value)
        return res.json()
    
    #To delete a customer
    def deleteCustomer(self, customer_id):
        newurl=self.url+"contacts/"+customer_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.delete(newurl,headers=custom_header)
        return res.json()
