#1 최대 100개의 정수를 차례로 입력받다가 -1이 입력되면 입력을 중단하고 -1을 제외한 마지막 
#세 개의 정수를 출력하는 프로그램을 작성하시오. (입력받은 정수가 3개 미만일 경우에는 모두 출력한다.)
#입력예 

# li=[]
# n=0
# for i in range(100):
#     li.append(int(input().strip()))
#     n+=1
#     if li[i]==-1:
#         if n <3:
#             print("%d" % (li[0]))
#             break
#         elif n < 4:
#             print("%d %d" % (li[0],li[1]))
#             break
#         else:
#             print("%d %d %d" % (li[-4], li[-3],li[-2]))
#             break

# 2 6명의 몸무게를 입력받아 평균을 출력하는 프로그램을 작성하시오. 풀력은 반올림하여 소수 첫째자리까지로 한다.
#입력예 23.2 39.6 66.4 50.0 45.6 48.0
#출력예 45.5

# weight=list(map(float,input().split()))
# cnt=0

# for i in weight:
#     cnt+=i

# avg = cnt / 6
# print("%.1f" % avg)

#3 6개의 문자리스트를 ['J','U','N','G','O','L']이라고 초기화한 후 문자 한 개를 입력받아 리스트에서의
# 위치를 출력하는 프로그램을 작성하시오. 첫 번째 위치는 0번이며 배열에 없는 문자가 입력되면
# none 이라는 메시지를 출력한다.

# li=['J','U','N','G','O','L']

# a =input().strip()
# flag=0

# for al in range(6):
#     if a ==li[al]:
#         print(al)
#     else:
#         flag+=1
# if flag==6:
#     print("none")

#4. 공백으로 구분하여 입력된 세자리 이하의 정수를 리스트로 받아서 입력된 최댓값과 최소값을 출력하는 
#프로그램을 작성하시오.
#입력예 45 19 123 58 10 -55 16 -1 999
#출력예  max : 123
#        min : -55

# a=list(map(int,input().split()))

# max_=0
# min_=1000

# for i in a:
#     if i > max_:
#         max_=i
#     if i < min_:
#         min_=i
# print("max :",max_)
# print("min :",min_)

#5. 100개 이하의 정수를 한 줄로 입력받아 입력된 정수 중 5의 배수의 개수와 합계, 평균을 출력하는 
# 프로그램을 작성하시오.
# 입력예 35 10 23 100 64 51 5
#Multiples of 5 : 4
# sum : 150
# avg : 37.5

# a =list(map(int,input().split()))
# m=0
# sum=0

# for i in a:
#     if i%5 ==0:
#         m+=1
#         sum+=i

# avg= sum/m
# print("Multiples of 5 :",m)
# print("sum :",sum)
# print("avg : %.1f" % avg)

#6. 100개 이하의 정수를 한 줄로 입력받아 입력 받은 개수를 출력한 후 입력받은 정수를 차례로 출력하되
# 그 수가 홀수이면 2배한 값을, 짝수인 경우에는 2로 나눈 몫을 출력하는 프로그램을 작성하시오.
#입력예 8 10 5 15 100
#출력예 5
#       4 5 10 30 50

# a=list(map(int,input().split()))
# n=len(a)

# print(n)
# for i in  a:
#     for j in range(n):
#         if a[j]%2 ==0:
#             print(a[j]//2,end=' ')
#         else:
#             print(a[j]*2,end=' ')
#     break       




#7 20이하의 정수 n을 입력받고 n명의 점수를 입력받아 높은 점수부터 차례로 출력하는 프로그램을 작성하시오.
# 입력예 5
#35 10 35 100 64
# 출력예 100
#64
#35
#35
#10

# a=input()
# a=int(a)
# b=list(map(int,input().split()))

# for i in range(a-1):
#     for j in range(i+1,a):
#         if b[i] >b[j]:
#             b[i],b[j]=b[j],b[i]

# for p in b[::-1]:
#     print(p)
        
# "flower","rose","lily","daffodil","azalea" 5개의 단어를 초기화한 후 한 개의 문자를 입력받아서
# 입력받은 문자가 두 번쨰나 세 번쨰에 포함된 단어를 모두 출력하고 마지막 줄에 출력한 단어의 개수를
# 출력하는 프로그램을 작성하시오. (해당되는 단어가 없으면 0만 출력한다.) 
# 입력예 l
# 출력예 flower
#        lily
#        2

# li =["flower","rose","lily","daffodil","azalea"]

# a=input().strip()
# flag=0
# n=0
# for word in li:
#     if word[1] == a:
#         print(word)
#         flag=1
#         n+=1
#     elif word[2] ==a:
#         print(word)
#         flag=1
#         n+=1
# if flag ==0:
#     print("0")
# if n !=0:
#     print(n)

#9. 단어를 입력받다가 "0"을 입력 받으면 입력을 종료하고 그 떄까지 입력받은 단어의 개수와 "mo"가
#들어간 단어를 모두 출력하는 프로그램을 작성하시오.
#입력예            출력예
#keyboard            3
#mouse              mouse
#monitor            monitor
#0

# li=[]
# flag=0
# m="mo"
# l=len(li)
# while True:
#     ch=input()
#     li.append(ch.strip())
#     if ch == '0':
#         break



#10. 5개의 단어를 입력받은 후 문자와 문자열을 한 개씩 입력받아 나중에 입력받은 문자나 문자열이 포함된
# 단어를 모두 출력하는 프로그램을 작성하시오. (입력되는 단어나 문자열의 길이는 100자 이하이고, 찾는
# 단어가 없으면 "none"라고 출력한다.)

li=[]

for i in range(7):
    li.append(input().strip())

for j in li:
    if li[0] == li[6]:
        print(li[j])