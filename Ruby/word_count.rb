class Phrase
    def initialize(phrase)
      @separeted_phrase = phrase.downcase.split(" ")
    end
  
    def word_count
      words = Hash.new(0)
      @separeted_phrase.each do |word|
        words[word] += 1
      end
    return words
    end
  
  end
  