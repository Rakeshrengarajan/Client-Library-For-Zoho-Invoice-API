import invoiceapi as im

API_obj=im.Invoice_API_Client()

print(API_obj.refreshaccessToken())

print(API_obj.createCustomer({
    "contact_name": "ABC Enterprises",
    "company_name": "ABC Enterprises"
}))

customer_data = API_obj.getCustomerById("576992000000014008")
print(customer_data)
print(customer_data['contact']['contact_name'])

print(API_obj.getCustomerData())

print(API_obj.updateCustomer("576992000000018014",{
    "contact_name": "ABC Enterprises",
    "company_name": "ABC Enterprises",
    "website": "www.abc.com"
    }
))

print(API_obj.deleteCustomer("576992000000018014"))


