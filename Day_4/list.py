import random
friends = ["alice","bob","charlie","david","emanuel"]
#1
friends_choose = random.randint(0,len(friends)-1)
print(friends[friends_choose])
#2
print(random.choice(friends))