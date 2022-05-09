#3행 3열의 리스트 두 개를 만들어서 입력을 받고 두 리스트 각 행렬끼리의 합을 구하여 출력하는 프로그램을 작성하시오.


# a= [0 for i in range(3)]
# for i in range(3):
#     q="첫 번째 배열 %d행 " % (i+1)
#     a[i] = list(map(int,input(q).split()))

# b=[]
# for i in range(3):
#     q="두 번쨰 배열 %d행 " % (i+1)
#     tmp=input(q).split()
#     b.append(list(map(int,tmp)))

# c=[[0 for i in range(3)] for j in range(3)]
# for i in range(3):
#     for j in range(3):
#         c[i][j] = a[i][j] + b[i][j]

# for i in range(3):
#     for j in range(3):
#         print(c[i][j], end=' ')
#     print()


#자가진단6, 2행 4열의 리스트 두 개를 만들어서 입력을 받고 두 리스트의 곱을 구하여 출력하는 프로그램을 작성해라.
# 입력예 first arry
# 입력예 1 2 3 4
# 입력예 5 6 7 8
# 입력예 second array
# 입력예 1 4 7 8
# 입력예 3 6 9 8
# 출력예 1 8 21 32
# 출력예 15 36 63 64

a=[]
for i in range(2):
    a.append(list(map(int,input("first array").split())))

b=[]
for i in range(2):
    b.append(list(map(int,input("second array").split())))

c=[[0 for i in range(4)] for j in range(2)]
for i in range(2):
    for j in range(4):
        c[i][j] = a[i][j] * b[i][j]

for i in range(2):
    for j in range(4):
        print(c[i][j],end=' ')
    print()