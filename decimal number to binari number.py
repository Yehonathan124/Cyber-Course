def decimal_to_binary(decimal_num, num_bits=8):
    if decimal_num < 0:
       
        binary_num = bin((1 << num_bits) + decimal_num)[2:]
    else:
        binary_num = bin(decimal_num)[2:]

    return binary_num.zfill(num_bits)


decimal_number = int(input("Enter a num"))
result = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {result}")