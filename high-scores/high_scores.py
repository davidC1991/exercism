

def latest(scores):
    return scores[len(scores)-1]
    


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scoreMaxs=[]
    scores=sorted(scores)
    if len(scores)>2:
        scoreMaxs.extend(scores[len(scores)-3:len(scores)])    
        return scoreMaxs[::-1]
    else:
        return scores[::-1]