class HighScores():
    
    def __init__(self, scores):
        
        self.scores = scores
        
        pass
        
    def latest(self):
        last_score = len(self.scores)-1
        print (self.scores[last_score])
        latest = self.scores[last_score]
        return latest

    def personal_best(self):
        best_score = 0
        for i in self.scores:
            if best_score < i:
                best_score = i
        return best_score    
                
    
    
    def personal_top_three(self):
        top_scores = [0]
        for i in self.scores:
            if top_scores[0] < i:
                top_scores.insert(0, i)
            else:
                if top_scores[1] < i:
                    top_scores.insert(1, i)
                else:
                    if top_scores[2] < i:
                        top_scores.insert(2, i)
        if len(self.scores) < 3:
            del top_scores[len(self.scores):len(top_scores)]
        else:
            del top_scores[3:len(top_scores)]
        return top_scores  
