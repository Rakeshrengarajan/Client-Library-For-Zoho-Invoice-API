import requests

url="https://invoice.zoho.in/api/v3/"
authCode="1000.b37b7a19c2a687b29e134bf9153d264d.6b53faa5031a5cd30e97c2fda727da80"
organizationId="60009537409"


#To refreshing the access token
def refreshaccessToken():
    refresh_token="1000.555cde678787e30f4a3a4271d3ffbe90.cceb404578cd702f9a76573c5dedd464"
    client_ID="1000.DNGBS79IK786GTSFTPOFF93E1ZG37N"
    client_scerect="033b26b9ae1f533282c6b196882706e6f7b94ed788"
    global authCode
    url="https://accounts.zoho.in/oauth/v2/token?refresh_token="+refresh_token+"&client_id="+client_ID+"&client_secret="+client_scerect+"&redirect_uri=http://www.zoho.in/invoice&grant_type=refresh_token"
    res=requests.post(url)
    value=res.json()
    authCode = value['access_token']
    return authCode


#To create a new customer
def createCustomer(parameters):
    newurl=url+"contacts"
    custom_header = {"Authorization": "Zoho-oauthtoken "+authCode,
    "X-in-zoho-invoice-organizationid":organizationId,
    "Content-Type":"application/json"
    }
    value={'JSONString':str(parameters)}
    res = requests.post(newurl, headers = custom_header, params=value)
    return res.json()


#To get the customer by ID
def getCustomerById(customer_id):
    newurl=url+"contacts/"+customer_id
    custom_header = {"Authorization": "Zoho-oauthtoken "+authCode,
    "X-in-zoho-invoice-organizationid":organizationId,
    "Content-Type":"application/json"
    }
    res = requests.get(newurl,headers=custom_header)
    return res.json()

#To get all the customer data
def getCustomerData():
    newurl=url+"contacts"
    custom_header = {"Authorization": "Zoho-oauthtoken "+authCode,
    "X-in-zoho-invoice-organizationid":organizationId,
    "Content-Type":"application/json"
    }
    res = requests.get(newurl,headers=custom_header)
    return res.json()

#To update a customer data
def updateCustomer(customer_id,parameters):
    newurl=url+"contacts/"+customer_id
    custom_header = {"Authorization": "Zoho-oauthtoken "+authCode,
    "X-in-zoho-invoice-organizationid":organizationId,
    "Content-Type":"application/json"
    }
    value={'JSONString':str(parameters)}
    res = requests.put(newurl, headers = custom_header, params=value)
    return res.json()


    
#To delete a customer
def deleteCustomer(customer_id):
    newurl=url+"contacts/"+customer_id
    custom_header = {"Authorization": "Zoho-oauthtoken "+authCode,
    "X-in-zoho-invoice-organizationid":organizationId,
    "Content-Type":"application/json"
    }
    res = requests.delete(newurl,headers=custom_header)
    return res.json()
