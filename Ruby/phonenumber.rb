class PhoneNumber
  def self.clean(number)
    number.gsub!("(", "")
    number.gsub!(")", "")
    number.gsub!(" ", "")
    number.gsub!("-", "")
    number.gsub!(".", "")
    number.gsub!("+", "")
    return number
  end
end

puts PhoneNumber.clean("(223) 456-7890")
puts PhoneNumber.clean("223.456.7890")
puts PhoneNumber.clean("223 456   7890   ")