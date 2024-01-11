# 초를 입력 받아 몇분 몇초인지 출력
# ex) 210초 -> 3분 30초
'''
input_seconds = int(input("초 입력: "))

minutes = input_seconds//60
seconds = input_seconds%60

print(f"{minutes}분 {seconds}초")
'''
# 분과 초를 입력하면 초를 출력
'''
input_minutes, input_seconds = int(input("분 입력: ")), int(input("초 입력: "))

minutes = input_minutes*60
seconds = input_seconds
total_seconds = minutes + seconds

print(f"{total_seconds}초")
'''

input_minutes, input_seconds = int(input("분 입력: ")), int(input("초 입력: "))

SECONDS_PER_MINUTES = 60  # 상수는 대문자로 (모든 언어가 그럼..)
minutes = input_minutes*SECONDS_PER_MINUTES
seconds = input_seconds
total_seconds = minutes + seconds

print(f"{total_seconds}초")
