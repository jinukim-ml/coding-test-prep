import sys
a = int(sys.stdin.readline())
if a >= 0 and a <= 100:
    if a >= 90 and a <= 100:
        print("A")
    elif a >= 80 and a <= 89:
        print("B")
    elif a >= 70 and a <= 79:
        print("C")
    elif a >= 60 and a <= 69:
        print("D")
    else:
        print("F")