def print_student_name(student_names, index):

    #Check if index is withing the valid range.
    if index < 0 or index >= len(student_names):
        print("Invalid index. Please enter a number between 0 and", len(student_names) -1)

    else: 
        #Print the student name at the specified index. 
        print("Student name at index", index, ":", student_names[index])

#Array with student names. 
student_names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Kate", "Leo", "Mia", "Nathan", "Olivia",
    "Peter", "Quinn", "Rachel", "Sam", "Tina"
]

index = int(input("Please enter the index of the student name you want to print: "))

print_student_name(student_names, index) 