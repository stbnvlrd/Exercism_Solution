=begin
Write your code for the 'Scale Generator' exercise in this file. Make the tests in
`scale_generator_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/scale-generator` directory.
=end

class Scale
    SHARP = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    FLATS = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    def initialize(note, scale, interval = "m"*11)
      @note = note
      @note_cap = note.capitalize
      @scale = scale
      @interval = interval
    end
  
    def name
      name = @note_cap.to_s + " " + @scale.to_s
    end
  
    def pitches
      pitches = [@note_cap]
      if SHARP.include? @note_cap and @note != 'g' and @note != 'F' and @note != 'd'
        pitch_type = SHARP
      else
        pitch_type = FLATS
      end
      index = pitch_type.index(@note_cap)
      @interval.each_char do |char|
        if char == "m"
          index = index + 1
        elsif char == "M"
          index = index + 2
        elsif char == "A"
          index = index + 3
        end
        if index >= 12
          index = index - 12
        end
        if !pitches.include? pitch_type[index]  
          pitches << pitch_type[index]
        end
      end
    return pitches
    end
  end
  