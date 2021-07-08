from main import InvoiceMainClient

im=InvoiceMainClient()

print(im.customer.getCustomerData())

print(im.item.getitemData())

print(im.invoice.getinvoiceData())

print(im.customer.createCustomer({
    "contact_name": "ABC Enterprises",
    "company_name": "ABC Enterprises"
}))

customer_data = im.customer.getCustomerById("576992000000014008")
print(customer_data)
print(customer_data['contact']['contact_name'])

print(im.customer.updateCustomer("576992000000018014",{
    "contact_name": "ABC Enterprises",
    "company_name": "ABC Enterprises",
    "website": "www.abc.com"
    }
))

print(im.customer.deleteCustomer("576992000000018014"))


