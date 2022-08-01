class PhoneNumber
  def self.clean(number)
    number.gsub!("(", "")
    number.gsub!(")", "")
    number.gsub!(" ", "")
    number.gsub!("-", "")
    number.gsub!(".", "")
    number.gsub!("+", "")
    if number[0] == "1" and number.length == 11
        number = number[1..-1]
    end
    if number.length == 10
      if number[0] == "0" or number[0] == "1" or number[3] == "0" or number[3] == "1"
        return nil
      else
        return number 
      end
    else
        return nil
    end
  end
end

puts PhoneNumber.clean("(223) 456-7890")
puts PhoneNumber.clean("223.456.7890")
puts PhoneNumber.clean("223 456   7890   ")
puts PhoneNumber.clean("123456789")
puts PhoneNumber.clean("22234567890")
puts PhoneNumber.clean("123-abc-7890")
puts PhoneNumber.clean("123-@:!-7890")
puts PhoneNumber.clean("+1 (223) 456-7890")
puts PhoneNumber.clean("1 (223) 056-7890")