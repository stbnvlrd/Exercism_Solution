def abbreviate(words):
    abbreviation = ''
    words = words.title()
    words = words.replace(" - ", " ")
    words = words.replace("-", " ")
    words = words.replace(" _", " ")
    words = words.replace("_ ", " ")
    list_words = words.split(" ")
    for i in list_words:
        abbreviation = abbreviation + i[0]
    return abbreviation
