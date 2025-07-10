import random
fruits = ["apple","peach","pear"]
for fruit in fruits:
    print(fruit)

scores = [12,11,23,4,46,7,456,1,2,6]
print(sum(scores))
print(max(scores))
print(min(scores))

min_scores = None
for score in scores:
    if min_scores == None:
        min_scores = score

    if score < min_scores:
        min_scores = score
print(min_scores)

print(list(range(0,6)))
print(list(range(0,11,3)))
