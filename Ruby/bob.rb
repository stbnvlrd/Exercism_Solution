class Bob

    def self.hey(message)
      while message[-1] == " "
        message = message[0..-2]
      end
      count_down = 0
      count_up = 0
      message.each_char do |letter| 
        if ("a".."z").include?(letter)
          count_down += 1
        end
        if ("A".."Z").include?(letter)
          count_up += 1
        end
      end
      capitalize = ((count_down == 0) and (count_up != 0))
      if message.to_s.strip.empty?
        responde = "Fine. Be that way!"
      elsif message[-1] == "?" and !capitalize
        responde = "Sure."
      elsif message[-1] == "?" and capitalize
        responde = "Calm down, I know what I'm doing!"
      elsif capitalize
        responde = "Whoa, chill out!"
      else
        responde = "Whatever."
      end
    return responde
    end
  end

  
info = Bob.hey("Tom-ay-to, tom-aaaah-to.")
puts info