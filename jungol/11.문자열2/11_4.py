# a=input().strip()
# b=input().strip()

# if a>b:
#     print(a)
# else:
#     print(b)

#세 문자열을 입력받아서, 세 문자열이 사전순으로 정렬되어 있으면 'YES'
# 아니면 'NO'를 출력하는프로그램을 작성하라
#Elbow
#Elegant
#Elephant
a=input().strip()
b=input().strip()
c=input().strip()

if a<b :
    if b<c or c>b:
        print("YES")
elif a<c:
    if c<b or c>b:
        print("YES")
elif a>b or a>c:
    print("NO")