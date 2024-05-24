#Assignment 30: Create a program that writes a new line in the file "test.txt" found within the "Assignment-29" folder.

#Specify the full file path
filepath = "/Users/gerardoflorencioarcesanchez/Kodemia/Python-Introduction/Assignment-29/test.txt"

#Open the file in write mode ("w") to write a new line
with open(filepath, "w") as file:
    #Write a new line
    file.write("Hello World")

#Print a success message
print(f"New line written succesfully in 'test.txt' at {filepath}")
