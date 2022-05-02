#a = ord('A')
#n =int(input())

#for i in range(1, n+1):
#    for j in range(i):
#        print(chr(a),end='')
#        a+=1
#    print()

a= ord('A')
n=int(input())

for i in range(n,0,-1):
    for j in range(i):
        print(chr(a),end='')
        a+=1
    print()