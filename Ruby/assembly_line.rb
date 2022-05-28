class AssemblyLine
  def initialize(speed)
    @speed = speed
    if speed <= 4
      success_rate = 1
    elsif speed <= 8
      success_rate = 0.9
    elsif speed == 9
      success_rate = 0.8
    elsif speed == 10
      success_rate = 0.77
    end
    @production_rate = success_rate*@speed*221
  end

  def production_rate_per_hour
    
    return @production_rate
  end

  def working_items_per_minute
    return (@production_rate.to_i)/60
  end
end
