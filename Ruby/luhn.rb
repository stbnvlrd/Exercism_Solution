class Luhn
  def self.valid?(number)
    sum = 0
    number = number.gsub(' ','')
    # puts number.length
    for digit in (1..number.length) do
    #   puts number[digit-1]
      if digit%2 == 0 then
        digit_result = 2 * number[digit-1].to_i
      else
        digit_result = number[digit-1].to_i
      end
      if digit_result >= 10 then
        digit_result = digit_result - 9
      end
      sum += digit_result
      puts sum 
    end
    
    return sum%10 == 0
  end
end

puts Luhn.valid?("059")