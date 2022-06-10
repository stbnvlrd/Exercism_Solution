
class Anagram
    def initialize(anagram)
      @anagram = anagram.downcase.split("")
      @letter_count = anagram.length
    end
  
    def match(words)
      count = Array.new(words.length, 0)
      result= []
      words.each_with_index do |word, index|
        @anagram.each do |letter|
          if word.downcase.include? letter
            count[index] = count[index] + 1
          end
        end
      end
      count.each_with_index do |word, index|
        if word == @letter_count and words[index].length == @letter_count and words[index].downcase != @anagram.join("")
          result << words[index]
        end
      end
    result.each do |word|
      @anagram.each do |letters|
        if @anagram.count(letters) != word.downcase.count(letters)
          result.delete(word)
        end
      end
    end
    return result
    end
  end
      
    
      
detector = Anagram.new('BANANA')
anagrams = detector.match(%w[BANANA Banana banana])
# puts anagrams