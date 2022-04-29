#몸무게 + 100 - 키를 비만수치 공식이라고 하자.
#키와 몸무게를 입력받아 첫 번째 줄에 비만수치를 출력하고
#비만 수치가 0보다 크면 다음 줄에 "Obesity"를 출력하는 프로그램을 작성하시오.
#입력예 155
#       60
#출력예 5
#      Obesit

height =int(input())
weight =int(input())
a = weight +100 -height
print(a)
if a > 0:
    print("Obesity")


