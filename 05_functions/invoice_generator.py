def generate_invoice(customer_name="Guest", *items: str, **charges: float):
    total = 0.0
    print(f"Invoice for {customer_name}\n\n")
    if items:
        print("Items:")
    for item in items:
        print(f"- {item}")
    if charges:
        print("Charges:")
    for charge, amount in charges.items():
        total += amount
        # charge = charge[0].upper() + charge[1:]  # Capitalize the first letter
        charge = charge.capitalize()  # Capitalize the first letter
        print(f"{charge}: {amount}")
    print(f"Total Amount Due: ₹{total}")

# generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0)
# generate_invoice("Riya", tax=30.0)
# generate_invoice()
generate_invoice("John", "Pizza", "Coke")

# def generate_invoice(customer_name: str ="Guest", *items: str, **charges: float) -> str:
#     total = 0.0
#     inv_struc=[f"Invoice for {customer_name}: "]
#     if items:
#         inv_struc.append("Items:")
#         #print("Items:")
#     for item in items:
#         inv_struc.append(f"- {item}")
#         # print(f"- {item}")
#     if charges:
#         inv_struc.append("Charges:")
#         # print("Charges:")
#     for charge, amount in charges.items():
#         total += amount
#         charge = charge[0].upper() + charge[1:] 
#         inv_struc.append(f"{charge}: {amount}")
#         # print(f"{charge}: {amount}")
#     inv_struc.append(f"Total Amount Due: {total}")
#     # print(f"Total Amount Due: ₹{total}")
#     return "\\n".join(inv_struc)
