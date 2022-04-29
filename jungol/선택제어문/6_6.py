#예제
#a,b,c = input("세수를 입력하시오.").split()
#a,b,c = int(a),int(b),int(c)

#if a > b:
#    if a > c:
#        max = a
#    else: 
#        max = c
#else:
#    if b > c: max = b
#    else: max = c

#print("입력받은 수 중 가장 큰 수는 %d 입니다." %)

#------------------ 남자는 'M',여자는'F'로 나타내기로 하고,18세 이상을 성인이라고 하자.
#성별과 나이를 입력받아 "MAN" (성인남자), "WOMAN"(성인여자),"BOY(미성년남자)","GIRL"(미성년여자)를 구분하여 출력하는 프로그램을 만드쇼.
#입력예 F 15
#출력예 GIRL


sex,age = input().split()
sex = str(sex)
M = 'M'
F = 'F'
age = int(age)

if age >= 18:
    if sex ==M:
        print("MAN")
    else:
        print("WOMAN")
if age <= 18:
    if sex == F:
        print("GIRL")
    else:  
        print("BOY")