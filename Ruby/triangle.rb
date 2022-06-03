=begin
Write your code for the 'Triangle' exercise in this file. Make the tests in
`triangle_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/triangle` directory.
=end

class Triangle
    def initialize(distance)
      @sides = distance
      @longest = 0
      distance.each do |sides|
        if @longest < sides
          @longest = sides
        end
      end
    end
  
    def scalene?
      @sides[0] != @sides[1] and @sides[1] != @sides[2] and @sides[0] != @sides[2] and (@longest < (@sides.sum - @longest))
    end
  
    def isosceles?
     ( (@sides[0] == @sides[1]) or (@sides[0] == @sides[2]) or (@sides[2] == @sides[1])) and (@longest < (@sides.sum - @longest))
    end
  
    def equilateral?
      @sides[0] == @sides[1] and @sides[1] == @sides[2] and @sides[2] != 0
    end
  
      
  end