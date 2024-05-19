#Program logic to print out all elements in an array next to their index number up to the number specified by the user.

def print_elements_up_to(array, max_index):

    #Check if the max_index is within the valid range.
    if max_index < 0 or max_index >= len(array):
        print(f"Invalid index. Please enter a number between 0 and {len(array) -1}")
        return
    

    #Use a loop to iterate through the array up to the specified index.
    for i in range(0, max_index +1):
        #Print the index and the element at that index.
        print(i, array[i])


#Array with student names. 
student_names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina"
]

#Change `student_names` to `array` for the function call.
array = student_names


#Step 1: Prompt the user to enter the index up to which they want to print the elements.

try: 
    max_index = int(input(f"Enter the index up to which you want to print the elements (0 - {len(array) - 1})"))

    #Step 2: Call the function to print out the elements up to the specified index. 
    print_elements_up_to(array, max_index)
except ValueError: 
    print("Invalid input. Please enter a valid intger.")