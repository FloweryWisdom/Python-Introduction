#Create a program that counts the number of elements of each data type in a given list. 


#Step 1: Create an array with elements of various data types.
mixed_array = [True, 42, 'hello', 3.14, False, 'world', 100, 2.718, '', 0, None, 1.0]


#Step 2: Initialize a dictionary to store the count of each data type. 
type_counts = {
    "bool": 0,
    "int": 0,
    "str": 0,
    "float": 0,
    "none": 0,
}

#Step 3: Iterate over the elements in the array.
for element in mixed_array:
    #Check the data type of each element and increment the corresponding count in the dictionary. 
    if isinstance(element, bool):
        type_counts["bool"] += 1
    elif isinstance(element, int):
        type_counts["int"] += 1
    elif isinstance(element, str):
        type_counts["str"] += 1
    elif isinstance(element, float):
        type_counts["float"] +=1
    elif element is None: 
        type_counts["none"] += 1


#Step 4: Print the count of each data type. 
print("Count of each data type in the array:")
for dtype, count in type_counts.items():
    print(f"{dtype}: {count}")