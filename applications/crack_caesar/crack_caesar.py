from time import time 

start = time()
f = open("applications/crack_caesar/ciphertext.txt", "r")

data = f.read()


decode_table = {}

cipher_key = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
]


def populate_table():
    for char in data:
        if char in decode_table and char in cipher_key:
            decode_table[char] += 1
        elif char not in decode_table and char in cipher_key:
            decode_table[char] = 1
    return decode_table


populate_table()

# Sorting our dict values from lowest to highest

decode_table = {k: v for k, v in sorted(
    decode_table.items(), key=lambda item: item[1])}

print(decode_table)

value_list = list(decode_table.keys())
value_list.reverse()
print(value_list)

for i in range(0, len(value_list)):

    decode_table[value_list[i]] = cipher_key[i]

# function that prints the decoded data


def print_new():
    new = ""
    for char in data:
        if char == " ":
            new += " "
        if char in decode_table:
            new += decode_table[char]

    print(new)


print_new()
print(time() -start)

#

# loop over all encrypted chars
# save the instances of each char into a dict key value pair
