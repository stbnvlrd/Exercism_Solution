class Series
    def initialize(serie)
      @series = serie
    end
  
    def slices(length)
      if length <= @series.length then
        subtrings = []
        for index in (0..@series.length-length) do
          subtrings.append(@series[index..index+length-1])
        end
      else
        raise ArgumentError
      end
    return subtrings
    end
  end
  