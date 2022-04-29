#예제
#1.삽입
#2.수정
#3.삭제
#메뉴를 선택하세요.

#print("1. 삽입")
#print("2. 수정")
#print("3. 삭제")
#cmd =int(input("메뉴를 선택하세요."))

#if cmd ==1:
#    print("삽입을 선택하셨습니다.")
#elif cmd ==2:
#    print("수정을 선택하셨습니다.")
#elif cmd ==3:
#    print("삭제을 선택하셨습니다.")
#else:
#    print("잘못 선택하셨습니다.")

#영문 대문자를 입력받아 'A'이면 "Excellent", 'B'이면 "Good",'C'이면 "Usually",'D'이면 "Effort",
# 'F'이면 "Failure", 그 외 문자열이면 "Mistake"라고 출력하는 프로그램을 만드시오.
#입력예 B
#출력예 Good

a = str(input())
if a == 'A':
    print("Excellent")
elif a == 'B':
    print("Good")
elif a == 'C':
    print("Usually")
elif a == 'D':
    print("Effort")
elif a == 'F':
    print("Failure")
else :
    print("Mistake")