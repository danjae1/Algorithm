sum_ = 0
a = list(map(int,input().split()))
for i in a:
    sum_+=i
    avg = sum_/len(a)
if avg < 80:
    print('avg : %.1f' % (avg))
    print("fail")
if avg >= 80:
    print('avg : %.1f' % (avg))
    print("pass")