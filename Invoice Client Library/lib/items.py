# coding: utf-8

# Module Dependencies
import os
import util
from dotenv import load_dotenv
import requests

load_dotenv()

class Items:
    def __init__(self,url=None,authcode=None,organizationId=None):
        self.url="https://invoice.zoho.in/api/v3/"
        self.organizationId=os.getenv('organizationId')
        code=util.Utils()
        self.authcode=code.refreshaccessToken()
   
    
    #To create a new item
    def createItem(self, parameters):
        newurl=self.url+"items"
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        value={'JSONString':str(parameters)}
        res = requests.post(newurl, headers = custom_header, params=value)
        return res.json()

    #To get the item by ID
    def getItemById(self, item_id):
        newurl=self.url+"items/"+item_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.get(newurl,headers=custom_header)
        return res.json()

    #To get all the item data
    def getitemData(self):
        newurl=self.url+"items"
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.get(newurl,headers=custom_header)
        return res.json()

    #To update a item data
    def updateItem(self, item_id, parameters):
        newurl=self.url+"contacts/"+item_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        value={'JSONString':str(parameters)}
        res = requests.put(newurl, headers = custom_header, params=value)
        return res.json()
    
    #To delete a item
    def deleteItem(self, item_id):
        newurl=self.url+"contacts/"+item_id
        custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }
        res = requests.delete(newurl,headers=custom_header)
        return res.json()
