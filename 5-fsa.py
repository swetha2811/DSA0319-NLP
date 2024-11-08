def equal_number_of_ones_and_zeros(string):
    count_ones = 0
    count_zeros = 0
    
    for char in string:
        if char == '1':
            count_ones += 1
        elif char == '0':
            count_zeros += 1
        else:
            return False  
    
    return count_ones == count_zeros

# Test the function
strings_to_test = ["1010", "1100", "111000", "00001111", "101010101"]
for string in strings_to_test:
    if equal_number_of_ones_and_zeros(string):
        print(f"{string}: Equal number of '1's and '0's")
    else:
        print(f"{string}: Not equal number of '1's and '0's")
