#modifying a list while iterating
nums = [1, 2, 3]
			
for n in nums:
    print(n)
    nums.remove(n)
    print(nums)  # Output will show the list being modified during iteration

print(nums)  # Output will be [2] because 1 and 3 are removed during iteration
