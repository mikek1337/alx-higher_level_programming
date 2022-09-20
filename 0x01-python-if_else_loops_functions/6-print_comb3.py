#!/usr/bin/python3
for i in range(0, 10):
    j = i + 1
    while j <= 9:
        print("{x}{j}".format(x=i, j=j), end='\n' if i == 8  else ', ')
        j += 1
