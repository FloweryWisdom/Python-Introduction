#Write a Python program to print the firs N numbers in the Fibonacci series.
def fibonnaci_series():
    #Step 1: Request the number of terms from the user.
    n = int(input("Please enter any number: "))

    #Step 2: Initialize the first two fibonacci numbers. 
    a, b = 0, 1

    #Step 3: Check the input value.
    if n == 1: 
        print(0)

    elif n <= 0:
        print("Please enter a positive integer.")
    else:
        print(a)
        print(b)
    
        #Step 5: Use a "For" loop to generate the Fibonacci series.
        for i in range(2, n):

            #Calculate the next Fibonacci number.
            next_fib = a + b

            #Update a and b to the next numbers in the sequence. 
            a = b
            b = next_fib

            #Step 6: Print the result. 
            print(f"{next_fib}")


#Call the function to run the program. 
fibonnaci_series()


