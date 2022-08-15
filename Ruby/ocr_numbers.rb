
class OcrNumbers
    def self.convert_single_number(input)
      case input
      when [" _ ", "| |", "|_|", "   "].join("\n")
        return "0"
      when ["   ", "  |", "  |", "   "].join("\n")
        return "1"
      when [" _ ", " _|", "|_ ", "   "].join("\n")
        return "2"
      when [" _ ", " _|", " _|", "   "].join("\n")
        return "3"
      when ["   ", "|_|", "  |", "   "].join("\n")
        return "4"
      when [" _ ", "|_ ", " _|", "   "].join("\n")
        return "5"
      when [" _ ", "|_ ", "|_|", "   "].join("\n")
        return "6"
      when [" _ ", "  |", "  |", "   "].join("\n")
        return "7"
      when [" _ ", "|_|", "|_|", "   "].join("\n")
        return "8"
      when [" _ ", "|_|", " _|", "   "].join("\n")
        return "9"
      else
        ArgumentError
      end
    end
  
    def self.convert(input)
      puts input.length
      puts input[0].length
      if input.length == 15 and then
        return OcrNumbers.convert_single_number(input)
      else
        puts "have to separate letters"
      end
    end
  end


  input = ["   ",
    "  |",
    "  |",
    "   "].join("\n")
puts OcrNumbers.convert(input)

input = [" _ ",
    "| |",
    "|_|",
    "   "].join("\n")
puts OcrNumbers.convert(input)