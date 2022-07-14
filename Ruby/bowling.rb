class Game
  class BowlingError < StandardError
  end

  def initialize()
    @final_score = 0
    @last_roll = 0
    @roll = 0
    @last_last_roll = 0
    @roll_count = 0  
  end

  def roll(pin)
    raise BowlingError if pin < 0
    raise BowlingError if pin > 10
    
    @last_last_roll = @last_roll
    @last_roll = @roll
    @roll = pin
    if pin == 10 then
      @roll_count += 2
    else
      @roll_count += 1  
    end

    # raise BowlingError if (@roll_count % 2 == 0 and (pin + @last_roll) > 10 and @last_roll != 10 and @last_last_roll != 10)
      
    print "Turn "
    puts @roll_count
    if @roll_count <= 20 then
      @final_score = @final_score + pin
      puts @final_score
    end
    if (@roll_count % 2 != 0 or (@roll_count % 2 == 0 and pin == 10)) and (@last_last_roll + @last_roll) == 10 and @last_roll != 10 and @last_roll != 0 then
      @final_score = @final_score + pin
      print "spare "
      puts @final_score
    end
    if @last_last_roll == 10 then 
      @final_score = @final_score + pin
      print "strike 2 "
      puts @final_score
    end
    if @last_roll == 10 and @roll_count < 23 then
      @final_score = @final_score + pin
      print "strike 1 "
      puts @final_score
    end
  end


  def score
    raise BowlingError if @roll_count == 0
    @final_score
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