#예제3, 정수를 전달받아 출력 예와 같이 '*'로 이루어진 직각삼각형을 출력하는 함수를 작성하고 입력받은 정수를
# 전잘하여 출력하는 프로그램을 작성하시오.

# def star(n):
#     for i in range(1,n+1):
#         print('*' * i)

# n = int(input())
# star(n)


#자가진단3, 정수를 전달받아 다음과 같이 숫자 정사각형을 출력하는 함수를 작성하고 함수를 호출하여 입력받은
# 정수를 함수로 전달하여 출력하는 프로그램을 작성하시오.


def sq(n):
    for i in range(1,(n*n)+1):
        if i%n ==0:
            print(i)
        else:
            print(i,end=' ')

n=int(input())
sq(n)
