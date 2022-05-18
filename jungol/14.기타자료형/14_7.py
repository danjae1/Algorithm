#예제7, 반장 선거의 개표 결과가 한 줄에 입력될 때, 제일 표를 많이 받은 학생을 출력하는
#프로그램을 작성해라 ( 만약 동일 수의 표를 받은 학생이 여러 명일 경우, 가장 먼저 입력된
# #학생을 우선으로 한다.)
#입력예 철기 재연 태현 태현 철기 재연 창호 창호 창호 철기 태현 창호 태현 창호

# students =input().split()
# dic={}
# for student in students:
#     if student in dic:
#         dic[student]+=1
#     else:
#         dic[student]=1

# max_=0
# for student,cnt in dic.items(): #모든 키-값 쌍에 대해 순회하기 위해서 items() 사용
#     if max_<cnt:                #반복원소인 키-값 쌍이 원소 2개의 튜플 형태로 반환되므로
#         leader,max_ = student,cnt # in키워드 앞에 student,cnt 같이 두 개의 변수를 써야한다.

# print("반장은"+leader+"입니다.")
# print(leader+"가 받은 표는"+str(cnt)+"표입니다")

#자가진단7 매 년 피아노 콩쿠르 최우수상을 받은 학생들의 이름과 정수 하나를 입력 받아,
#입력받은 정수 만큼 최우수상을 받은 학생들을 모두 출력하는 프로그램을 작성하시오.
# (먼저 입력된 이름을 우선하여 출력한다.)
# 입력예 cindy katherine mark mark cindy jack cindy maria katerine
# 입력예 2
# 출력예 Katherine
# 출력예 mark


dic={}
a=input().split()
b=int(input())

for student in a:
    if student in dic:
        dic[student]+=1
    else:
        dic[student]=1

for student,cnt in dic.items():
    if b == cnt:
        print(student)