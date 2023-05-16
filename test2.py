from random import randint
top_scores = [[940, 'name14', '5/13/1333'], [866, 'name37', '5/13/1333'], [848, 'name95', '5/13/1333'], [833, 'name16', '5/13/1333'], [494, 'name21', '5/13/1333'], [414, 'name61', '5/13/1333'], [364, 'name41', '5/13/1333'], [148, 'name14', '5/13/1333'], [147, 'name49', '5/13/1333'], [77, 'name33', '5/13/1333']]
rands = []
for item in top_scores:
    s = item[1]
    rands.append(s)
for i in range(0,1):
    rand = randint(1,100)
    rands.append(rand)
    string = "name" + str(randint(1,20))
    new_score = [rand, string, "5/16/23"]
    top_scores.append(new_score)
    print(new_score)
rands.sort()
rands.reverse()
print(rands)
new = []
for score in top_scores:
    s = score[0]
    new.append(s)
new.sort()
new.reverse()
new = new[:10]
print(new)
new_top = []
for score in top_scores:
    s = score[1]
    if s in new:
        new_top.append(score)
new_top = new_top[:10]
new_top.sort()
new_top.reverse()
print(new_top)