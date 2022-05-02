#1
#a,b =input().split()
#a,b =int(a),int(b)
#if a >= b:
#    print(a-b)
#elif b >= a:
#    print(b-a)

#2
#a = int(input())
#if a == 0:
#    print("zero")
#elif a > 0:
#    print("plus")
#elif a < 0:
#    print("minus")

#3
#a = int(input())
#if a%4 == 0 and a%100 >0:
#    print("leap year")
#elif a%400 ==0:
#    print("leap year")
#else:
#    print("common year")

#4
#a = int(input("Number? "))
#if a == 1:
#    print('dog')
#elif a ==2:
#    print('cat')
#elif a ==3:
#    print('chick')
#else:
#    print("I don't know.")

#5
a =int(input())
if a == 2:
    print("28")
elif a == 1 or a ==3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("31")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")