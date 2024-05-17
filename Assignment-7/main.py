#Using the "while" loop to create the FizzBuzz logic.
def fizzbuzz():
    num = 1 #Initialize the loop variable.
    while num <= 100: #loop from 1 to 100.
        output = str(num) + ". " #Initialize the output with the number, period and space.
        if num % 3 == 0: #Check if the number is divisible by 3,
            output += "Fizz" #Append "Fizz" to the output. 
        if num % 5 == 0: #Check if the number is divisible by 5.
            output += "Buzz" #Append "Buzz" to the output. 
        print(output) #Print the result.
        num += 1 #Manual incrementation of the loop variable per each iteration since we are using the "while" loop. 
    

#Call the function to execute the FizzBuzz logic with a "while" loop. 
fizzbuzz()
