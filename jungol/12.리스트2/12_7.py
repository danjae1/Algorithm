#5개의 정수 리스트를[95,75,85,100,50]로 초기화하고 오름차순으로 정렬하여 출력하는 프로그램을
#작성하시오.
#출력예 50 75 85 95 100

# a = [95,75,85,100,50]
# for i in range(4):
#     for j in range(i + 1,5):
#         if a[i] >a[j]:
#             a[i],a[j] = a[j],a[i]

# for i in range(5):
#     print(a[i], end=' ')

#0 1 2 3 4 5

# 10개의 정수를 입력받아 내림차순으로 정렬하여 출력하시오.
#입력예 95 100 88 65 76 89 58 93 77 99
#출력예 100 99 95 93 89 88 77 76 65 58

a=list(map(int,input().split()))

for i in range(9):
    for j in range(i+1,10):
        if a[i]<a[j]:
            a[i],a[j] = a[j],a[i]
for i in range(10):
    print(a[i],end=' ')