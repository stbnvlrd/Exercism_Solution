class Lasagna
    EXPECTED_MINUTES_IN_OVEN = 40
    TIME_PER_LAYER = 2
    def remaining_minutes_in_oven(actual_minutes_in_oven)
      remiander = EXPECTED_MINUTES_IN_OVEN - actual_minutes_in_oven
      return remiander
    end
  
    def preparation_time_in_minutes(layers)
      preparation_time = layers * TIME_PER_LAYER
      return preparation_time
    end
  
    def total_time_in_minutes(number_of_layers:, actual_minutes_in_oven:)
      prep_time = preparation_time_in_minutes(number_of_layers)
      total_time = prep_time + actual_minutes_in_oven
      return total_time
    end
  end
  