#형성평가1

#a = int(input())
#print(["No.%d" % (i+1) for i in range(a)])

#형성평가 2

# a,b=map(int,input().split())
# li=[0 for i in range(a)]

# for i in range(a):
#     li[i]

#형성평가 3

# li= [0 for i in range(6)]
# a=list(map(int,input().split()))

# for i in a:
#     li[i-1]+=1

# for i in range(6):
#     print(('%d : %d') % (i+1,li[i]))

#형성평가4

li= [0 for i in range(11)]
a = list(map(int,input().split()))

for i in a:
    li[(i//10)] += 1

for i in range(10,-1,-1):
    if li[i]>0:
        print(('%d : %d person') % (i*10,li[i]))