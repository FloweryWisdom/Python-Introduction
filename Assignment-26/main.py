#Assignment 26: Create a function that receives a list of names as its parameter
# and returns the same list but with all the names in uppercase.

def names_to_uppercase(names):
    for name in names:
        print(f"{name.upper()}")


#Array with names.
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Tina", "Ivy", "Jack",
    "Kate", "Leo", "Bob", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina", "Lincoln"
]

#Call the function with the list of names.
names_to_uppercase(names)