# 13-4 예제
#fibo = [0 for i in range(41)]
#fibo[1] = fibo[2] = 1
#for i in range(3,41):
#    fibo[i] = fibo[i-1] + fibo[i-2]

#for i in range(10,41,10):
#    print("피보나치 수열 %d항 : %d" % (i,fibo[i]))

#자가진단4 100이하의 자연수를 입력받아 첫 번째 항은 100으로 두 번째 항은 입력받은 수로 초기화하고
#다음항부터는 전전항에서 전항을 뺀 수로 채워나가는 수열을 작성하여 그 수가 음수가 나올 때까지 출력하는 프로그램을 작성하시오.
# 입력예 62
# 출력예 100 62 38 24 14 10 4 6 -2

a=input().strip()
a=int(a)
fibo = [0 for i in range(101)]
fibo[1] = 100
fibo[2] = a
for i in range(3,101):
   fibo[i] = fibo[i-2] - fibo[i-1]
   if fibo[i]<0:
       break

for i in range(1,101):
   print(fibo[i],end=' ')
   if fibo[i] <0:
       break


