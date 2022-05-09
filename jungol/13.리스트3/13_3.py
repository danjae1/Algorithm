# 정수 리스트를 입력받아 입력된 정수의 일의 자리 숫자가 각각 몇개인지 작은 수부터 출력하는 프로그램을 작성하시오.
# 0개인 숫자는 출력하지 않는다.
#입력예 10 55 123 63 85 61 125 0

#cnt = [0 for i in range(10)]
#li=list(map(int,input().split()))

#for num in li:
#    cnt[num % 10] +=1

#for i in range(0,10):
#    if cnt[i] > 0 :
#        print("%d : %d개" % (i,cnt[i]))

# 자가진단3, 100미만의 정수 리스트를 입력받아 입력된 정수의 십의 자리 숫자가 각각 몇 개인지 작은 수부터 출력하는
#프로그램을 작성하시오. (0개인 숫자는 출력하지 않는다.)

cnt =[0 for i in range(10)]
li=list(map(int,input().split()))

for num in li:
    cnt[num//10] +=1

for i in range(10,-1,-1)