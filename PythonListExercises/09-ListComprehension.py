# 9. List Comprehension
# Exercise: Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [a for a in numbers if a % 2 == 0]
for b in squares:
    print(b ** 2)