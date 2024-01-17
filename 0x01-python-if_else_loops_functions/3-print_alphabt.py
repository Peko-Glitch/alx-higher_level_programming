#!/usr/bin/python3

alpha = list(range(97, 123))
for i in range(len(alpha)):
    if alpha[i] == 101 or alpha[i] == 113:
        continue
    print("{}".format(chr(alpha[i])), end="")
