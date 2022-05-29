=begin
Write your code for the 'Clock' exercise in this file. Make the tests in
`clock_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/clock` directory.
=end
class Clock
    def initialize(time)
      hour = (time.has_key?(:hour) ? time.fetch(:hour) : 0)
      minute = (time.has_key?(:minute) ? time.fetch(:minute) : 0)

      @minute , @hour = correct_time(minute, hour)
    end

    def correct_time(minute, hour)
      while minute < 0
        hour = hour -1+ (minute/60).floor
        minute = 60 + minute%60
      end
      while minute > 59
        hour = hour + 1
        minute = minute - 60
      end

      while hour > 23
        hour -= 24
      end
      while hour < 0
        hour += 24
      end
      return minute, hour
    end
    def  + (clock)
      clock_minute = clock.get_minute
      clock_hour = clock.get_hour
      @minute += clock_minute
      @hour += clock_hour
      @minute , @hour = correct_time(@minute, @hour)
      self
    end
  
    def  - (clock)
      clock_minute = clock.get_minute
      clock_hour = clock.get_hour
      @minute += -clock_minute
      @hour += -clock_hour
      @minute , @hour = correct_time(@minute, @hour)
      self
    end

    def == (clock)
      @hour == clock.get_hour && @minute == clock.get_minute
    end
  
    def get_minute
      @minute
    end
  
    def get_hour
      @hour
    end 
      
    def to_s
      ("%02d" % @hour) + ":" + ("%02d" % @minute)
    end
end


clock = Clock.new(hour: 6, minute: 41)
clock_final = clock - Clock.new(minute: 11)
clock_final.to_s