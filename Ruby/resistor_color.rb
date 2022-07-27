class ResistorColor
    COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
  
    
    def self.color_code(color)
      return COLORS.find_index(color)
    end
  end

  puts ResistorColor.color_code("black")
  
  puts ResistorColor.color_code("white")
  
  puts ResistorColor.color_code("orange")
  
  puts ResistorColor::COLORS