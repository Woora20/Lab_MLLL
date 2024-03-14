def numsys(to):
    # Convert to binary and hexadecimal
    binary_representation = bin(to)
    hexadecimal_representation = hex(to)

    return binary_representation, hexadecimal_representation

if __name__ == "__main__":
    results = numsys (20)
    print('results = ', results)
    
    b, h = numsys (30)
    print('b = ', b)
    print('h = ', h)
