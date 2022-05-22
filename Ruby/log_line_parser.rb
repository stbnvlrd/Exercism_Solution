class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    message_line = @line.slice(@line.index(' ') + 1, @line.size - 1)
    message_line = message_line.gsub(/[\t\r\n]/,'')
    message_line = message_line.strip
    return message_line
  end

  def log_level
    message_line = @line.slice(@line.index('[') + 1, @line.index(']') -1 )
    message_line = message_line.downcase
    return message_line
  end

  def reformat
    message_line = message + " (" + log_level + ")"
  end
end
