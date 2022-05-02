
# while True:
#     print("1.입력하기")
#     print("2.출력하기")
#     print("3.삭제하기")
#     print("4.끝내기")
#     a=input('작업할 번호를 선택하세요.')
#     a=int(a)
#     print()

#     if a == 1:
#         print('입력하기를 선택하였습니다.')
#     elif a == 2:
#         print('출력하기를 선택하였습니다')
#     elif a == 3:
#         print('삭제하기를 선택하였습니다.')
#     elif a == 4:
#         print('끝내기를 선택하였습니다.')
#         break
#     else:
#         print("잘못 선택하였습니다.")
#     print()

# 아래와 같이 나라 이름을 출력하고 숫자를 입력 받아 해당하는 나라의 수도를 출력하는 작업을 반복하다가 
# 해당하는 번호 이외의 숫자가 입력되면 "none"이라고 출력한 후 종료하는 프로그램을 작성하시오.

# * 각 나라의 수도 : 

# 대한민국 = 서울(Seoul)

# 미국 = 워싱턴(Washington)

# 일본 = 동경(Tokyo)

# 중국 = 북경(Beijing)​ 

while True:
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    a =int(input('number? '))
    if a == 1:
        print('Seoul')
    elif a == 2:
        print("Washington")
    elif a == 3:
        print('Tokyo')
    elif a == 4:
        print('Beijing')
    else:
        print('none')
        break