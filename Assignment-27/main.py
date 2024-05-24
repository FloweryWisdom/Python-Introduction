#Assignment 27: Create a function that computes two parameters:
# 1. A list of numbers
#2. A number
#The function should return a list with all the numbers that are greater than the number (2nd parameter).

def numbers_greater_than(numbers, number):

    greater_numbers = []

    for num in numbers:
        if num > number:
            greater_numbers.append(num)
    
    print(f"Numbers greater than {number} are {greater_numbers}")
    return greater_numbers


#Array with numbers and number to be compared: 
numbers = [12, 34, 76, 23, 45, 67, 89, 90, 41, 78, 56]
number = 50

#Call the function.
numbers_greater_than(numbers, number)