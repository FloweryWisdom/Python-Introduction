#Assingment 20: Create a function that receives a name as a paramter and greets the user with the same name. 

def greet_user(name):
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Hope you are having an awesome one!")


#Call the function to greet the user.
greet_user("name")