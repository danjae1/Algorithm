#예제4, 합과 차를 각각 리턴하는 함수를 작성한 후 두 정수를 입력받아 함수를 호출하여 두 수의 합과 차를
#출력하는 프로그램을 작성하시오.
#입력예 30 50
#출력예 두 수의 합 = 80
#출력예 두 수의 차 = 20

# def add(x,y):
#     return x+ y
# def sub(x,y):
#     cha = x-y
#     if cha <0: cha *=-1
#     return cha

# a,b=map(int,input().split())
# sum_= add(a,b)
# print("두 수의 합 = ", sum_)
# print("두 수의 차 = ", sub(a,b))

#자가진단4, 세 개의 정수를 전달받아 최대값을 구하여 리턴하는 함수를 작성하고 세 정수를 입력받아 최댓값을 출력하는
#프로그램을 작성하시오.
#입력예 -10 115 33 
#출력예 115

def big(a,b,c):
    if a >b and a>c:
        return a
    elif b > c and b > a:
        return b
    elif c>a and c>b:
        return c

x,y,z = map(int,input().split())
bbig = big(x,y,z)
print(bbig)