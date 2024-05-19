#Create a program logic to print out all the elements in an array next to their index number. 

def print_elements_with_index(array):
    for i in range(0, len(array)):
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

#call the function to print out all the elements in the array next to their index number.
print_elements_with_index(array)