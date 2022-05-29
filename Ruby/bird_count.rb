class BirdCount
    @last_week_count = [0, 2, 5, 3, 7, 8, 4]
    def self.last_week
      return @last_week_count
    end
  
    def initialize(birds_per_day)
      @this_week_count = birds_per_day
    end
  
    def yesterday
      @this_week_count[-2]
    end
  
    def total
      @this_week_count.sum
    end
  
    def busy_days
      count = 0
      @this_week_count.each do |days|
        if days >= 5 
          count += 1
        end
      end
    return count
    end
  
    def day_without_birds?
      @this_week_count.include?(0)
    end
  end
  