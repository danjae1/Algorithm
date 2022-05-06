# #10명의 컴퓨터 성적 리스트를 입력받아 배열에 저장하고 총점과 평균을 구하여 출력하는 프로그램을 작성
# #하시오. (평균은 반올림하여 소수 첫쨰자리까지 출력한다.)
# #입력예 95 100 88 65 76 89 58 93 77 99
# #출력예 총점 840
# #       평균 84.0

# a =list(map(int,input().split()))
# sum=0

# for i in a:
#     sum+=i

# avg=sum/10
# print("총점 = ",sum)
# print("평균 = ",avg)

# 10개의 정수 리스트를 입력받아 짝수 번째 입력된 값의 합과 홀수 번째 입력된 값의 평균을 출력하는
# 프로그램을 작성하시오. 평균은 반올림하여 소수 첫째자리까지 출력한다
#입력예 95 100 88 65 76 89 58 93 77 99
#입력예 0   1  2  3  4  5  6  7  8  9
#출력예 sum: 446
#       avg:78.8
a=list(map(int,input().split()))
evensum=0
oddsum=0
for i in a[1:11:2]:
    evensum+=i
for j in a[0:11:2]:
    oddsum+=j    
avg=oddsum/5
print("sum :",evensum)
print("avg :",avg) 

