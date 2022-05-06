# # 4자리 이하의 10개의 정수를 입력받아 짝수 중 가장 큰 값과 홀수 중 가장 작은 값을 출력하는 프로그램을
# #만드시오.
# #입력예 5 10 8 55 6 31 12 24 61 2
# #출력예 31 12

# a =list(map(int,input().split()))
# max_,min_ = -10000,10000

# for num in a:
#     if num %2 == 0:
#         if num > max_: max_ = num
#     else:
#         if num <min_ : min_ = num

# print("%d %d" % (min_,max_))

# 10개의 정수를 입력받아 100미만의 수 중 가장 큰 수와 100이상의 수 중 가장 작은 수를 출력하는
# 프로그램을 만드시오. (입력되는 정수의 범위는 1이상 10000미만이다. 만약 해당하는 수가 없을
# # 때에는 100을 출력한다.)
#입력예 88 123 659 15 443 1 99 313 105 48
#출력예  99 105
a=list(map(int,input().split()))
max_,min_ =0,10000

for num in a:
    if num <100:
        if num >max_:
            max_ = num
    elif num >100:
        if num <min_:
            min_ = num 
if max_==0:
        max_=100
if min_==10000:
        min_=100
            
       
print("%d %d" % (max_,min_))

#152 872 95 282 57 784 771 61 826 66
#445 292 171 496 116 862 926 622 248 928