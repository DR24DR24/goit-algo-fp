import random
ref=[item/36*100 for item in [1,2,3,4,5,6,5,4,3,2,1]]

n=10000
res=[0]*12
for i in range(n):
    cur=random.randint(1,6)+random.randint(1,6)
    res[cur-2]+=1
normres=[item/sum(res)*100    for item in res]
for i in range(0,11):
    print(f" {i+2:>2} -> {normres[i]:>6.2f}%  {normres[i]-ref[i]:>6.2f}%")
