#Assignment 24: Create a function that receives a list as a parameter and evaluates a list of grades and returns the average.

def calculate_average_grade(grades):
    average = sum(grades) / len(grades)
    print(f"The average grade is: {average:.2f}")
    return average

#List of grades:
grades = [90, 85, 75, 100, 47, 88, 92, 75, 80, 100]


#Call the function to run the program.
calculate_average_grade(grades)