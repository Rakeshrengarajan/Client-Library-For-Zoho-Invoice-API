# coding: utf-8

# Module Dependencies
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Utils:
    def __init__(self,refresh_token=None,client_ID=None, client_sceret=None):
        self.client_ID=os.getenv('client_ID')
        self.client_sceret=os.getenv('client_sceret')
        self.refresh_token=os.getenv('refresh_token')
    
    def refreshaccessToken(self):
        client_ID=self.client_ID
        client_sceret=self.client_sceret
        refresh_token=self.refresh_token
        url="https://accounts.zoho.in/oauth/v2/token?refresh_token="+refresh_token+"&client_id="+client_ID+"&client_secret="+client_sceret+"&redirect_uri=http://www.zoho.in/invoice&grant_type=refresh_token"
        res=requests.post(url)
        value=res.json()      
        self.authcode = value['access_token']
        return self.authcode





