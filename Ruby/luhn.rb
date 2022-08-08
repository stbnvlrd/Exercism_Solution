class Luhn
    def self.valid?(number)
      sum = 0
      number = number.gsub(' ','')
      
      if number.length < 2 or number.gsub(/[^0-9]/, '') != number then
        return false
      end
      # puts number.length
      for digit in (1..number.length) do
      #   puts number[digit-1]
        if digit%2 == 0  and number.length%2 != 0 then
          digit_result = 2 * number[digit-1].to_i
        elsif digit%2 != 0  and number.length%2 == 0 then
          digit_result = 2 * number[digit-1].to_i
        else
          digit_result = number[digit-1].to_i
        end
        if digit_result >= 10 then
          digit_result = digit_result - 9
        end
        sum += digit_result
        # puts sum 
      end
      
      return sum%10 == 0
    end
  end
    

puts Luhn.valid?("059")
puts Luhn.valid?("055 444 286")
puts Luhn.valid?("055 444 285")
puts Luhn.valid?("0")
puts Luhn.valid?("055-444-285")
puts Luhn.valid?("0000 0")