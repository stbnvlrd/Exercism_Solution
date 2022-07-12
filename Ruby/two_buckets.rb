
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
      while big_bucket_remaining != @desired_volumen do
        count += 2
        small_bucket_remaining = @small_bucket
        big_bucket_remaining += small_bucket_remaining
        small_bucket_remaining = 0
        if big_bucket_remaining > @big_bucket then
          big_bucket_remaining -= @big_bucket
        end
          
        # puts big_bucket_remaining
        # puts small_bucket_remaining
        # puts @desired_volumen
        @other_bucket = small_bucket_remaining
      end
    else
      while small_bucket_remaining != @desired_volumen do
        if big_bucket_remaining == 0 then
          big_bucket_remaining = @big_bucket
          count += 1
        elsif big_bucket_remaining + small_bucket_remaining < @small_bucket then
          small_bucket_remaining = big_bucket_remaining
          big_bucket_remaining = 0
          count += 1
        elsif big_bucket_remaining + small_bucket_remaining > @small_bucket then
          big_bucket_remaining = big_bucket_remaining - @small_bucket + small_bucket_remaining
          small_bucket_remaining = @small_bucket
          count += 1
          
        elsif small_bucket_remaining == @small_bucket then
          small_bucket_remaining = 0
          count += 1
        end
        puts big_bucket_remaining
        puts small_bucket_remaining
        @other_bucket = big_bucket_remaining
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
  


subject = TwoBucket.new(3, 5, 1, 'one')
puts subject.moves

subject = TwoBucket.new(3, 5, 1, 'two')
puts subject.moves

subject = TwoBucket.new(7, 11, 2, 'one')
puts subject.moves

subject = TwoBucket.new(7, 11, 2, 'two')
puts subject.moves

subject = TwoBucket.new(1, 3, 3, 'two')
puts subject.moves

subject = TwoBucket.new(2, 3, 3, 'one')
puts subject.moves