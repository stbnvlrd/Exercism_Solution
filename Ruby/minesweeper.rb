=begin
Write your code for the 'Minesweeper' exercise in this file. Make the tests in
`minesweeper_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/minesweeper` directory.
=end

class ValueError < ArgumentError
end 

class Board
  def self.transform(minesweep)
    raise ValueError unless valid?(minesweep)
    minesweep.each_with_index do |line, x|
      line.split('').each_index do | y |
        if minesweep[x][y] == ' '
          sum = 0
          sum += (minesweep[x][y + 1] + minesweep[x][y - 1]).count('*')
          sum += minesweep[x + 1][y - 1..y + 1].count('*')
          sum += minesweep[x - 1][y - 1..y + 1].count('*')
          minesweep[x][y] = sum.to_s unless sum == 0
        end
      end
    end
    minesweep 
  end
  
  def self.valid?(minesweep)
    (minesweep[0]+minesweep[-1]).match(/[^+-]/) && minesweep.first == minesweep.last 
    minesweep[1..-2].all? { |part| part.match(/(^\|)([ *]+)(\|$)/) && 
    part.size == minesweep.first.size}
  end
end