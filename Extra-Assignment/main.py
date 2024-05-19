#Create a program to generate a list of the Fibonnaci numbers up to a specified number in the sequence.

#Import math module since we will be using square roots.
import math


#Define the Golden Ratio and its counterpart. 
def fibonacci_binet_list():
    
    #Prompt the user to enter the number of Fibonacci numbers to generate. 
    count = int(input("Please enter the number of Fibonacci numbers to generate: "))


    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2

    fibonacci_list = []

    #Calculate the Fibonacci numbers using the Binet formula.
    for n in range(0, count): 
        fibonacci_number = (phi ** n - psi ** n) / math.sqrt(5) 
        fibonacci_list.append(round(fibonacci_number))
    
    for num in fibonacci_list: 
        print(num)

#Call the function to generate the Fibonacci numbers. 
fibonacci_binet_list()
