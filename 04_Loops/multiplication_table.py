List = []
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1,11,1):
        multiply = number * i 
        #print(f"{number} x {i} = {multiply}")  
        List.append(f"{number} x {i} = {multiply}")
print(List)
