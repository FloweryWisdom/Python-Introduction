#Generate and print numbers from 0 to 255 with their hexadecimal representations
def integer_to_binary (n):
    if n == 0:
        return "00000000"
    binary_digits = []
    while n > 0: 
        binary_digits.append(str(n % 2))
        n = n // 2
    binary_str = ''.join(reversed(binary_digits))
    return binary_str.zfill(8) 
