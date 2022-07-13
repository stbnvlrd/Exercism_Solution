class Game
    def initialize()
      @final_score = 0
      @last_roll = 0
      @roll = 0
      @last_last_roll = 0
      @roll_count = 0  
    end
  
    def roll(pin)
      @last_last_roll = @last_roll
      @last_roll = @roll
      @roll = pin
      @roll_count += 1  
      @final_score = @final_score + pin
      if @roll_count % 2 != 0 and (@last_last_roll + @last_roll) == 10 then
        @final_score = @final_score + pin
      elsif @last_last_roll == 10 then 
        @final_score = @final_score + pin
      elsif @last_roll == 10 then
        @final_score = @final_score + pin
      end
    end
  
  
    def score
      @final_score
    end
  end
      
      