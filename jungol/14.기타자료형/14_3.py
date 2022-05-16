#예제3
# li=[]
# a=int(input('학생은 몇 명?'))

# for _ in range(a):
#     name,age,lang = input('이름 나이 사용언어?').split()
#     tup=(name,age,lang)
#     li.append(tup)

# for name,age,lang in li:
#     if int(age)<=19 and lang =='Python':
#         print(name)

#자가진단3
#인터넷 게임 계정의 수를 입력 받은 후, 각 계정의 아이디, 승률, 계급을 입력 받아, 계급이 'Bronze'
#아니면서 승률이 60.0 이상이거나, 계급이 'Platinum'인 아이디를 입력 받은 순서대로 출력 예와 같은
#형식으로 "[Gosu]" 를 붙여 출력하는 프로그램을 작성하시오.

# li=[]
# a=int(input())

# for i in range(a):
#     name,rate,tier = input().split()
#     cnt=(name,rate,tier)
#     li.append(cnt)

# for name,rate,tier in li:
#     if tier != 'Bronze' and float(rate)>60.0 or tier == 'Platinum':
#         print('[Gosu]',name)