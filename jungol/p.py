#2차원 리스트를 생성하여 1행의 1열과 3열, 5열을 각각 1로 
# 나머지는 모두 0으로 초기화한 후 2행부터는 바로 전행의 왼쪽과 오른쪽의 값을 더하여 
# 채운 후 출력하는 프로그램을 작성하시오. 
#입력예
# 1 0 1 0 1
# 0 2 0 2 0
# 2 0 4 0 2
# 0 6 0 6 0
# 6 0 12 0 6

pas =[[0 for i in range(7)] for i in range(7)]

for i in range(1,6,2):
    pas[1][i]=1
    
for i in range(2,6):
    for j in range(1,6):
        pas[i][j] =  pas[i-1][j-1] + pas[i-1][j+1]

for i in range(1,6):
    for j in range(1,6):
        print(pas[i][j],end=' ')
    print()