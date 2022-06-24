def reverse(text):
    reversed_text = ""
    for index in text:
        reversed_text = index + reversed_text
    return reversed_text
