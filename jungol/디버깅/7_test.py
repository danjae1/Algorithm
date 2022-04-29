#a= 5
#a += 10
#a = a-1 #-----------------------
#print(1) #여기에서 출력될 1을 위치애서의 a값으로 바꾸어준다.


import time
now = time.localtime()
a=0
a = now.tm_year-1900 # 1
a += now.tm_mon-1 #2
a += now.tm_mday
print(0,122,152) #3