#Assignment 23: Create a function that receives a list as a parameter and returns a "truthy" value if the list contains
# repeated elements. Otherwise, return a "falsy" value. And also provide the repeated name(s). 

def check_repeated_elements(names):

    #Check for any repeated names in the list using sets
    unique_names = set()
    repeated_names = set()

    for name in names: 
        if name in unique_names:
            repeated_names.add(name)
        else:
            unique_names.add(name)
    
    if repeated_names:
        print("True. Repeated names:", ", ".join(repeated_names))
    else:
        print("False. No repeated names found.")

    return bool(repeated_names)


#Array with names. 
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Tina", "Ivy", "Jack",
    "Kate", "Leo", "Bob", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina", "Lincoln"
]

#Call the function with the list of names. 
check_repeated_elements(names)