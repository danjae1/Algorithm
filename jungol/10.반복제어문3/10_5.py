#for i in range(1,6):
#    print(' ' * (5-i) + '*'* (i*2-1))


a= int(input())
for i in range(a,0,-1):
    print((' '*(a-i)) + ("*"*(i*2-1)))