cnt3 = 0
cnt5 = 0
a =list(map(int,input().split()))
for x in a:
    if x%3 ==0:
        cnt3+=1
    if x%5 ==0:
        cnt5+=1

print('Multiples of 3 :',cnt3)
print('Multiples of 5 :',cnt5)