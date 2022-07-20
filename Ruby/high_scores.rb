class HighScores
    def initialize(scores)
      @list_scores = []
      for score in scores do
        @list_scores.append(score)
      end
    end
end
