class WordProblem
    def initialize(phrase)
      @phrase = phrase
    end
  
    def answer
      number_text = @phrase.delete "^0-9", "^ "
      numbers = number_text.split(" ")
    
      target = 'plus'
      sz = target.size
      plus = (0..@phrase.size-sz).select { |i| @phrase[i,sz] == target }

      target = 'minus'
      sz = target.size
      minus = (0..@phrase.size-sz).select { |i| @phrase[i,sz] == target }

      target = 'multiplied'
      sz = target.size
      multiplied = (0..@phrase.size-sz).select { |i| @phrase[i,sz] == target }

      target = 'divided'
      sz = target.size
      divided = (0..@phrase.size-sz).select { |i| @phrase[i,sz] == target }
    
      puts plus
      puts minus
      puts multiplied
      puts divided
      puts numbers

      if multiplied != nill
        
    end
end
    
  problem = WordProblem.new("What is 1 plus 1 plus 1?")
  puts problem.answer

  problem = WordProblem.new("What is 10 divided 2 plus 4?")
  puts problem.answer

  problem = WordProblem.new("What is 1 minus 1 minus 1?")
  puts problem.answer