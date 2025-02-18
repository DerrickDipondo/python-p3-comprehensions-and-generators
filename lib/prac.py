squared_minus_one = list()

for n in range(1, 11):
    squared_minus_one.append((n ** 2) - 1)

print(squared_minus_one)

squared_minus_one = [(n ** 2) - 1 for n in range(1, 11)]

print(squared_minus_one)

"""

new_list = [optional_operation(item) for item in old_list if optional_condition == True]

"""

one_to_three = range(1,4)

# A list comprehesion uses square brackets
squared_lc = [n **2 for n in one_to_three]

# A generator expression uses parenthese
squared_ge = (n **2 for n in one_to_three)

# Looping through each shows identical values...
for n in squared_lc:
    print(n)

print("........................")

for n in squared_ge:
    print(n)


print(squared_lc)
print(squared_ge)