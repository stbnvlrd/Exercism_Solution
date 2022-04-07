day_list = ["first"
,"second"
,"third"
,"fourth"
,"fifth"
,"sixth"
,"seventh"
,"eighth"
,"ninth"
,"tenth"
,"eleventh"
,"twelfth"]

frase_list = ["a Partridge in a Pear Tree."
, "two Turtle Doves, and "
, "three French Hens, "
, "four Calling Birds, "
, "five Gold Rings, "
, "six Geese-a-Laying, "
, "seven Swans-a-Swimming, "
, "eight Maids-a-Milking, "
, "nine Ladies Dancing, "
, "ten Lords-a-Leaping, "
, "eleven Pipers Piping, "
, "twelve Drummers Drumming, "]


def recite(start_verse, end_verse):
    song = []
    
    for x in range(start_verse - 1, end_verse):
        verse = ""
        for y in range(x + 1):
            
            verse = frase_list[y] + verse
            # print(verse + "\n")
        song.append('On the ' + day_list[x] + ' day of Christmas my true love gave to me: ' + verse)
    print(song)
    return song

recite(3,3)