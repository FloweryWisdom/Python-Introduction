#Evaluate data type being received from the user.
def get_valid_input(prompt, data_type):
    while True:
        user_input = input(prompt)
        try:
            user_input = data_type(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Function to compute the perimeter of the regular polygon.
def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

def run_perimeter_calculator():
    print("Welcome to the Perimeter Calculator!")


    num_sides = get_valid_input("Please enter the number of sides: ", int)
    while num_sides < 3: #A polygon must have at least 3 sides. 
        print("A polygon must have at least 3 sides")
        num_sides = get_valid_input("Please enter the number of sides: ", int)
    

    side_length = get_valid_input("Please enter the length of one side: ", float)
    while side_length <= 0: #A polygon must have a positive side length.
        print("A polygon must have a positive side length.")
        side_length = get_valid_input("Please enter the length of one side: ", float)

    perimeter = calculate_perimeter(num_sides, side_length)
    print(f"The perimeter of the polygon is {perimeter} units.")


#Call the function to run the program.
run_perimeter_calculator()
