class HighScores
    def initialize(scores)
      @list_scores = []
      for score in scores do
        @list_scores.append(score)
      end
    end

    def scores
      return @list_scores
    end
  
    def latest
      return @list_scores[-1]
    end
  end

end

scores = [30, 50, 20, 70]
score = HighScores.new(scores)
puts score.scores
puts score.latest

scores = [100, 0, 90, 30]
score = HighScores.new(scores)
puts score.scores
puts score.latest

scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
score = HighScores.new(scores)
puts score.scores
puts score.latest
