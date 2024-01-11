# 원시타입, 내장함수 <-> import, pip
# 개발자는 값을 검증

# string 타입
str1 = "10"
str2 = "3.14"
str3 = "홀짝홀짝홀짝홀짝"

# 연산
print(str1+str2)    # 연결
print(str1*10)      # 반복

# 인덱스 연산 -> 시퀀스와 동일
print(str3[0])
print(str3[5])

# 슬라이싱(slicing) 연산 -> 시퀀스와 동일
print(str3[0:3])

str4 = "72568"
print(str4[2:])
print(str4[::2])    # [시작위치:끝위치+1:간격]      제발 끝위치+1이라는거 잊지 말자...

str5 = "0123456789"
# 홀수만 출력           13579
print(str5[1::2])

# 3의 배수만 출력       0369
print(str5[::3])

# 내장함수: len
# 길이라는 것은 집합(sequence)이어야 한다.
print(len("hello"))

# 문자열은 변경불가능 (immutable <-> mutable)
str6 = "hello"
# str6[3] = "h"       주석 걸어놓은 이유는 실행하면 에러 나니까..
list6 = ["h", "e", "l", "l", "o"]
list6[3] = "z"


str11 = "hello"
str11 = str11 + " python"
print(str11)
# str은 변경 불가능하다 했는데 위의 실행문은 왜 될까? -> chatgpt..
# 변수 공간에 변수를 저장하는거기 때문에?