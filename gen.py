import os


lim = 10000000
for i in range(0, lim, 100000):
    with open(f"{i}.txt", "w") as f:
        f.write(str(i))

