#예제6, 실수의 연산식을 입력받아 연산을 위한 함수를 호출하여 사칙연산의 결과를 출력하는 프로그램을 작성하시오.
# ( 각각의 실수는 소수 첫째자리까지 출력하고 사칙연산 이외의 결과는 0.0으로 한다.)
#입력예 15.5 / 3.1
#출력예 15.5 / 3.1 = 5.0

# def gesan(x,y,op):
#     if op == '+': return x+y
#     if op == '/': return x/y
#     if op == '-': return x-y
#     if op == '*': return x*y
#     return 0.0

# a,c,b = input().split()
# a=float(a)
# b=float(b)
# print('%.1f %c %.1f = %.1f' % (a,c,b,gesan(a,b,c)))

#자가진단6, 정수의 연산식을 입력받아 연산을 위한 함수를 호출하여 사칙연산(+-*/)의 연산결과를 출력하는
#프로그램을 작성해라 (/의 경우 정수 부분만 출력하고 사친연산 이외의 연산결과는 0으로 한다.)
#입력예 10 + 20
#출력예 10 + 20 = 30

def su(x,y,op):
    if op == '+': return x+y
    if op == '/': return x//y
    if op == '-': return x-y
    if op == '*': return x*y
    return 0

a,c,b = input().split()
a=int(a)
b=int(b)
print('%d %c %d = %d' % (a,c,b,su(a,b,c)))
