#!/usr/bin/python3
hexa = list(range(0, 99))

for i in range(len(hexa)):
    print("{:d} = 0x{:x}".format(hexa[i], hexa[i]))
