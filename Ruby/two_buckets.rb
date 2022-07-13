
class TwoBucket
  def initialize(small_bucket, big_bucket, desired_volumen, full_bucket)
    @small_bucket = small_bucket
    @big_bucket = big_bucket
    @desired_volumen = desired_volumen
    @full_bucket = full_bucket
  end
    
  def moves
    count = 0
    small_bucket_remaining = 0
    big_bucket_remaining = 0
    if @full_bucket == "one" then
      while small_bucket_remaining != @desired_volumen and count < 20 do
        ### Fill Small Bucket
        if small_bucket_remaining == 0 then
          count += 1
          small_bucket_remaining = @small_bucket

        ### Empty Small Bucket in Big Bucket
        elsif small_bucket_remaining > 0 and big_bucket_remaining < @big_bucket then
          if small_bucket_remaining > (@big_bucket - big_bucket_remaining) then
            small_bucket_remaining = small_bucket_remaining - (@big_bucket - big_bucket_remaining)
            big_bucket_remaining = @big_bucket
          else
            big_bucket_remaining = small_bucket_remaining + big_bucket_remaining
            small_bucket_remaining = 0
          end
          count += 1

        ### Empty Small Bucket
        elsif big_bucket_remaining == @big_bucket then
          big_bucket_remaining = 0
          count += 1
        end

        # puts count
        # puts small_bucket_remaining
        # puts big_bucket_remaining
        @other_bucket = big_bucket_remaining
      end
    else
      while big_bucket_remaining != @desired_volumen and count < 20 do

        ### Fill Big Bucket
        if big_bucket_remaining == 0 then
          count += 1
          big_bucket_remaining = @big_bucket

        ### Empty Big Bucket in Small Bucket
        elsif big_bucket_remaining > 0 and small_bucket_remaining < @small_bucket then
          if big_bucket_remaining > (@small_bucket - small_bucket_remaining) then
            big_bucket_remaining = big_bucket_remaining - (@small_bucket - small_bucket_remaining)
            small_bucket_remaining = @small_bucket
          else
            small_bucket_remaining = small_bucket_remaining + big_bucket_remaining
            big_bucket_remaining = 0
          end
          count += 1

        ### Empty Small Bucket
        elsif small_bucket_remaining == @small_bucket then
          small_bucket_remaining = 0
          count += 1
        end
        # puts count
        # puts small_bucket_remaining
        # puts big_bucket_remaining
        @other_bucket = small_bucket_remaining
      end
    end
    return count
  end
  
  def goal_bucket
    return @full_bucket
  end
  
  def other_bucket
    return @other_bucket
  end
end
  

puts "1st Exercise"
subject = TwoBucket.new(3, 5, 1, 'one')
puts subject.moves
puts subject.goal_bucket
puts subject.other_bucket

puts "2nd Exercise"
subject = TwoBucket.new(3, 5, 1, 'two')
puts subject.moves
puts subject.goal_bucket
puts subject.other_bucket

puts "3rd Exercise"
subject = TwoBucket.new(7, 11, 2, 'one')
puts subject.moves
puts subject.goal_bucket
puts subject.other_bucket

puts "4th Exercise"
subject = TwoBucket.new(7, 11, 2, 'two')
puts subject.moves
puts subject.goal_bucket
puts subject.other_bucket

puts "5th Exercise"
subject = TwoBucket.new(1, 3, 3, 'two')
puts subject.moves
puts subject.goal_bucket
puts subject.other_bucket

puts "6th Exercise"
subject = TwoBucket.new(2, 3, 3, 'one')
puts subject.moves
puts subject.goal_bucket
puts subject.other_bucket