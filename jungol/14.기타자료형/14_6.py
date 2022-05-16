#예제6
# dic={}
# while True:
#     name=input("이름은?").strip()

#     if name in dic:
#         print("%s의 별명은 %s입니다^^" % (name,dic[name]))
#         break

#     nickname=input("%s의 별명은? " % name).strip()
#     dic[name]=nickname
#     print("="*15)

#자가진단6, 정수를 입력받아 입력받은 정수만큼 반복하면서, 각 줄에 나라의 이름과 그 나라의 수도를 공백을
#사이에 두고 입력받는다. 그 후에, 나라의 이름을 입력받아 그 나라의 수도를 출력하는 프로그램을 작성하라.
#만약 나라가 입력된 적이 없으면, Unknown Country를 출력한다.

dic={}
a=int(input())
for i in range(a):
    con,cap=input().split()
    dic[con]=cap

b=input()
if b in dic:
    print(dic[b],end='')
else:
    print('Unknown Country')