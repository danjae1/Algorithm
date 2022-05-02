#for i in range(ord('A'), ord('E') + 1):
#   print(chr(i),i)

#ord() 문자-> 아스키코드값 반환
#chr() = ord()의 역연산 chr()에서 정수 아스키코드값을 넣으면 문자 반환.

#'A'부터 'Z'까지 문자를 한 줄에 출력하는 프로그램을 작성하시오.


for i in range(ord('A'),ord('Z')+1):
    print(chr(i),end='')