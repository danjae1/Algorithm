# 1 공백을 포함한 문자열을 입력받아 문자열 '(space)'를 기준으로 분리하여역순으로 출력하는 프로그램을 작성하시오.
# 입력예 Python (space) Programing (space) jjang!!

# a = input().strip()
# b= a.split('(space)')

# for i in b[::-1]:
#     print(i.strip())
    
# 2.문자열 한 개와 두개의 정수 x,y를 입력받아 문자열을 x만큼 왼쪽으로 순환하여 출력하는 작업을 y만큼 반복하는 
# 프로그램을 작성하시오.

# 예제
#  st=input()
# len_=len(st)

# for i in range(len_):
#     st = st[1:] + st[0]
#     print(st)

# st,x,y=input().split()
# st=str(st)
# x,y= int(x),int(y)
# l=len(st)

# for i in range(y):
#     st= st[x:] + st[0:x]
#     print(st)

#3 세 개의 문자열을 입력받아 사전순으로 가장 작은 문자열과 가장 큰 문자열을 출력하는 프로그램을 만드시오.

# a,b,c=input().split()

# if a<b and a<c:
#     print(a)
# elif b<c and b<a:
#     print(b) 
# elif c<a and c<b:
#     print(c)

# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# elif c>a and c>b:
#     print(c)

# 4 두 개의 문자열 A와 B, 한 개의 정수 n을 입력받아서 A에 B를 연결하고 A에서 n개 문자를 B에서 복사한 후
# A와 B를 출력하는 프로그램을 작성하시오. (A와 B의 문자열 길이는 50자이하고 n은 A와 B의 문자열 길이의 합보다 작다.)

a,b,n = input().split()
a,b=str(a),str(b)
n=int(n)
l=len(a+b)
l<=50
n<l

print(a+b)
print(a[0:n]+b[n:])



#5 한 개의 단어를 입력 받아서 거꾸로 뒤집어서 출력하는 작업을 반복하다 "END"라고 입력이 되면 종료하는 프로그램을
# 작성하시오 (입력받는 단어의 길이는 20이하이고, 단어의 개수는 100개 이하이다.

# while True:
#     a=input().strip()
#     if a != 'END':
#         print(a[::-1])
#     elif a == 'END':
#         break

#6 
# a =input().strip()
# if  a.isupper():
#     print("U")
#     print(a)
# elif a.islower():
#     print("L")
#     print(a.upper())
# elif a.isdigit():
#     print("D")
#     print(a)
# elif a.isupper != True:
#     print("X")
#     print(a.upper())

#7
# a=input().strip()
# b,c=input().split()

# print(a.count(b))
# a=a.replace(b,c)
# print(a)

