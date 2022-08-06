require 'prime'

class Prime
  def self.nth(number)
    sucession = 1
    primes = []
    while number >= primes.length do
      if sucession.prime? then
        primes.append(sucession)
      end
      sucession += 1
    end
    return primes[number - 1]
  end
end