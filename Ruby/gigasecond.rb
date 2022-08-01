class Gigasecond
  def self.from(time)
    return time + 1000000000
  end
end

puts Gigasecond.from(Time.utc(2011, 4, 25, 0, 0, 0))
puts Gigasecond.from(Time.utc(1977, 6, 13, 0, 0, 0))
puts Gigasecond.from(Time.utc(1959, 7, 19, 0, 0, 0))
puts Gigasecond.from(Time.utc(2015, 1, 24, 22, 0, 0))
puts Gigasecond.from(Time.utc(2015, 1, 24, 23, 59, 59))