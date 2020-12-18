ignored = ["/", '"', ":", ";", ",",
           ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]


def build_string(s):
    new = ""
    for char in s:
        if char not in ignored:
            new += char.lower()
        elif char == " ":
            new += char

    return new


def word_count(s):
    word_table = {}
    s = build_string(s)

    words = s.split()

    for el in words:
        if el == "":
            continue
        if el in ignored:
            continue
        if el in word_table:
            word_table[el] += 1
        else:
            word_table[el] = 1

    return word_table


if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count(
    # 'This is a test of the emergency broadcast network. This is only a test.'))
