=begin
Write your code for the 'Resistor Color Trio' exercise in this file. Make the tests in
`resistor_color_trio_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/resistor-color-trio` directory.
=end

class ResistorColorTrio
    def initialize(colors)
      @first_color = colors[0]
      @second_color = colors[1]
      @third_color = colors[2]
    end
  
    def label
      color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
      if color.include?(@first_color) and color.include?(@second_color) and color.include?(@third_color)
        omhs = ((color.index(@first_color) * 10) + (color.index(@second_color))) * (10 ** color.index(@third_color))
        if omhs > 999
          omhs = omhs / 1000
          prefix = " kilo"
        else
          prefix = ' '
        end
        message = "Resistor value: " + omhs.to_s + prefix + "ohms"
        return message
      else
        raise ArgumentError
      end
  
  
    end
  end

resistance = ResistorColorTrio.new(["red", "black", "red"])
puts resistance.label