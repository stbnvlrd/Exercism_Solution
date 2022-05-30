=begin
Write your code for the 'Darts' exercise in this file. Make the tests in
`darts_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/darts` directory.
=end
class Darts
    def initialize( x, y)
      @distance = Math.sqrt((x**2)+(y**2))
    end
    def score  
      if @distance > 10
        points = 0
      elsif @distance > 5
        points = 1
      elsif @distance > 1
        points = 5
      else
        points = 10
      end
    end
  end