#정수를 계속 입력받다가 100이상의 수가 입력되면 마지막 입력된 수를 포함해 
#합계와 평균을 출력하는 프로그램을 작성하시오. ( 평균은 반올림하여 소수 첫쨰차리까지 출력.)

sum_ = 0
cnt = 0 

while True:
    a = int(input())
    if a >= 100:
        sum_+=a
        cnt +=1
        break
    sum_+=a
    cnt +=1
        
    
avg = sum_/cnt
print(sum_)
print('%.1f' % avg)