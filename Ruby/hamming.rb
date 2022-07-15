
class Hamming
  def self.compute(strand_a, strand_b)
    count = 0
    if strand_a.length == strand_b.length then
      for index in (0..strand_a.length) do
        if strand_a[index] != strand_b[index] then
          count += 1
        end
      end
    else
      raise ArgumentError
    end
    return count
  end
end
        

  puts Hamming.compute('GGACTGAAATCTG', 'GGACTGAAATCTG')

  puts Hamming.compute('GGACGGATTCTG', 'AGGACGGATTCT')