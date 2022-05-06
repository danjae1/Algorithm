# 5개 단어를 입력받아 리스트에 저장한 후 출력하는 프로그램을 작성하시오.
#입력예 
#junol
#information
#gifted
#center
#high

#li=[]
#for _ in range(5):
#    li.append(input().strip())
#
#for st in li:
#    print(st)

#자가진단2 5개의 단어를 입력받아 모든 단어를 입력받은 역순으로 출력하는 프로그램을 작성해라
li=[]
for _ in range(5):
    li.append(input().strip())

for a in li[::-1]:
    print(a)