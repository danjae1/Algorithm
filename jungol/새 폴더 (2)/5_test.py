#a = [-1,-2,-3,-4,-5]
#print(a)

#2 

#3
#a,b = input("Input? ").split()
#c,d = input("Input? ").split()
#e,f = input("Input? ").split()
#g,h = input("Input? ").split()
#color = [a,c,e,g]
#ani = [b,d,f,h]
#print("Color:",color)
#print("Animal:",ani)

#4
#a = input().strip()
#b = list(a)
#print(b[::-1])

# 5 한 줄에 리스트를 입력 받아, 3의 배수 (3,6,9...)번째 원소들만 골라서 리스트로 출력하는 프로그램을 작성하라.
# li = []
# a = input().split()
# li=list(a) 
# print(a[2::3])


# 6 공백을 사이에 두고 리스트를 입력 받아, 끝에서 두 번쨰 원소부터 앞에서 두 번째 원소까지 역순으로된 리스트를 출력하는 프로그램을 작성하라.
# 단 입력되는 한 줄에는 공백이 4개 이상이다.

li = []
a =str(input()).split()
li =list(a)
print(a[-2:0:-1])