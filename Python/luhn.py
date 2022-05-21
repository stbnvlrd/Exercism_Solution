class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        print (self.card_num)
        pass
        

    def valid(self):
        validation = True
        card_number = list(self.card_num)

        if len(self.card_num) > 1 and self.card_num.isdigit():
            print(self.card_num.isdigit())
            i = 2
            sum = 0
            while i < len(card_number)+1:
                double = int(card_number[-i])*2
                print("The number is " + card_number[-i] + " and the double is " +  str(double))
                if double > 9:
                    double = double - 9
                    
                card_number[-i] = str(double)
                i += 2

            print (card_number)
            for item in card_number:
                sum = sum + int(item)
            print(sum)

            if not sum % 10 == 0:
                validation = False
            
        else:
            validation = False
            
        return validation
