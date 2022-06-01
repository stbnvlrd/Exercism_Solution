=begin
Write your code for the 'Rna Transcription' exercise in this file. Make the tests in
`rna_transcription_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/rna-transcription` directory.
=end
class Complement
  
    def self.of_dna(data="")
      @data_complement = ""
      puts data
      data.each_char do |n|
        if n == "G"
          @data_complement += "C"
        elsif n == "A"
          @data_complement += "U"
        elsif n == "C"
          @data_complement += "G"
        elsif n == "T"
          @data_complement += "A"
          end
        end
        return @data_complement  
      end
    end
Complement.of_dna("A")
Complement.of_dna("G")
Complement.of_dna("T")
Complement.of_dna("C")
Complement.of_dna('ACGTGGTCTTAA')