nums = {1, 2, 3, 2}
nums.add(4)  # duplicates are ignored
print(nums)  # {1, 2, 3, 4}
branch_a_products = {"bread", "milk","butter","jam"}
print(branch_a_products)
brnach_b_products = {"bread","cheese","butter","ketchup"}
print(brnach_b_products)
print(branch_a_products | brnach_b_products) #printing union 
print(branch_a_products & brnach_b_products) #intersection 
print(branch_a_products - brnach_b_products) #difference, products that are in branch_a_products but not in branch_b_products
print('ketchup' in branch_a_products) #Check whether "ketchup" is available in branch_a_products 
#frozenset
frozenset_to_print = frozenset(["milk","bread","ketchup"])
print(frozenset_to_print)