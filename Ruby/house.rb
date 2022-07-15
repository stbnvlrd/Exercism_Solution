FIRST_LINE = ["This is the house that Jack built.\n", "This is the malt", "This is the rat", "This is the cat", "This is the dog", "This is the cow with the crumpled horn", "This is the maiden all forlorn", "This is the man all tattered and torn", "This is the priest all shaven and shorn", "This is the rooster that crowed in the morn", "This is the farmer sowing his corn", "This is the horse and the hound and the horn"]

NOT_FIRST_LINE = ["that lay in the house that Jack built.\n", "that ate the malt", "that killed the rat", "that worried the cat", "that tossed the dog", "that milked the cow with the crumpled horn", "that kissed the maiden all forlorn", "that married the man all tattered and torn", "that woke the priest all shaven and shorn", "that kept the rooster that crowed in the morn", "that belonged to the farmer sowing his corn"]


class House
  def self.recite
    poem = []
    for x in (0..FIRST_LINE.length-1) do
      poem.append(FIRST_LINE[x])
      if x > 0 then
        for y in (0..x-1) do
          poem.append(NOT_FIRST_LINE[x-1-y])
        end
      end
    end
    return poem.join("\n")
  end
end

puts House.recite
