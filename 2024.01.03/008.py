user_name = input("이름 입력: ")
user_nai = input("나이 입력: ")

print(type(user_name))
print(type(user_nai)) 
# 사용자가 입력받은 값의 타입은 무조건 문자열이다. (다른 언어들도 그럼)
user_nai = int(user_nai)
