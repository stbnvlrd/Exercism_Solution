CONSONANTS = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
VOWELS = ["a","e","i","o","u","y"]
def translate(text):
    
    vowel_start = False
    for vowel in VOWELS:
        if text[0] == vowel:
            vowel_start = True
    
    if (text[0:2] != "xr" and text[0:2] != "yt" and vowel_start != True) or (text[0] == "y" and text[1] != "t"):
        if text[1:3] == "qu":
            text = text[3:len(text)] + text[0:3]
        elif text[0:2] == "qu":
            text = text[2:len(text)] + text[0:2]
        else:
            
            position = 0
            vowel_pos = 0
            while vowel_pos == 0:
                for vowel in VOWELS:
                    if text[position] == vowel:
                        vowel_pos = position
                        print(vowel_pos)
                        break
                position = position + 1
            text = text[vowel_pos:len(text)] + text[0:vowel_pos]

    
            
    text = text + "ay"    
    return text