#형성평가1, 세 개의 실수를 입력받아, 그 합, 곱으로 이루어진 튜플을 출력하는 프로그램을 작성해라
#입력예 3.141 1.414 2.717
#출력예 (7.272, 12.067213158)
# a,b,c=input().split()
# a,b,c=float(a),float(b),float(c)
# abc=a+b+c
# cba=a*b*c
# print(('(%.3f, %.3f)') % (abc,cba))


#형성평가2

# a=int(input())
# li=[]

# for i in range(a):
#     b,c=input().split()
#     cnt=(b,c)
#     li.append(cnt)
# print(li)

#형성평가3, 주차장에 세워진 자동차의 차종을 모두 입력 받아, 중복되어 입력된 이름을 제거
#한 후, 알파벳 순서대로 출력하고, 그 개수를 출력하는 프로그램을 작성하시오
#입력예 gra ava son son ava gen son
#출력예 ava gen gra son
#출력예 4

# a=list(input().split())
# aa=dict.fromkeys(a)
# a=list(aa)
# a.sort()

# for x in a:
#     print(x,end=' ')
# print()
# print(len(a))

#형성평가4, 두 줄에 여러 개의 정수를 입력 받아, 첫 번째 줄에는 존재하면서 두 번째 줄에는
# 존재하지 않는 숫자를 오름차순(크기가 작은 수부터 큰 수의 순서)으로 출력하는 프로그램
#작성해라 (중복된 원소는 하나만 출력한다.)
#입력예 90 95 100 70 95 90 50
#입력예 100 85 75 65 95
#출력예 50 70 90

# a=set(map(int,input().split()))
# b=set(map(int,input().split()))
# c=a-b
# c=list(c)
# c.sort()
# for i in c:
#     print(i,end=' ')

#형성평가5, 정수를 입력 받아 정수만큼 반복하면서 키,자료 쌍을 공백을 사이에 두고 입력받아
# 딕셔너리에 추가한다. 마지막으로 문자열을 하나 더 입력 받아, 그 문자열을 키 값으로 하는
#자료를 출력하는 프로그램을 작성하시오.(동일한 키 값이 두 번 입력되는 경우는 없다.)

# a=int(input())
# music=dict()
# for i in range(a):
#     mus,num=input().split()
#     music[mus]=num

# b=str(input())
# if b in music:
#     print(music[b])

#형성평가6, 야구선수들의 파울 기록을 입력 받아, 파울을 가장 적게 한 선수를 모두 출력하고,
#최소 파울 횟수를 마지막에 출력하는 프로그램을 작성하시오.
#입력예 jay john john jay jack jack john jo jo jack

dic={}
a=input().split()
min_=1000
for i in a:
    if i in dic:
        dic[i]+=1
    else: 
        dic[i]=1
        

for i,bb in dic.items():
    if min_>=bb:
        min_=bb
        
for i,bb in dic.items():
    if bb==min_:
        print(i)
print(min_)

