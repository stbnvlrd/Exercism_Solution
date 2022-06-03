class SpaceAge
    def initialize(second)
      # second_int = second.gsub('_','').to_f
      @year_earth = ((((second/60.0)/60.0)/24.0)/365.25).round(2)
    end
  
    def on_earth
      @year_earth
    end
  
    def on_mercury
      (@year_earth/0.2408467).round(2)
    end  

    def on_venus
      (@year_earth/0.61519726).round(2)
    end  

    def on_mars
      (@year_earth/1.8808158).round(2)
    end  

    def on_jupiter
      (@year_earth/11.862615).round(2)
    end  

    def on_saturn
      (@year_earth/29.447498).round(2)
    end  

    def on_uranus
      (@year_earth/84.016846).round(2)
    end  

    def on_neptune
      (@year_earth/164.79132).round(2)
    end
  end

  age = SpaceAge.new(1_000_000_000)
  puts age.on_earth

  age = SpaceAge.new(2_134_835_688)
  puts age.on_mercury