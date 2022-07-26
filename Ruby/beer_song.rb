class BeerSong
    def self.recite(start, length)
      counter = start
      whole_text = ""
      while counter > start-length do
        if counter == 1 then
          phrase = counter.to_s + " bottle of beer on the wall, " +  counter.to_s + " bottle of beer.\n"
        elsif counter == 0 then
          phrase = "No more bottles of beer on the wall, no more bottles of beer.\n"
        else
          phrase = counter.to_s + " bottles of beer on the wall, " +  counter.to_s + " bottles of beer.\n"
        end
        whole_text += phrase + "\n"
      end
    return whole_text[0..-2]
    end
  end