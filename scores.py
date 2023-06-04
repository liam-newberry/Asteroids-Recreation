# File created by: Liam Newberry
from settings_copy import *
# high scores for specific device
MAX_HIGH_SCORES = 10
high_scores = []
# name of high score document
path_to_high_scores = "asteroid_high_scores.csv"

def load_high_scores():
    lines = []
    # seperates different score sets by line
    try:
        with open(path_to_high_scores) as file:
            lines = file.read().splitlines()
    except:
        pass
    count = 0
    # seperate the name, date, score in each line
    for line in lines:
        line_list = line.split(',')
        if len(line_list) == 3:
            name = line_list[2]
            date = line_list[1]
            score = int(line_list[0])
            new_score = [score,date,name]
            high_scores.append(new_score)
            count += 1
            if count > MAX_HIGH_SCORES:
                break

def save_high_scores():
    # write new high scores in the document
    with open(path_to_high_scores,'w') as f:
        for score in high_scores:
            name = score[2]
            date = score[1]
            s = score[0]
            s = str(s)
            print(s + ',' + date + ',' + name, file=f)

def is_high_score(score):
    # if the score is 0, then it's not a high score
    if score == 0:
        return False
    count = 0
    for item in high_scores:
        count += 1
        # if the score is bigger than a score in our list, then it is a high score
        if score > item[0]:
            return True
    # if we don't have the max number of high scores yet, then this is a high score
    if count < MAX_HIGH_SCORES:
        return True
    # not a high score
    return False

def add_high_score(name,date,score):
    # create new high score and add to doc
    # all data for doc
    high_score = [score,date,name]
    inserted = False
    # find pos for the new high score
    for i in range(0,len(high_scores)):
        if score > high_scores[i][0]:
            high_scores.insert(i, high_score)
            inserted = True
            break
    if not inserted:
        high_scores.append(high_score)
    while len(high_scores) > MAX_HIGH_SCORES:
        high_scores.pop(-1)
    save_high_scores()