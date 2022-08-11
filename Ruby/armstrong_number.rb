class ArmstrongNumbers
    def self.include? (number)
      sum = number.digits.sum{|digit| digit ** number.digits.size }
      puts sum
      sum == number
    end
  end

  puts ArmstrongNumbers.include?(0)
  puts ArmstrongNumbers.include?(5)
  puts ArmstrongNumbers.include?(10)
  puts ArmstrongNumbers.include?(153)
  puts ArmstrongNumbers.include?(100)
  puts ArmstrongNumbers.include?(9474)
  puts ArmstrongNumbers.include?(9475)
  puts ArmstrongNumbers.include?(9_926_315)
  puts ArmstrongNumbers.include?(9_926_314)