# coding: utf-8

# Module Dependencies
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Utils:
    def __init__(self):
        self.client_ID=os.getenv('client_ID')
        self.client_sceret=os.getenv('client_sceret')
        self.refresh_token=os.getenv('refresh_token')
        self.authcode=None
    
    def refreshaccessToken(self):
        url="https://accounts.zoho.in/oauth/v2/token?refresh_token="+self.refresh_token+"&client_id="+self.client_ID+"&client_secret="+self.client_sceret+"&redirect_uri=http://www.zoho.in/invoice&grant_type=refresh_token"
        res=requests.post(url)      
        self.authcode = res.json()['access_token']
        return self.authcode
