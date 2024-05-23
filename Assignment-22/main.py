##Assignment 22: Create a function that receives a list as a parameter and returns the shortest name in the list.

def return_smallest_name(names):

    #Initialize the smallest length to 0.
    min_length = len(names[0])
    shortest_names = []

    #Iterate through the list of names.
    for name in names:
        name_length = len(name)

        #check for the longest names
        if name_length < min_length:
            min_length = name_length
            shortest_names = [name]
        elif name_length == min_length:
            shortest_names.append(name)
        
    print(f"Shortest name(s): {', '.join(shortest_names)}")
    return shortest_names


#Array with names. 
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina", "Lincoln"
]

#Call the function and print the result.
return_smallest_name(names)
