class Pangram
  
    def self.pangram?(sentence)
      sentence = sentence.downcase
      count = 0
      target = ('abcdefghijklmnopqrstuvwxyz')
      target.each_char do |n|
        sentence.each_char do |m|
          if n == m
            # puts n + m
            count += 1
            break
            # puts count
          end
        end
      end
      puts count
      puts target.length
      return count == (target.length)

    end
  end

    puts Pangram.pangram?('')
    puts Pangram.pangram?('abcdefghijklmnopqrstuvwxyz')
    puts Pangram.pangram?('the quick brown fox jumps over the lazy dog')
    puts Pangram.pangram?('a quick movement of the enemy will jeopardize five gunboats')
    puts Pangram.pangram?('five boxing wizards jump quickly at it')
    puts Pangram.pangram?('the_quick_brown_fox_jumps_over_the_lazy_dog')
    puts Pangram.pangram?('the 1 quick brown fox jumps over the 2 lazy dogs')
    puts Pangram.pangram?('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog')
    puts Pangram.pangram?('"Five quacking Zephyrs jolt my wax bed."')
    puts Pangram.pangram?('the quick brown fox jumps over with lazy FX')