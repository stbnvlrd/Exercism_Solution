=begin
Write your code for the 'ISBN Verifier' exercise in this file. Make the tests in
`isbn_verifier_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/isbn-verifier` directory.
=end
class IsbnVerifier
    def self.valid?(string)
      result = false
      isbn_num = string.gsub('-','')
      isbn_sum = 0
    #   puts isbn_num.length
      if isbn_num.length == 10
        isbn_num.each_char.with_index do |item, index|
        #   puts item
          if item == 'X' and index == 9
            item = 10
          elsif item.to_i == 0 and item != '0'
            isbn_sum = 1
            break
          end
          isbn_sum = isbn_sum + (item.to_i*(10 - index))
        end
        if isbn_sum % 11 == 0
          result = true
        end
      end
    return result
    end
  end

  puts IsbnVerifier.valid?("3-598-21508-8")
  puts IsbnVerifier.valid?("3-598-21508-9")
  puts IsbnVerifier.valid?("3-598-21507-X")
  puts IsbnVerifier.valid?("3-598-21507-A")
  puts IsbnVerifier.valid?("3-598-P1581-X")
  puts IsbnVerifier.valid?("3-598-2X507-9")
  puts IsbnVerifier.valid?("3598215088")
  puts IsbnVerifier.valid?("359821507X")
  puts IsbnVerifier.valid?("359821507")
  puts IsbnVerifier.valid?("3598215078X")
  puts IsbnVerifier.valid?("00")
  puts IsbnVerifier.valid?("3-598-21507")
  puts IsbnVerifier.valid?("3-598-21515-X")
  puts IsbnVerifier.valid?("")
  puts IsbnVerifier.valid?("134456729")
  puts IsbnVerifier.valid?("3132P34035")
  puts IsbnVerifier.valid?("98245726788")
