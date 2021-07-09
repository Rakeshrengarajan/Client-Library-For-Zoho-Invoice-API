# coding: utf-8

# Module Dependencies
from response import Response

class Items:
    def __init__(self):
        self.url="https://invoice.zoho.in/api/v3/items"
        self.res=Response()      
    
    #To create a new item
    def createItem(self, parameters):
        return self.res.getResposnse("post", self.url, parameters)

    #To get the item by ID
    def getItemById(self, item_id):
        return self.res.getResposnse("get", self.url+item_id)

    #To get all the item data
    def getitemData(self):
        return self.res.getResposnse("get", self.url)

    #To update a item data
    def updateItem(self, item_id, parameters):
        return self.res.getResposnse("put", self.url+item_id, parameters)       
    
    #To delete a item
    def deleteItem(self, item_id):
        return self.res.getResposnse("delete", self.url+item_id)
