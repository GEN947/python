# f문자열
# replace: 치환

str4 = "010-1111-2222"
# 함수: 소속 없는 함수 + 소속 있는 메소드
print(len(str4))

# method: 특정 타입 소속 -> 타입은 함수도 가질 수 있다.
# 문자열 메소드는 새로운 문자열을 만든다
# method도 함수다....
str4.replace("-", ".")       # replace는 멤버 연산자 / 즉, 문자열 함수에 소속 돼있다
print(str4)                 # 문자열은 immutable이기 때문에....

# 비유로 설명하면 문자열은 tv와 리모컨으로 보면 된다
# "가리킨다" 라는 표현 잊지 말기

str4 = str4.replace("-", ".")        # immutable이기 때문에 변수를 하나 더 만들면 된다
print(str4)

# 원래 값은 안 바뀌는건데 (변수를 하나 더 만들어서) 대입한거다

str4 = str4.replace("1111", "xxxx")
print(str4)

# 주민등록번호 "987545-2312342"
jumin = "987545-2312342"

jumin = jumin.replace(jumin[8:], "*"*6)
# jumin = jumin[:-6] + "*"*6
# jumin = jumin.replace(jumin[8:], "******")
print(jumin)

str5 = "         aa            a    a       "
# 앞 뒤 공백은 쓸데 없는 공백이라 인식하고 없앰, 안쪽의 공백은 내용이라 인식하고 없애지 않음
print(str5.strip())
