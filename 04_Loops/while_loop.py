Messages = []
withdrawals = [1,4,5,7,8,3]
balance = 15

index = 0
while index < len(withdrawals):
    i = withdrawals[index]
    if(balance >= i):
        balance -= i
        Messages.append(f"Withdrawn: {i}")
    else:
        Messages.append(f"insufficient funds for requested amount: {i}")
    index += 1
Messages.append(f"Remaining Balance: {balance}")
print(Messages)
    

# for i in withdrawals:
#     if(balance > i):
#         Messages.append(f"Withdrawn: {i}")
#         balance -= i
#     else:
#         Messages.append(f"Insufficient funds for requested amount: {i}")
#         break
    
# Messages.append(f"Remaining Balance: {balance}")
# print(Messages)


