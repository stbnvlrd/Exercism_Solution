class Game
  class BowlingError < StandardError
  end

  def initialize()
    @rolls = []
    @score = 0
    @strike_count = 0
  end

  def roll(pin)
    raise BowlingError if pin < 0
    raise BowlingError if pin > 10
    @strike_count += 1 if pin == 10
    # raise BowlingError if @rolls.length > 1 and (@rolls.length + @strike_count)%2  != 0 and (@rolls[-1] + pin) > 10
      
    @rolls.append(pin)
  end

  def score
    count = 0
    for index in (0..@rolls.length-1) do
      count += 1
      if count <= 20 then
        @score += @rolls[index] 
        if  @rolls[index] == 10 then
          count += 1
          @score += @rolls[index + 1] 
          @score += @rolls[index + 2] 
        elsif count%2 != 0 and count <= 19 and(@rolls[index] + @rolls[index + 1]) == 10 then
          @score += @rolls[index + 2] 
        end
      end
    end
    return @score
  end
end
    
  
  # puts "Game 1"    
  # game = Game.new
  # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 7]
  # rolls.each { |pins| game.roll(pins) }
  # puts game.score

  # puts " "  
  # puts "Game 2"    
  # game = Game.new
  # rolls = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  # rolls.each { |pins| game.roll(pins) }
  # puts game.score

  # puts " "  
  # puts "Game 3"  
  # game = Game.new
  # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 3]
  # rolls.each { |pins| game.roll(pins) }
  # puts game.score
  
  # puts " "  
  # puts "Game 4"  
  # game = Game.new
  # rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10]
  # rolls.each { |pins| game.roll(pins) }
  # puts game.score

  puts " "  
  puts "Game 5"  
  game = Game.new
  rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 10]
  rolls.each { |pins| game.roll(pins) }
  puts game.score
  
  puts " "  
  puts "Game 6"  
  game = Game.new
  rolls = [5, 5, 10, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  rolls.each { |pins| game.roll(pins) }
  puts game.score