# Assignment 29: Create a program that creates a file named "test.txt"

#Specify the full file path
filepath = "/Users/gerardoflorencioarcesanchez/Kodemia/Python-Introduction/Assignment-29/test.txt"


#Open the file in exclusive creation mode ("x"), this will create the file if it does not exist.
with open(filepath, "x") as file:
    #Do not write any content, just create the file
    pass

#Print a success message
print(f"File 'test.txt' created successfully at {filepath}")
