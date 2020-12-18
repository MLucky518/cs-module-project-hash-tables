ignored = ["/", '"', ":", ";", ",",
           ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "!", "?"]


def build_string(s):
    new = ""
    for char in s:
        if char not in ignored:
            new += char.lower()
        elif char == " ":
            new += char

    return new


def histo():
    f = open("applications/histo/robin.txt", "r")
    data = f.read()

    new = ""
    for char in data:
        if char not in ignored:
            new += char.lower()
        elif char == " ":
            new += char

    d = new.split()

    table = dict()

    longest_word = ""

    for el in d:
        if len(el) > len(longest_word):
            longest_word = el
        if el in table:
            table[el] += 1
        else:
            table[el] = 1
    table = {k: v for k, v in sorted(
        table.items(), reverse=True, key=lambda item: item[1])}

    for key in table:
        if len(key) > len(longest_word):
            longest_word = key

        remainder = 17 - len(key)
        spacing = " " * remainder
        num = "#" * table[key]
        print(f"{key}{spacing}{num}")


histo()
