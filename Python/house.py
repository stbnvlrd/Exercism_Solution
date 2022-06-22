FIRST_LINE = ["This is the house that Jack built", "This is the malt", "This is the rat", "This is the cat", "This is the dog", "This is the cow with the crumpled horn", "This is the maiden all forlorn", "This is the man all tattered and torn", "This is the priest all shaven and shorn", "This is the rooster that crowed in the morn", "This is the farmer sowing his corn", "This is the horse and the hound and the horn"]

NOT_FIRST_LINE = ["that lay in the house that Jack built", "that ate the malt", "that killed the rat", "that worried the cat", "that tossed the dog", "that milked the cow with the crumpled horn", "that kissed the maiden all forlorn", "that married the man all tattered and torn", "that woke the priest all shaven and shorn", "that kept the rooster that crowed in the morn", "that belonged to the farmer sowing his corn"]

def recite(start_verse, end_verse):
    lenght = end_verse - start_verse + 1
    poem = []
    for index in range(start_verse-1, end_verse):
        i = index -1
        line = ""
        while i >= 0: 
            line = line + " " + NOT_FIRST_LINE[i]
            i = i - 1
        line = FIRST_LINE[index] + line + "."
        poem.append(line)
    return poem