#Assignment 28: Create a function that computes two parameters:
# 1. A list of names
# 2. A number
# The function should return a list with all the names whose length is greater than the number (2nd parameter).

def names_greater_than(names, number):
    
    greater_names = []

    for name in names:
        if len(name) > number:
            greater_names.append(name)
    
    return print(f"Names with length greater than {number} are {greater_names}")


#Array with names and number to be compared:
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Tina", "Ivy", "Jack",
    "Kate", "Leo", "Bob", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina", "Lincoln"
]

number = 5

#Call the function.
names_greater_than(names, number)