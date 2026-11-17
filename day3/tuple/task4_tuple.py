subscribers = {
    "vahida@gmail.com",
    "aksha@gmail.com",
    "aman@gmail.com",
    "haniya@gmail.com"
}

customers = {
    "aksha@gmail.com",
    "shifa@gmail.com",
    "aman@gmail.com",
    "fatima@gmail.com"
}

no_purchase = subscribers - customers
no_subscription = customers - subscribers

print("Subscribers without purchase:", no_purchase)
print("Customers without subscription:", no_subscription)