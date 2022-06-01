=begin
Write your code for the 'Raindrops' exercise in this file. Make the tests in
`raindrops_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/raindrops` directory.
=end

class Raindrops
    def self.convert(number)
      result = ''
      if number % 3 == 0
        result = result + 'Pling'
      end
      if number % 5 == 0
        result = result + 'Plang'
      end
      if number % 7 == 0
        result = result + 'Plong'
      end
      if result == ''
        result = number.to_s
      end
      return result
    end
  end

  puts Raindrops.convert(1)
  puts Raindrops.convert(8)
  puts Raindrops.convert(52)
