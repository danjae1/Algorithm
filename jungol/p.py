while True:
    t = int(input())
    if t < 0:
        break
    if t%3 != 0:
        continue
    elif t%3 == 0:
        t//3
        print(t//3)
    