#Create a program logic to print out every thrid element in an array using a while loop. 

def print_every_third_element(array):
    
    #Initialize the index counter to 0.
    index = 0

    #Use a while loop to iterate through every third element in the array. 
    while index <= len(array) - 1:
        #Print every third element in the array.
        print(array[index])

        #Increment the index by 3 to move to the next third element.
        index += 3


#Array with student names.
student_names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina"
]

#Change `student_names` to `array` for the function call.
array = student_names

#Call the function to print out every third element in the array.
print_every_third_element(array)


#NOTES: The `while` loop always has to have an intialized index counter and an incrementor. 