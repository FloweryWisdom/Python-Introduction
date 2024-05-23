#Initialize an empty list to store names. 
names = []

#Step 1 and 2: Prompt the user to provide names and ask if they want to continue.
while True:
    name = input("Enter a name: ")
    names.append(name)

    #Ask the user if they want to continue with validation. 
    while True:
        continue_adding = input("Do you want to add another name? (yes/no): ").strip().lower()
        if continue_adding in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    if continue_adding == 'no':
        break

#Step 3a: Print the number of names provided by the user. 
print(f"\nNumber of names provided: {len(names)}")

#Step 3b: Check for any repeated names in the list using sets for efficiency. 
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

#Step 3c: Initialize variables to track the maximum and minimum lenghths and the corresponding names. 
max_length = 0
min_length = len(names[0])
longest_names = []
shortest_names = []

#Iterrate through the list of names.
for name in names: 
    name_length = len(name)

    #Check for the longest names: 
    if name_length > max_length: 
        max_length = name_length 
        longest_names= [name]
    elif name_length == max_length:
        longest_names.append(name)
    
    #Check for the shortest names:
    if name_length < min_length:
        min_length = name_length
        shortest_names = [name]
    elif name_length == min_length:
        shortest_names.append(name)

#Step 3d: Print the results.

#Print the longest names: 
print(f"Longest name(s): {', '.join(longest_names)}")

#Print the shortest names:
print(f"Shortest name(s): {', '.join(shortest_names)}")
