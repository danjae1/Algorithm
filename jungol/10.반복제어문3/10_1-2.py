#한 줄에 두 문자를 입력받아서, 앞 문자의 아스키코드부터 뒤 문자의 아스키코드까지 순서대로 순회하면서 모든 문자를
#출력하는 프로그램을 작성하시오. 앞 문자의 아스키코드가 뒤 문자의 아스키코드보다 클 수도 있음에 주의하시오.



# a,b=input().split()
# a,b=str(a),str(b)
# for i in range(ord(a),ord(b)+1):
#    if ord(a)>=ord(b):
#        for j in range(ord(a),ord(b)+1,-1):
#            print(chr(j),end=' ')
#    else:
#        print(chr(i),end=' ')




a,b=input().split()
a,b=str(a),str(b)

if ord(a)>=ord(b):
    for i in range(ord(a),ord(b)-1,-1):
        print(chr(i),end=' ')
else:
    for i in range(ord(a),ord(b)+1):
        print(chr(i),end=' ')


      
      




