
# & < 교집합
# | 합집합
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a1=set(a)
b1=set(b)
c1=set(c)
print('Intersection:',a1&b1&c1)
print('Union:',a1|b1|c1)
