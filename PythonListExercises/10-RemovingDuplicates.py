# 10. Removing Duplicates
# Exercise: Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
new_nums = []

for c in nums:
    if c not in new_nums:
        new_nums.append(c)

print("Unique elements:", new_nums)