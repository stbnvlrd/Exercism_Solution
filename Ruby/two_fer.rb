=begin
Write your code for the 'Two Fer' exercise in this file. Make the tests in
`two_fer_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/two-fer` directory.
=end

class TwoFer
  def self.two_fer(name="you")
    message = "One for " + name + ", one for me."
    return message
  end
end

  
puts TwoFer.two_fer()
puts TwoFer.two_fer(Ana)