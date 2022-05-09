class PhoneNumber:
    def __init__(self, number):
        number = number.replace(" ", "")
        number = number.replace("-", "")
        number = number.replace(".", "")
        number = number.replace("(", "")
        number = number.replace(")", "")
        number = number.replace("+", "")

        if len(number) == 11 and number[0] == "1":
            number = number[1:11]
        if len(number) == 10:
            self.number = number
            self.area_code = number[0:3]

            if not number.isdigit():
                if any(c.isalpha() for c in number):
                    raise ValueError("letters not permitted")
                else:
                    raise ValueError("punctuations not permitted")
            elif number[0] == "1":
                raise ValueError("area code cannot start with one")
            elif number[0] == "0":
                raise ValueError("area code cannot start with zero")
            elif number[3] == "0":
                raise ValueError("exchange code cannot start with zero")
            elif number[3] == "1":
                raise ValueError("exchange code cannot start with one")
            
        elif len(number) < 10:
            raise ValueError("incorrect number of digits")
        elif len(number) > 11:
            raise ValueError("more than 11 digits")
        elif len(number) == 11 and number[0] != "1":    
            raise ValueError("11 digits must start with 1")
        pass

    def pretty(self):
        return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:10]

