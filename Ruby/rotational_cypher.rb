=begin
Write your code for the 'Rotational Cipher' exercise in this file. Make the tests in
`rotational_cipher_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/rotational-cipher` directory.
=end

class RotationalCipher
    def self.rotate(text, key)
      alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
      alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      
      text.each_char.with_index do |char, index|
        if alphabet_lower.include? char
          new_index = alphabet_lower.index(char) + key
          if new_index >= 26
              new_index = new_index - 26
          end
         text[index] = alphabet_lower[new_index]
        end
        if alphabet_upper.include? char
          new_index = alphabet_upper.index(char) + key
          if new_index >= 26
              new_index = new_index - 26
          end
         text[index] = alphabet_upper[new_index]
        end
      end
      return text
    end
  end

  puts RotationalCipher.rotate("a", 0)
  puts RotationalCipher.rotate("a", 1)
  puts RotationalCipher.rotate("a", 26)
  puts RotationalCipher.rotate("m", 13)
  puts RotationalCipher.rotate("n", 13)
  puts RotationalCipher.rotate("OMG", 5)
  puts RotationalCipher.rotate("O M G", 5)
  puts RotationalCipher.rotate("Testing 1 2 3 testing", 4)
  puts RotationalCipher.rotate("Let's eat, Grandma!", 21)
  puts RotationalCipher.rotate("The quick brown fox jumps over the lazy dog.", 13)