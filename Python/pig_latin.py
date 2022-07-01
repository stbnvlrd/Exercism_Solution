CONSONANTS = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
VOWELS = ["a","e","i","o","u","y"]
def translate(text):
    text_separated = text.split()
    word_con = ""
    final_list = []
    for words in text_separated:
        vowel_start = False
        for vowel in VOWELS:
            if words[0] == vowel:
                vowel_start = True
        
        if (words[0:2] != "xr" and words[0:2] != "yt" and vowel_start != True) or (words[0] == "y" and words[1] != "t"):
            if words[1:3] == "qu":
                word_con = words[3:len(words)] + words[0:3]
            elif words[0:2] == "qu":
                word_con = words[2:len(words)] + words[0:2]
            else:
                
                position = 0
                vowel_pos = 0
                while vowel_pos == 0:
                    for vowel in VOWELS:
                        if words[position] == vowel:
                            vowel_pos = position
                            print(vowel_pos)
                            break
                    position = position + 1
                word_con = words[vowel_pos:len(words)] + words[0:vowel_pos]
    
        
        else:
            word_con = words
        word_con = word_con + "ay"
        final_list.append(word_con)

    return " ".join(final_list)