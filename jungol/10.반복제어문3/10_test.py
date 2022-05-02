#1 아스키코드 48번부터 90번까지의 모든 문자를 출력하는 프로그램을 작성하라.

#for i in range(ord('0'),ord('Z')+1):
#    print(i,"-",chr(i))

#2 정수 n을 입력 받아, 알파벳 소문자 중 n의 배수 번째 알파벳만 출력하는 프로그램을 작성하시오.
# 입력예 2
# 출력예 bdfhjlnprtvxz

#n =int(input())

#for i in range(ord('a'),ord('z')+1,n):
#    print(chr(i),end='')

# 3자연수 n을 입력받아 출력예와 같이 출력되는 프로그램을 작성하시오.
#n = int(input())
#for i in range(1,n):
#    print("*"*i)
#for i in range(n,0,-1):
#    print("*"*i)

# 4 자연수 n을 입력받아 각 문제의 출력예와 같이 출력되는 프로그램을 작성하시오. 
#⁕⁕⁕⁕⁕ 
# ⁕⁕⁕
#  ⁕
# ⁕⁕⁕
#⁕⁕⁕⁕⁕

#n=int(input())
#for i in range(n,0,-1):
#    print((' '*(n-i))+("*"*(i*2-1)))
#for i in range(2,n+1):
#    print(((' ')*(n-i))+("*"*(i*2-1)))

#5 자연수 n을 입력받아 각 문제의 출력예와 같이 출력되는 프로그램을 작성하시오.
#입력예 3
#    ⁕
#  ⁕⁕⁕
#⁕⁕⁕⁕⁕

# a = int(input()) 
# for i in range(1,a+1):
#     print((" "*((a*2)-(i*2))) + ("*"*(i*2-1)))

#6 자연수 n을 입력받아 각 문제의 출력예와 같이 출력되는 프로그램을 작성하시오. 
# 입력예 3
#     1
#   1 2
# 1 2 3   

n=int(input())
for i in range(n):
    for j in range(1,i+2):
        print(" "*(n*2)-(i*2),j,end=' ')
    print()


