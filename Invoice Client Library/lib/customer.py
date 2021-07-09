# coding: utf-8

# Module Dependencies
from response import Response

class Customers:
    def __init__(self):
        self.url="https://invoice.zoho.in/api/v3/contacts/"
        self.res=Response()
   
    #To create a new customer
    def createCustomer(self, parameters):
        return self.res.getResposnse("post",self.url,parameters)

    #To get the customer by ID
    def getCustomerById(self, customer_id):
        return self.res.getResposnse("get", self.url+customer_id)

    #To get all the customer data
    def getCustomerData(self):
        return self.res.getResposnse("get",self.url)

    #To update a customer data
    def updateCustomer(self, customer_id, parameters):
        return self.res.getResposnse("put", self.url+customer_id,parameters)
    
    #To delete a customer
    def deleteCustomer(self, customer_id):
        return self.res.getResposnse("delete", self.url+customer_id)
