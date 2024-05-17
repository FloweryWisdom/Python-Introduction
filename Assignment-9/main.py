#Use the "for" loop to create the FizzBuzz logic. 
def fizzbuzz():
    for num in range(1, 101): #Loop from 1 to 100.
        output = str(num) + ". "
        if num % 3 == 0:
            output += "Fizz"
        if num % 5 == 0:
            output += "Buzz"
        print(output) #Print the result. 

#Call the function to execute the FizzBuzz logic. 
fizzbuzz()
