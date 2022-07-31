class Diamond
    @letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def self.make_diamond(final_letter)
      space = 1

      lines = []
      length = @letters.index(final_letter) + 1
      puts "length: " + length.to_s
      text = ""
      for letter in ('A'..final_letter) do
        if letter == 'A' then
          indent_length = length - 1
          text = " "*(length - 1) + letter + " "*(length - 1)
        else
          indent_length -= 1
          text = " "*indent_length + letter + " "*space + letter + ''*indent_length
          space += 2 
        end
        lines.append(text)
        # puts text 
      end
      indent_length = 0
      space = 2*length - 3
      for letter in (@letters[0..length -2].reverse) do
        if letter == 'A' then
          indent_length = length - 1
          text = " "*(length - 1) + letter + " "*(length - 1)
        else
          indent_length += 1
          space -= 2 
          text = " "*indent_length + letter + " "*space + letter + ''*indent_length
          
        end
        lines.append(text)
        # puts text 
      end

      return lines.join("\n")
    end
  end
  
  
  # puts Diamond.make_diamond('A')
  puts Diamond.make_diamond('C')
  puts Diamond.make_diamond('E')
  