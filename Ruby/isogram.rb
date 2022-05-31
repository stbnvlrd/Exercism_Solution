=begin
Write your code for the 'Isogram' exercise in this file. Make the tests in
`isogram_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/isogram` directory.
=end

class Isogram
    def self.isogram?(phrase)
      phrase = phrase.downcase
      phrase = phrase.gsub(' ','')
      phrase = phrase.gsub('-','')
      phrase.each_char do |char|
        if phrase.count(char) > 1
          return false
          break
        end
      end
      return true
    end
  end
  

puts Isogram.isogram?('')
puts Isogram.isogram?('isogram')
puts Isogram.isogram?('eleven')
puts Isogram.isogram?('zzyzx')
puts Isogram.isogram?('subdermatoglyphic')
puts Isogram.isogram?('Alphabet')
puts Isogram.isogram?('alphAbet')
puts Isogram.isogram?('thumbscrew-japingly')
puts Isogram.isogram?('thumbscrew-jappingly')
puts Isogram.isogram?('six-year-old')
puts Isogram.isogram?('Emily Jung Schwartzkopf')
puts Isogram.isogram?('accentor')
puts Isogram.isogram?('angola')
  