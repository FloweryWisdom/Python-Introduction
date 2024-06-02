def multiplication_table(number):
    #iteratre from 1 to 12.
    for i in range(1, 17):
        #Calculate the product of the current number and loop index. 
        result = number * i
        #Print the result in the format "number x i = result"
        print(f"{number} x {i} = {result}")

#Get the number from the user. 
number = int(input("Please enter a number to generate its multiplication table: "))


#Call the function to gnerrate the multiplcation table. 
multiplication_table(number)