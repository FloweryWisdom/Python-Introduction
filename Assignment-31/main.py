#Create a program the contents of the file 'text.txt' in the 'Assignment-29' folder.

#Speicify the full file path
filepath = "c:/Users/srger/Kodemia/Python-Introduction/Assignment-29/test.txt"

#Open the file in read mode ("r") to read the contents
with open(filepath, "r") as file:
    #read the contents of the file
    content = file.read()

    #Print the contents of the file
    print(content)

