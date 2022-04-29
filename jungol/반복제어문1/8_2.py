#100 이하의 정수를 입력받아 while 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성해라.
#입력예 10 
#출력예 55

a = input()
a = int(a)
b = 1
sum_ = 0
while b <= a:
    sum_ +=b
    b += 1
    

print(sum_)