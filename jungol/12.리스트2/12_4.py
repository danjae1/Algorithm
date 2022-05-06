# lst= list(map(int,input().split()))
# max_=0

# for a in lst:
#     if a>max_:
#         max_=a
# print(max_)

a = list(map(int,input().split()))
min_=a[1]

for b in a:
    if b<min_:
        min_=b
print(min_)