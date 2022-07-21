class Phrase
    def initialize(phrase)
      phrase.gsub!(",", " ")
      phrase.gsub!("'", " ")
      phrase.gsub!("  ", " ")
      phrase.gsub!(/[^0-9A-Za-z ]/, '')
      phrase.gsub!(" t ", "'t ")
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
  