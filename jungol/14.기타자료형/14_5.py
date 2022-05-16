#예제5
#문자열을 입력받아 입력받은 문자열이 "사과"는 1번, "배"는 2번, "포도"는 3번
#그 외의 문자열이 입력되면 0번을 출력하는 프로그램을 작성하라.

# dic = {"사과":1, "배":2}
# dic["포도"] = 3
# a=input("문자열을 입력하시오: ").strip()

# if a in dic:
#     print("%d번" % dic[a])
# else:
#     print("0번")

#자가진단5
# 딕셔너리를 이용하여, "Pokemon"을 입력하면 "Pikachu","Digmon"을 입력하면 "Agumon","Yugioh"를
#입력하면 "Black Magician", 그 외의 문자열이 입력되면 "I don't know"를 출력하는 프로그램을 작성해라.

dic = {"Pokemon":"Pikachu","Digimon":"Agumon","Yugioh":"Black Magician"}

a=input().strip()

if a in dic:
    print(dic[a])
else:
    print("I don't know")
