my_cart = ["apples","bananas","milk"]
print(my_cart)
my_cart.append("bread") #inserting at end
print(my_cart)
my_cart.insert(0, "ketchup") #inserting at beginning
print(my_cart)
# my_cart.pop(2) #removing bananas from position 2
my_cart.remove("bananas") #removing bananas by value, it removes the first occurrence of the value
print(my_cart)
removed_item = my_cart.pop() #removing last item
print(removed_item)
print(my_cart)
# my_cart.append("rice") #adding rice at end
# my_cart.append("butter")
my_cart.extend(["rice", "butter"]) #adding multiple items at end
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

#adding two lists
list1 = [1,2]
list2 = [3,4]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3,4]

#string to list
str = "apple"
print(list(str))  # Output: ['a', 'p', 'p', 'l', 'e']

string_list = "apple banana orange"
print(list(string_list))  # Output: ['a', 'p', 'p', 'l', 'e', ' ', 'b', 'a', 'n', 'a', 'n', 'a', ' ', 'o', 'r', 'a', 'n', 'g', 'e']
