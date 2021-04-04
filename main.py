import random
import re, string

with open('text.txt', 'r') as file:
    contents = []
    for line in file.readlines():
        for word in line.split(" "):
            contents.append(re.sub(r'[\W]+', '', word.lower()))

D = dict()

for i in range(len(contents)-1):
    cw = contents[i]
    nw = contents[i+1]

    if cw not in D:
        D[cw] = [nw]
    else:
        D[cw].append(nw)


init_word = random.choice(list(D.keys()))
res = [init_word]

N = 50

for i in range(N):
    w = res[i]
    n = random.choice(D[w])
    res.append(n)

res[0] = res[0].capitalize()
res.append(".")
print(" ".join(res))
