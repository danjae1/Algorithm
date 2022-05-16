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

# li= [0 for i in range(11)]
# a = list(map(int,input().split()))

# for i in a:
#     li[(i//10)] += 1

# for i in range(10,-1,-1):
#     if li[i]>0:
#         print(('%d : %d person') % (i*10,li[i]))

#형성평가 5

# fibo=[0 for i in range(10)]
# a,b=map(int,input().split())
# fibo[0]=a
# fibo[1]=b

# for i in range(2,10):
#     fibo[i]= (fibo[i-2] + fibo[i-1])%10

# for i in range(10):
#     print(fibo[i],end=' ')

#형성평가 6

# li=[[3,5,9],[2,11,5],[8,30,10],[22,5,1]]
# sum=0
# for i in range(4):
#     for j in range(3): 
#        print(li[i][j],end=' ')
#        sum+=li[i][j]
#     print()
# print(sum)

#형성평가 7

# a=[]

# for i in range(4):
#     a.append(list(map(int,input('%dclass? ' % (i+1)).split())))
#     a[i]+=[0] # 이거 이해하기

# for i in range(4):
#     for j in range(3):
#         a[i][3] += a[i][j]   # 사실 sum을 사용하면 쉽게 풀 수 있다.

# for i in range(4):
#     print(('%dclass :') % (i+1),a[i][3])

#형성평가 8

#형성평가9

# a=[]
# print("first array")
# for i in range(2):
#     a.append(list(map(int,input().split())))
# b=[]
# print("second array")
# for i in range(2):
#     b.append(list(map(int,input().split())))

# c=[[0 for i in range(3)] for i in range(2)]

# for i in range(2):
#     for j in range(3):
#         c[i][j] = a[i][j] * b[i][j]

# for i in range(2):
#     for j in range(3):
#         print(c[i][j],end=' ')
#     print()

#형성평가 10
#4행 2열 첫 번쨰 줄 가로평균, 둘 째줄 세로 평균, 셋째줄 전체평균
#입력예 16 27           출력예 21 69 53 40
#입력예 39 100          출력예 33 58
#입력예 19 88           출력예 46
#입력예 61 20           출력예
