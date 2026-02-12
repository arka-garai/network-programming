# 4. Write a Python program to implement the Cyclic Redundancy
# Check (CRC) method.

def xor(a, b):
    """Perform XOR between two binary strings"""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def mod2div(dividend, divisor):
    """Perform Modulo-2 division"""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp


def encode_data(data, generator):
    """Encode data by appending CRC remainder"""
    l_gen = len(generator)
    appended_data = data + '0' * (l_gen - 1)
    remainder = mod2div(appended_data, generator)
    codeword = data + remainder
    return codeword


def crc_check(codeword, generator):
    """Check received codeword for errors"""
    remainder = mod2div(codeword, generator)
    if '1' in remainder:
        return False
    else:
        return True


# -------------------------------
# Main Program
# -------------------------------
data = input("Enter data (binary): ")
generator = input("Enter generator polynomial (binary): ")

# Sender Side
codeword = encode_data(data, generator)
print("Encoded Data (Codeword):", codeword)

# Receiver Side
received = input("Enter received data: ")

if crc_check(received, generator):
    print("No error detected in received data.")
else:
    print("Error detected in received data.")

# output
# Enter data (binary): 1001
# Enter generator polynomial (binary): 1011
# Encoded Data (Codeword): 1001110
# Enter received data: 1001110
# No error detected in received data.
