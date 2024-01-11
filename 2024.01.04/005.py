# slicing
any_list = [10, 20, 30, 40, 50]
# 리스트[시작인덱스: 끝인덱스+1]
print(any_list[0:1])
print(any_list[2:4])

# slicing은 문자열도 가능
string = "0123456"
print(string[1:3])
print(string[2:5])

# 간격지정
print(string[:]) # 처음부터 끝까지
print(string[3:]) # 3번째(사실상 4번째)부터 끝까지
print(string[3::3]) # 3부터 "3"찍고 3 건너뛴 숫자 찍기
print(string[1::2])
  
# 프로필 업로드 문제
# aaaa.png라고 유저가 썼을때 확장자는 바꾸지 않고 이름만 바꾸기