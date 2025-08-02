customer = {"name":"John Doe", "age":32,"city":"New York"}
print(customer)
#Add "email" and "phone" to the dictionary.
customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"
print(customer)
#customer’s "name" and "city" values
print(customer["name"])
print(customer["city"])
#Check whether the key "email" exists in the dictionary
print("email" in customer)
#Delete the "age" field
customer.pop("age")
print(customer)
#Print all dictionary keys, values, and items
print(customer.keys())
print(customer.values())
print(customer.items())
#Remove and print the last inserted key-value pair
print(customer.popitem())
#Use .get() to access the key "membership" (which doesn’t exist, like removed phone in last command).
print(customer.get("phone")) #result None
customer["address"] = "221B Baker Street"
print(customer)