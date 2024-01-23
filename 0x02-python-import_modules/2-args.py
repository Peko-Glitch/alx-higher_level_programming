#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    x = len(argv) - 1
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("{} argument:".format(x))
        print("{}: {}".format(x, argv[x]))
    elif x > 1:
        print("{} arguments:".format(x))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
