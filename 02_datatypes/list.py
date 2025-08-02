my_cart = ["apples","bananas","milk"]
print(my_cart)
my_cart.append("bread") #inserting at end
print(my_cart)
my_cart.insert(0, "ketchup") #inserting at beginning
print(my_cart)
my_cart.pop(2) #removing bananas from position 2
print(my_cart)
removed_item = my_cart.pop() #removing last item
print(removed_item)
print(my_cart)
my_cart.append("rice") #adding rice at end
my_cart.append("butter")
print(my_cart)
my_cart.sort() #sorted
print(my_cart)
my_cart.reverse() #reverse
print(my_cart)
another_list = ["juice", "jam"]
my_cart = my_cart + another_list #concatenating with another list
print(my_cart)
my_cart = my_cart * 2 # duplicating the list twice
print(my_cart)
new_string = "tomato cucumber spinach"
converted_list = new_string.split() #converting string into list
print(converted_list)
