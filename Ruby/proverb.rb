class Proverb
    def initialize(*args, qualifier:'')
      @list = args
    end
  
    def to_s
      text = ""
      for index in (0 .. @list.length - 2)
        text += "For want of a " + @list[index] + " the " + @list[index+1] +" was lost.\n"
      end
      text += "And all for the want of a " + @list[0] + "."

    end
  end