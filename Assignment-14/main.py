#Create a program that provides the average grade of students in a class. 


def calculate_average_grade():
    #Step 1: Prompt the user to provide the number of students in the class.
    try:
        num_students = int(input("Enter the number of students in the class: "))

        #Check for valid user input. 
        if num_students <= 0:
            print("The number of students must be a positive integer.")
            return
    except ValueError: 
        print("Invalid input. Please enter a valid integer.")
        return
    
    #Step 2: Create an empty list to store the grades.
    grades = []


    #Step 3: Collect each grade from the user.
    for i in range(0, num_students):
        while True:
            try:
                grade = float(input(f"Enter the grade for student {i + 1}: "))

                #Check for valid grade input.
                if grade < 0 or grade > 100:
                    print("Invalid grade. Please enter a number between 0 and 100.")
                else: 
                    grades.append(grade)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    #Step 4: Calulate the sum of all the grades.
    total_sum = sum(grades)

    #Step 5: Calculate the average grade.
    average = total_sum / num_students

    #Print the result. 
    print(f"The average grade of the class is: {average:.2f}")


#Call the function to run the program.
calculate_average_grade()