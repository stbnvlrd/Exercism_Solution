class WordProblem
  def initialize(phrase)
    phrase = phrase.slice!(8..-2)
    phrase = phrase.gsub(' by', ' ')
    @phrase = phrase.split(' ')  
    # puts @phrase
  end

  def answer
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
    return result
  end
end
    
  problem = WordProblem.new("What is 1 plus 1 plus 1?")
  puts problem.answer

  problem = WordProblem.new("What is 10 divided by 2 plus 1?")
  puts problem.answer

  problem = WordProblem.new("What is 1 minus 1 plus 1?")
  puts problem.answer