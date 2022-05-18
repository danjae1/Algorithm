# 예제8
# pas =[[0 for i in range(6)] for j in range(6)]
# pas[1][1]=1

# for i in range(2,6):
#     for j in range(1,i+1):
#         pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(pas[i][j], end=' ')
#     print()

#자가진단8, 반복문을 이용하여 리스트에 아래와 같이 저장한 후 출력하는 프로그램을 작성해라.
#출력예
# 1 1 1 1 1
# 1 2 3 4 5
# 1 3 6 10 15
# 1 4 10 20 35
# 1 5 15 35 70

# pas = [[0 for i in range(6)] for i in range(6)]

# for i in range(1,6):
#     pas[1][i]=1
#     pas[i][1]=1
    
# for i in range(1,6):
#     for j in range(2,6):
#         pas[i][j] = pas[i][j-1]+pas[i-1][j]

# for i in range(1,6):
#     for j in range(1,6):
#         print(pas[i][j],end=' ')
#     print()