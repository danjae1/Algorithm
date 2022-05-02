#1
# #a =input()
# a=int(a)
# for i in range(a):
#     print("JUNGOL")

#2
# n1,n2 = input().split()
# n1,n2 = int(n1),int(n2)
# n1 <= 100, n2 <= 100
# if n1 > n2:
#     for i in range(n2,n1+1):
#         print(i,end=' ')
# if n2 > n1:
#     for i in range(n1,n2+1):
#         print(i,end=' ')
# if n1 == n2:
#     for i in range(n1,n2+1):
#         print(i)

#3
# a = int(input())
# sum= 0 
# for i in range(1,a+1):
#     if i%5 !=0:
#         continue
#     if i%5 ==0:
#         sum+=i   
# print(sum)

#4
# cnt =0
# sum=0
# a = list(map(int,input().split()))
# for x in a :
#     cnt +=1
#     sum +=x
# avg=float(sum/cnt)
# print('%.2f' % (avg))

#5
# even=0
# odd=0
# a =list(map(int,input().split()))
# for x in a:
#     if x%2 ==0:
#         even+=1
#         continue
#     if x%2 !=0:
#         odd+=1
# print('even :',even)        
# print('odd :',odd)

#6
# a,b= input().split()
# a,b = int(a),int(b)
# sum_= cnt =0
# a>0, b>0
# if a > b:
#     c = a
#     a = b
#     b = c
# for i in range(a,b+1):
#      if i%3 ==0 or i%5 ==0:
#         sum_+=i
#         cnt+=1
# avg= float(sum_/cnt)
# print('sum :',sum_)
# print('avg : %.1f' % (avg))

#7
# a = int(input())
# a >0
# for i in range(a,(a*10)+1,a):
#     print(i,end = ' ')

#8

#9

# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         print('(%d, %d)' % (i,j),end =' ')
#     print()

#10
# 부터 9까지의 정수a와 b를 입력받아 a단부터 b단까지의 구구단을 차례대로 출력하는 프로그램을
# 작성해라 구구단 사이의 공백은 3칸이다.
