T = int(input())

for i in range(T):
    L, U, X = input().split()
    L = int(L)
    U = int(U)
    X = int(X)

    ans = 0
    # 운동을 덜한경우
    if L > X:
        ans = L - X
    else :
        # 운동을 더한경우
        if X > U:
            ans = -1
        else:
            ans = 0

    print("#%d %d" % (i+1, ans))