# 9. List Comprehension
# Exercise: Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x for x in numbers if x % 2 == 0]
for y in squares:
    print(y ** 2)