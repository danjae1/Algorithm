#예제2 1부터 10까지의 정수를 한 줄로 입력받아 1번 이상 입력된 각 숫자의 개수를 작은 수부터 출력하는 프로그램을 작성하시오.

#cnt = [0 for i in range(11)]
#lst = list(map(int,input().split()))

#for num in lst:
#    cnt[num] +=1   

#for i in range(1,11):
#    if cnt[i] > 0 :
#        print("%d : %d개" % (i,cnt[i]))

#a=list(map(int,input().split()))

#for i in range(1,11):
#    cnt=a.count(i)
#    if cnt >0:
#        print("%d : %d개" % (i,cnt))

#자가진단2, 영문 대문자를 한 줄로 입력받아 1번 이상 입력된 각 문자의 개수를 사전 순으로 출력하는 프로그램을 작성하시오.


a= list(map(str,input().split()))

for i in range(1,27):
    cnt =a.count(chr(i))
    if cnt>0:
        print("%d : %d" % (chr(i),cnt))