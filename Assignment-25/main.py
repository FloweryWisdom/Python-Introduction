#Assignment 25: Create a function that receives a list of names as its parameter and returns the 
# a list of repeated values in the list.

def find_repeated_names(names):
    unique_names = set()
    repeated_names = set()
    for name in names: 
        if name in unique_names:
            repeated_names.add(name)
        else:
            unique_names.add(name)
    if repeated_names:
        print("Repeated names:", ", ".join(repeated_names))
    else:
        print("No repeated names found.")
    
    return repeated_names


#Array with names.
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Tina", "Ivy", "Jack",
    "Kate", "Leo", "Bob", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina", "Lincoln"
]

#Call the function with the list of names.
find_repeated_names(names)