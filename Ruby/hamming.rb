
class Hamming
  def self.compute(strand_a, strand_b)
    count = 0
    for index in (0..strand_a.length) do
      if strand_a[index] != strand_b[index] then
        count += 1
      end
    end
    return count
  end
end

  puts Hamming.compute('GGACTGAAATCTG', 'GGACTGAAATCTG')

  puts Hamming.compute('GGACGGATTCTG', 'AGGACGGATTCT')