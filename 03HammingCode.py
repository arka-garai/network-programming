# 3) Write a Python program to implement the Hamming code.
def hamming_generator(data):
    data = list(map(int, data))
    k = len(data)

    # number of parity bits
    r = 0
    while True:
        if (k + r) <= (2 ** r - 1):
            break
        r += 1

    n = k + r
    hamming = []
    j = 0

    # Insert data bits and parity placeholders
    for i in range(1, n + 1):
        if i & (i - 1) == 0:
            hamming.append(0)
        else:
            hamming.append(data[j])
            j += 1

    # parity bits calculation
    for i in range(r):
        p = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & p:
                parity += hamming[j - 1]
        hamming[p - 1] = parity % 2

    # Reverse
    hamming.reverse()
    return hamming


def hamming_checker(code):
    code = list(map(int, code))

    code.reverse()
    n = len(code)

    # number of parity bits
    r = 0
    while (2 ** r) <= n:
        r += 1

    syndrome = []

    # syndrome bits calculation
    for i in range(r):
        p = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & p:
                parity += code[j - 1]
        syndrome.append(parity % 2)

    syndrome.reverse()

    error_pos = 0
    for bit in syndrome:
        error_pos = error_pos * 2 + bit

    # Error detection and correction
    if error_pos == 0:
        print("No error detected")
    else:
        print("Error detected at position:", error_pos)
        code[error_pos - 1] ^= 1

    code.reverse()
    return code


# main
data = input("Enter binary data: ")
hamming_code = hamming_generator(data)
print("Generated Hamming Code :", hamming_code)

received = input("Enter received Hamming code: ")
corrected_code = hamming_checker(received)
print("Corrected Hamming Code :", corrected_code)


# output:
# Enter binary data: 10011001
# Generated Hamming Code : [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
# Enter received Hamming code: 101100100101
# Error detected at position: 11
# Corrected Hamming Code : [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1]
