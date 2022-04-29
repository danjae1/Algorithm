

# max_data = a if a > b else b
# => if와 else 사이의 조건이 참이면 a의 값 리턴, 거짓이면 b의 값 리턴.
#if a>b:
#   max_data = a
#else:
#   max_data = b

#8# 3개의 정수를 입력받아 삼항 연산자를 이용하여 입력받은 수들 중 최소값을 출력하는 프로그램을 작성하시오,
#입력예 18 -5 10
#출력예 -5

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

min = a if a < b else b
min = min if min < c else c
print(min)