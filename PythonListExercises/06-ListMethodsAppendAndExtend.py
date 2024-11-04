# 6.List Methods: Append and Extend
# Exercise: Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list.

shopping_cart = []

shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")

extended_shopping_cart = ["butter", "cheese"]

shopping_cart.extend(extended_shopping_cart)

print(shopping_cart)