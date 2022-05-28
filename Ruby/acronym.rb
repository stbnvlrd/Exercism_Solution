=begin
Write your code for the 'Acronym' exercise in this file. Make the tests in
`acronym_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/acronym` directory.
=end

class Acronym
    def self.abbreviate(phrase)
      acronym = ''
      phrase = phrase.gsub('- ','')
      phrase = phrase.gsub('-',' ')
      phrase_words = phrase.split(' ')
      phrase_words.each do |word|
        acronym = acronym + word[0]
      end
    acronym = acronym.upcase
    end
  end
    