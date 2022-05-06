# a=input().strip()

# for i in a:
#     print(i, end=' ')

#문자열을 하나 입력받아, 문자 사이사이에 쉼표(,)를 넣어 출력하는 프로그램을 작성해라.
#입력예 Jungbo Olympiad
#출력예 J,u,n,g,b,o, ,O,l,y,m,p,i,a,d

a = input().strip()
len_=len(a)
for i in range(len_-1):
    print(a[i],end=',')
print(a[len_-1])

