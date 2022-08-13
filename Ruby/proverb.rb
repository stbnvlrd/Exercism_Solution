class Proverb
    def initialize(*args, qualifier:'')
      @list = args
      @qualifier = qualifier
    end
  
    def to_s
      text = ""
      for index in (0 .. @list.length - 2)
        text += "For want of a " + @list[index] + " the " + @list[index+1] +" was lost.\n"
      end
      if @qualifier == '' then
        text += "And all for the want of a " + @list[0] + "."
      else
        text += "And all for the want of a " + @qualifier + " " + @list[0] + "."
      end
    end
  end