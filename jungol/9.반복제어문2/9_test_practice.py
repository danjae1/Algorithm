# 자연수 n을 입력받아서 n개의 줄에 n + 1개의 숫자와 문자로 채워서 다음과 같이 출력하는 프로그램을 작성하시오

# n =input().strip()

# for i in range(1,1+n):
#     for j in range(1,n+2):
#         print(i,end='')


a= 1
n=int(input())
b = ord('A')

for i in range(1,n+1):
    for j in range(n-i+1):
        print(a,end=' ')
        a+=1
    for j in range(i):
        print(chr(b),end=' ')
        b+=1
    print()
