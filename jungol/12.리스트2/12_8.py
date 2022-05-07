# 20자 미만인 5개의 단어를 입력 받아 문자열 크기 순으로 정렬하여 출력하는 프로그램을 작성하시오.

# print("단어 5개를 입력하세요.")
# word=[]

# for i in range(5):
#     word.append(input().strip())

# for i in range(4):
#     for j in range(i+1,5):
#         if word[i] > word[j]:
#             word[i],word[j] = word[j],word[i]

# for a in word:
#     print(a)


word=[]

for i in range(5):
    word.append(input().strip())

for i in range(4):
    for j in range(i+1,5):
        if word[i] < word[j]:
            word[i],word[j] = word[j],word[i]

for a in word:
    print(a)