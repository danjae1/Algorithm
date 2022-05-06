


#d = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#while True:
#     year = int(input("YEAR = "))
#    month =int(input("MONTH = "))
#    if month ==0:break
#    if month>12 or month <0:
#        print("잘못 입력하였습니다.")
#    else:
#        if year % 400 ==0:
#            d[2] = 29
#        elif year % 4 ==0 and year % 100!= 0:
#            d[2] = 29
#        else:
#            d[2] = 28
#        print("입력하신 달의 날 수는 %d일입니다.\n" %d[month])

# 1반부터 6반까지의 평균점수를 저장한 후, 두 반을 입력받아 두 반 평균점수의 합을 출력하는
# 프로그램을 작성하시오. 반별 평균점수는 초기값으로 1반부터 차례로 85.6,79.5,83.1,80.0,78.2,75.0으로
#초기화하고 출력은 소수 첫째자리까지 한다.

avg= [85.6,79.5,83.1,80.0,78.2,75.0]
a,b=input().split()
a,b=int(a),int(b)
print(avg[a-1]+avg[b-1])