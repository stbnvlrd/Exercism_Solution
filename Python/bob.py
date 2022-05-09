def response(hey_bob):
    if bool(hey_bob):
        while hey_bob[-1] == " " and len(hey_bob) > 1:
            hey_bob = hey_bob[:-1]
    else:
        hey_bob = " "
    answer = ''
    if hey_bob.isupper() and "?" in hey_bob:
        answer = "Calm down, I know what I'm doing!"
    elif hey_bob.isupper() and "?" not in hey_bob:
        answer = 'Whoa, chill out!'
    elif hey_bob[-1] == "?" :
        answer = 'Sure.'
    elif hey_bob.isspace():
        answer = "Fine. Be that way!"
    else:
        answer = 'Whatever.'
    return answer
