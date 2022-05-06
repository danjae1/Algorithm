
#words =["champion","tel","pencil","jungol","olympiad","class","information","lesson","book"\
#    ,"lion"]

#ch=input("문자를 입력하세요. ").strip()
#flag = 0

#for word in words:
#    if word[0] == ch:
#        print(word)
#        flag = 1

#if flag ==0:
#    print("찾는 단어가 없습니다.")

li =[]

for _ in range(10):
    li.append(input().strip())

a =input().strip()
for i in li:
    if i[-1] ==a:
        print(i)
        flag=1

