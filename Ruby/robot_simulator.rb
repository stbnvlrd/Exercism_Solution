class Robot
    CARDINALS = [:north, :east, :south, :west]
    def initialize
      @bearing = 0
      @coordinates = [0,0]
    end
  
    def orient(bearing)
      if CARDINALS.include? bearing
        @bearing = CARDINALS.index(bearing)
        puts @bearing
      else
        raise ArgumentError
      end
    end
  
    def turn_right
      @bearing = @bearing + 1
      if @bearing == 4
        @bearing = 0
      end
      puts @bearing
    end
  
    def turn_left
      @bearing = @bearing - 1
      if @bearing == -1
        @bearing = 3
      end
      puts @bearing
    end
  
    def bearing
      return CARDINALS[@bearing]
    end

    def at(x, y)
      @coordinates = [x, y]
    end

    def coordinates
      return @coordinates
    end

  def advance
    if @bearing == 0
      @coordinates[1] = @coordinates[1] + 1
    elsif @bearing == 1
      @coordinates[0] = @coordinates[0] + 1
    elsif @bearing == 2
      @coordinates[1] = @coordinates[1] - 1
    elsif @bearing == 3
      @coordinates[0] = @coordinates[0] - 1
    end
  end

end

class Simulator
  def initialize
  end

  def instructions(instruction_text)
    instruction_text.chars.map do |instruction|
      case instruction
      when 'L'
        :turn_left
      when 'R' 
        :turn_right
       when 'A'
        :advance
      end
    end
  end

  def place(robot, x: 0, y: 0, direction: :north)
    robot.at(x, y) if x && y
    robot.orient(direction) if direction
  end

  def evaluate(robot, str)
    instructions(str).each { |inst|       robot.send(inst) }
  end
end

  robot = Robot.new
  robot.orient(:south)
  robot.turn_right
  puts robot.bearing

  robot.turn_left
  puts robot.bearing