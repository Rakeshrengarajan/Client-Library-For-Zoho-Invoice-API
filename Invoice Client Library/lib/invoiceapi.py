# coding: utf-8

# Module Dependencies
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Invoice_API_Client:
    def __init__(self,url=None,authcode=None,organizationId=None,client_ID=None,client_sceret=None,refresh_token=None):
        self.url="https://invoice.zoho.in/api/v3/"
        self.client_ID=os.getenv('client_ID')
        self.client_sceret=os.getenv('client_sceret')
        self.organizationId=os.getenv('organizationId')
        self.refresh_token=os.getenv('refresh_token')
        self.authcode=""
   

    #To refreshing the access token
    def refreshaccessToken(self):
        client_ID=self.client_ID
        client_sceret=self.client_sceret
        refresh_token=self.refresh_token
        url="https://accounts.zoho.in/oauth/v2/token?refresh_token="+refresh_token+"&client_id="+client_ID+"&client_secret="+client_sceret+"&redirect_uri=http://www.zoho.in/invoice&grant_type=refresh_token"
        res=requests.post(url)
        value=res.json()      
        self.authcode = value['access_token']
        return self.authcode

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
