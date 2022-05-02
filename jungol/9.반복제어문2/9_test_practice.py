# 행과 열의 수를 입력받아 다음과 같이 출력하는 프로그램을 만드시오.
# 입력예 3 4
# 출력예 1 2 3 4
# 출력예 2 4 6 8
# 출력예 3 6 9 12

# for a in range(1,13):
#     for j in range(3,7):
#         print('%d %d' % (j,a),end=' ')
#     print()


a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        print('(%d, %d)' % (i,j),end =' ')
    print()

    

