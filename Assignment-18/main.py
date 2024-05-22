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

#Step 3c: Find the longest name in the list.
longest_name = max(names, key=len)
print(f"Longest name: {longest_name}")

#Step 3d: Find the shortest name in the list.
shortest_name = min(names, key=len)
print(f"Shortest name: {shortest_name}")
