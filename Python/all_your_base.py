def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    else:    
        if all([ v == 0 for v in digits ]) :
            result = [0]
        else:
        
            if output_base < 2:
                raise ValueError("output base must be >= 2")
            else:
                sum = 0
                power = len(digits) - 1
                for x in range(len(digits)):
                    if digits[x] < input_base and digits[x] >= 0:
                        sum = sum + (digits[x] * (input_base ** (power - x) ))
                    else:
                        raise ValueError("all digits must satisfy 0 <= d < input base")
            # if output_base == 10:
            #     string_sum = str(sum)
            #     result = []
            #     for number in string_sum:
            #         result.append(int(number))
            # elif output_base == 2:
            result = []
            string_binary = ""
            while sum != 0:
                digit = sum % output_base
                # string_binary = str(digit) + string_binary
                result.insert(0, digit)
                sum = sum // output_base
                if  sum == 1:
                    result.insert(0, sum)
                    sum = 0
            # for number in string_binary:
            #     result.append(int(number))
    return result
