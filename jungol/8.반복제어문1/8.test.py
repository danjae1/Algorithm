#1정수를 입력받아 1부터 입력받은 정수까지 차례대로 출력하는 프로그램을 작성하시오.
#입력예 5
#출력예 1 2 3 4 5

# a = int(input())
# b = 1
# while b <= a:
#     print(b, end =' ')
#     b += 1

#2 정수를 입력받다가 0이 입력되면 그 떄까지 입력받은 홀수의 개수와 짝수의 개수를 출력하는 
#프로그램을 만드시오.
# odd = 0
# even = 0
# while True:
#     a =input()
#     a=int(a)
#     if a == 0:
#         print('odd :',odd)
#         print('even :',even)
#         break
#     elif a % 2 == 0:
#         even+=1
#         continue
#     elif a % 2 != 0:
#         odd+=1
        
#3 0부터 100까지 점수를 계쏙 입력받다가 범위를 벗어나는 수가 입력되면 그 이전까지 입력된 자료의
# 합계와 평균을 출력하는 프로그램을 작성하시오 ( 평균은 반올림하여 소수 첫쨰자리까지 출력)

# sum_ = cnt =0
# while True:
#     a =int(input())
#     if a > 100:
#         break
#     if a >= 0 or a <= 100:
#         sum_+=a
#         cnt+=1
# avg= sum_/cnt
# avg=float(avg)
# print('sum :',sum_)
# print('avg : %.1f' % (avg))
    
#4 0이 입력될 떄까지 정수를 계속 입력받아 3의 배수와 5의 배수를 제외한 수들의 개수를 
#출력하는 프로그램을 작성하시오.

# cnt=0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     if a%3 ==0 or a%5 ==0:
#         continue
#     else:
#         cnt+=1
# print(cnt)

#5 삼각형의 밑변의 길이와 높이를 입력받아 넓이를 출력하고, "Continue?"에서 'Y'나 'y'를
#입력하면 작업을 반복하고 다른 문자를 입력하면 종료하는 프로그램을 작성하시오.
#(넓이는 반올림하여 소수 첫쨰 자리까지 출력한다.)



while True:
    witch = int(input('Witch ='))
    height =int(input('Height ='))
    a = (witch*height)/2
    print('Triangle Area =',a)
    yn = input('Continue?')
    if yn == 'Y'or yn =='y':
        continue
    else:
        break

