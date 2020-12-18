import random

ignored = ["/", ":", ";", ",",
           "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

end = [".", "?", "!"]

with open("applications/markov/input.txt") as f:
    words = f.read()


def build_string():
    new = ""
    for char in words:
        if char not in ignored:
            new += char
        elif char == " ":
            new += char

    return new.split()


words2 = build_string()


def markov():
    table = dict()
    for i in range(len(words2)):
        table[words2[i]] = []

    for i in range(len(words2)-1):
        table[words2[i]].append(words2[i+1])

    start = [word for word in table if word[0] ==
             '"' and word[1].isupper() or word[0].isupper()]

    print(random.choice(start), end=" ")
    for word in table:

        if len(table[word]) >= 1:
            print(random.choice(table[word]), end=" ")
        else:
            if (word[-1] in end) or ((word[-2] in end) and (word[-1] == '"')):

                print(word, end=" ")
                break


markov()
