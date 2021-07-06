import invoiceapi as im

print(im.refreshaccessToken())

print(im.createCustomer({
    "contact_name": "ABC Enterprises",
    "company_name": "ABC Enterprises"
}))

customer_data = im.getCustomerById("576992000000014008")
print(customer_data)
print(customer_data['contact']['contact_name'])

print(im.getCustomerData())

print(im.updateCustomer("576992000000018014",{
    "contact_name": "ABC Enterprises",
    "company_name": "ABC Enterprises",
    "website": "www.abc.com"
    }
))

print(im.deleteCustomer("576992000000018014"))


