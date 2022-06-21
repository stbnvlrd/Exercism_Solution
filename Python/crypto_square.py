def cipher_text(plain_text):
    if plain_text == "":
        message = ""
    else:
        no_space = plain_text.replace(" ", "").lower()
        no_space = no_space.replace("@", "")
        no_space = no_space.replace("!", "")
        no_space = no_space.replace("%", "")
        no_space = no_space.replace(",", "")
        no_space = no_space.replace(".", "")
        minor_difference = len(no_space)
        r = 0
        c = 0
        if len(no_space) == 1:
            r = 1
            c = 1 
        else:
            for index in range(round(len(no_space))):
                difference = (index)*(index) - len(no_space)
                if difference < minor_difference and difference >= 0:
                    minor_difference = difference
                    r = index
                    c = index
                difference = (index)*(index + 1) - len(no_space)
                if difference < minor_difference and difference >= 0:
                    minor_difference = difference
                    r = index
                    c = index + 1
            while r*c > len(no_space):
                no_space = no_space + " "
        rows = [""]*r
        for index in range(len(rows)):
            rows[index] = no_space[c*index:c*(index+1)]
        message = ""
        for column in range(len(rows[0])):
            for row in rows:
                message = message + row[column]
            message = message + " "
        message = message[0:-1]
    return message
