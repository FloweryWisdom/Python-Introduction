#Generate and print numbers from 0 to 255 with their binary and hexadecimal representations

def integer_to_binary(n): #name of function and parameter
    if n == 0: #Special case for 0
        return "00000000" #8-bit representation of 0
    binary_digits = [] #List to store the binary digits
    while n > 0: #Initialize an infinite loop that will run until n is 0
        binary_digits.append(str(n % 2)) #Append the remainder of n divided by 2 to the list of binary digits
        n = n // 2 #Use floor division to divide n by 2 and update n (result/quotient) to be the new value
    binary_str = ''.join(reversed(binary_digits)) #Join the list of 'binary_digits' in reverse order to 'binary_str' to form a binary string 
    #The zfill() method add zeros and the beginning of any string until it reaches the specified length. 
    return binary_str.zfill(8) # Note: if the value of the len parameter is less than the length of the string, no filling is done. 

def integer_to_hexadecimal(n):
    if n == 0: #Special case for 0
        return "0x0" #Hexadecimal representatrion of 0
    hex_digits = [] #List to store the hexadecimal digits
    #Create a string based lookup table with the 16 hexadecimal symbols to map remainders to their corresponding hex values.
    hex_map = "0123456789ABCDEF" 
    while n > 0: #Initialize an infinite loop that will run until n is 0
        hex_digits.append(hex_map[n % 16]) #Use the remainder to index into the string 'hex_map' and append the corresponding hex digit to the list of 'hex_digits'
        n = n // 16 #Use floor division to divide n by 16 and update n (result/quotient) to be the new value
    hex_str = ''.join(reversed(hex_digits)) #Join the list of 'hex_digits' in reverse order to 'hex_str' to form a hexadecimal string.
    return "0x" + hex_str #Return the hexadecimal string with the 'ox' prefix

#Generate and print numbers from 0 to 255 with their hexdacimal and binary repersentations
for i in range(256):
    integer = i #"integer" in base-10 (decimal) representation. 
    hexadecimal = integer_to_hexadecimal(i) #Convert the integer to hexadecimal
    binary = integer_to_binary(i) #Convert the integer to binary
    #Print the results
    print(f"Integer: {integer}, Hexadecimal: {hexadecimal}, Binary: {binary}") 


    #NOTES: PREFIX '0x' IN HEXADECIMAL REPRESENTATION

    # • Purpose: The '0x' prefix explicitly indicates that the number is in hexadecimal format. 
    #            Without the prefix, there could be ambiguity about the number's base, specially in contexts where multiple bases are used.
    
    # • Usage: This notation is commonly used in programming languages like C, C++, Python, and many others.  