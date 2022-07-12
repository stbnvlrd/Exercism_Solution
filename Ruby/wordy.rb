class WordProblem
  def initialize(phrase)
    phrase = phrase.slice!(8..-2)
    phrase = phrase.gsub(' by', ' ')
    @phrase = phrase.split(' ')  
    # puts @phrase
  end

  def answer
    if @phrase.length == 2 then
      raise ArgumentError
    end
    if not Integer(@phrase[0]) then
      raise ArgumentError
    end
    case @phrase[1]
    when "plus"
      result = @phrase[0].to_i + @phrase[2].to_i 
    when "divided"
      result = @phrase[0].to_i / @phrase[2].to_i
    when "multiplied"
      result = @phrase[0].to_i * @phrase[2].to_i
    when "minus"
      result = @phrase[0].to_i - @phrase[2].to_i
    end
    if @phrase.length == 5 then
      case @phrase[3]
      when "plus"
        result = result + @phrase[4].to_i 
      when "divided"
        result = result / @phrase[4].to_i
      when "multiplied"
        result = result * @phrase[4].to_i
      when "minus"
        result = result - @phrase[4].to_i
      end
    end
    return result
  end
end
    
  problem = WordProblem.new("What is 1 plus 1 plus 1?")
  puts problem.answer

  problem = WordProblem.new("What is 10 divided by 2 plus 1?")
  puts problem.answer

  problem = WordProblem.new("What is 1 minus 1 plus 1?")
  puts problem.answer