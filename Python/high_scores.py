def latest(scores):
    last_score = len(scores)-1
    return scores[last_score]


def personal_best(scores):
    best_score = 0
    for i in scores:
        if best_score < i:
            best_score = i
    return best_score    
            


def personal_top_three(scores):
    top_scores = [0]
    for i in scores:
        if top_scores[0] < i:
            top_scores.insert(0, i)
        else:
            if top_scores[1] < i:
                top_scores.insert(1, i)
            else:
                if top_scores[2] < i:
                    top_scores.insert(2, i)
    if len(scores) < 3:
        del top_scores[len(scores):len(top_scores)]
    else:
        del top_scores[3:len(top_scores)]
    return top_scores  
