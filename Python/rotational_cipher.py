ALFABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALFABET_UP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
OTHER_CHAR = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '_', '-', '?', '!', '(', ')', '+', "'", '{', '}', '[', ']', ':']
def rotate(text, key):
    code_text = ""
    for char in text:
        for index in range(len(ALFABET)):
            if char == ALFABET[index]:
                new_index = index + key
                if new_index >25:
                    new_index = new_index - 26
                code_text = code_text + ALFABET[new_index]
            elif char == ALFABET_UP[index]:
                new_index = index + key
                if new_index >25:
                    new_index = new_index - 26
                code_text = code_text + ALFABET_UP[new_index]
            elif char == OTHER_CHAR[index]:
                code_text = code_text + char
    return code_text