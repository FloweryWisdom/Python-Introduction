#Assignment 21: Create a function that receives a list as a parameter and returns the largest name in the list.

def return_largest_name(names):

    #Initialize the maximum length to 0.
    max_length = 0
    longest_names = []

    #Iterate through the list of names.
    for name in names:
        name_length = len(name)

        #check for the longest names
        if name_length > max_length:
            max_length = name_length
            longest_names = [name]
        elif name_length == max_length:
            longest_names.append(name)
        
    print(f"Longest name(s): {', '.join(longest_names)}")
    return longest_names


#Array with names. 
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina", "Lincoln"
]

#Call the function and print the result.
return_largest_name(names)


