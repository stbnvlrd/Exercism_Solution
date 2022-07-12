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
        
        puts big_bucket_remaining
        puts small_bucket_remaining
        puts @desired_volumen
      end
    else
      while small_bucket_remaining != @desired_volumen do
        if big_bucket_remaining = @big_bucket
        small_bucket_remaining = @small_buckets
        big_bucket_remaining -= small_bucket_remaining
        while small_bucket_remaining > @small_bucket do
          small_bucket_remaining -= @small_bucket
        end
        count += 2
      end
    end
    return count
  end
end


subject = TwoBucket.new(3, 5, 1, 'one')
puts subject.moves