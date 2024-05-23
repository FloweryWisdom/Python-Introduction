#Initialize an empty list to store names. 
names = []

#Step 1 and 2: Prompt the user to provide names and ask if they want to continue.
while True:
    name = input("Enter a name: ").strip() #Remove any leading or trailing whitespaces. 

    #Check if the name contains any digits.
    if any(char.isdigit() for char in name):
        print("Invalid input. Names cannot contain numbers. Please enter a valid name.")
        continue #Continue to prompt for a valid name.  

    #Check if the name is empty.
    if not name:
        print("Name cannot be empty. Please enter a valid name.")
        continue #continue to prompt for a valid name.
    
    names.append(name)#Add the name to the list of names.

    #Ask the user if they want to continue with validation. 
    while True:
        continue_adding = input("Do you want to add another name? (yes/no): ").strip().lower()
        if continue_adding in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    if continue_adding == 'no':
        break

#Step 3. Function to print the index number of the specified name.
def print_index_number(name, names):
    while True:
        #Check if name is provided by the user.
        if not name:
            print("Name cannot be empty.")
            name = input("Please enter a valid name: ").strip()
            continue
        
        #Check if the name contains any digits.
        if any(char.isdigit() for char in name):
            print("Invalid input. Names cannot contain numbers. Please enter a valid name.")
            name = input("Please enter a valid name: ").strip()
            continue

        #Check if name is within the list of names provided by the user.
        if name in names:
            print(f"{name} is at index {names.index(name)} in the list.")
            break

        else: 
            print("Name not found in the list.")
            name = input("Please enter a valid name: ").strip()
            continue

#Step 4: Ask the user to provide the name of the user's index they would like to see.
name_to_check = input("Please enter the name of the user's index you would like to see: ")

print_index_number(name_to_check, names)
