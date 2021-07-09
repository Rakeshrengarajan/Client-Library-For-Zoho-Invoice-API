# coding: utf-8

# Module Dependencies
import os
import util
from dotenv import load_dotenv
import requests

class Response:
    def __init__(self):
        self.organizationId=os.getenv('organizationId')
        code=util.Utils()
        self.authcode=code.refreshaccessToken()
        self.custom_header = {
            "Authorization": "Zoho-oauthtoken "+self.authcode,
            "X-in-zoho-invoice-organizationid":self.organizationId,
            "Content-Type":"application/json"
        }

    def getResposnse(self,method,url,parameters=None):
        return requests.request(method,url,headers=self.custom_header,params=parameters).json()
