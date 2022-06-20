PLAIN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3']
CYPHER = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '1', '2', '3']

def encode(plain_text):
    ciphered_text = ""
    for letter in plain_text.casefold():
        for index in range(29):
            if letter == PLAIN[index]:
                ciphered_text = ciphered_text + CYPHER[index]
    new_ciphered_text = ""
    if len(ciphered_text) > 5:
        for index in range((len(ciphered_text)-1)//5):
            new_ciphered_text = new_ciphered_text + ciphered_text[(index*5):((index*5)+5)] + " " 
        for index in range((len(ciphered_text)-1)%5+1):
            new_ciphered_text = new_ciphered_text + ciphered_text[((len(ciphered_text)-1)//5)*5 + index]
            
    else:
        new_ciphered_text = ciphered_text
    return new_ciphered_text 

def decode(ciphered_text):
    plain_text = ""
    for letter in ciphered_text.casefold():
        for index in range(29):
            if letter == PLAIN[index]:
                plain_text = plain_text + CYPHER[index]
    return plain_text
