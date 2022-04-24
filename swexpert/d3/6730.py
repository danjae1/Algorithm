T = int(input())

for i in range(T):
    li = input().strip()
    print("#%d " % (i+1), end="")
    for ch in li:
        if ch == 'a' or ch == 'e' or ch =='i'  or ch =='o'  or ch =='u':
            continue
        else:
            print(ch, end="")
    print()