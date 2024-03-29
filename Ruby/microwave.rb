class Microwave
  def initialize(time)
    if time > 9 then
      seconds = ((time.to_s[-2..-1]).to_i % 60).to_s
    else
      seconds = (time % 60).to_s
    end
    minutes = ((time.to_s[0..-3]).to_i + ((time.to_s[-2..-1]).to_i / 60)).to_s
    
    @minutes = minutes
    @seconds = seconds
  end

  def timer
    if @minutes.length == 1 then
      @minutes = "0" + @minutes
    end
    if @seconds.length == 1 then
      @seconds = "0" + @seconds
    end
    final_time = @minutes + ":" + @seconds
  end
end
      

Microwave.new(1).timer == "00:01" ? (puts "True") : (puts "False" + " " + Microwave.new(1).timer)

Microwave.new(59).timer == "00:59" ? (puts "True") : (puts "False" + " " + Microwave.new(59).timer)

Microwave.new(60).timer == "01:00" ? (puts "True") : (puts "False" + " " + Microwave.new(60).timer)

Microwave.new(100).timer == "01:00" ? (puts "True") : (puts "False" + " " + Microwave.new(100).timer)

Microwave.new(200).timer == "02:00" ? (puts "True") : (puts "False" + " " + Microwave.new(200).timer)

Microwave.new(1001).timer == "10:01" ? (puts "True") : (puts "False" + " " + Microwave.new(1001).timer)

Microwave.new(272).timer == "03:12" ? (puts "True") : (puts "False" + " " + Microwave.new(272).timer)
