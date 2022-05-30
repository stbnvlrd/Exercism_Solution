=begin
Write your code for the 'Difference Of Squares' exercise in this file. Make the tests in
`difference_of_squares_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/difference-of-squares` directory.
=end
class Squares
    def initialize(n_number)
      @n_number = n_number
    end
  
    def square_of_sum
      sum = 0
      (1..@n_number).each do |number|
        sum = sum + number
      end
      total = sum ** 2
      return total
    end
    def sum_of_squares
      sum = 0
      (1..@n_number).each do |number|
        square = number ** 2
        sum = sum + square
      end
      return sum
    end
    def difference
       self.square_of_sum - self.sum_of_squares
    end