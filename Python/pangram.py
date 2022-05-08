ALFABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def is_pangram(sentence):
    letters_used = []
    for letter in range(26):
        for char in sentence.casefold():
            # print(ALFABET[letter])
            if char == ALFABET[letter]:
                letters_used.append(ALFABET[letter])
                print(ALFABET[letter])
                print("done")
                break
    if letters_used == ALFABET:
        result = True
    else:
        result = False
    return result

x = is_pangram("the quick brown fox jumps over the lazy dog")
print(x)