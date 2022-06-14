class ResistorColorDuo
  
    def self.value(colors)
      @first_color = colors[0]
      @second_color = colors[1]
      color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
      if color.include?(@first_color) and color.include?(@second_color)
        omhs = ((color.index(@first_color) * 10) + (color.index(@second_color)))
        
        message = "Resistor value: " + omhs.to_s + " ohms"
        return omhs
      else
        raise ArgumentError
      end
  
  
    end