# 숫자를 입력받아 양수, 음수, 0을 출력
input_number = int(input("숫자 입력: "))

if input_number > 0:
    print("양수")
elif input_number < 0:
    print("음수")
else:
    print("0")

'''
# 이건 숫자를 양수, 음수, 0로 바꿔 출력하는거..
input_number = int(input("숫자 입력: "))
positive_number = 0
negative_number = 0
ZERO = 0

if input_number > 0:
    positive_number = input_number
    negative_number = -input_number
    print(f"양수: {positive_number}, 음수: {negative_number}, {ZERO}")
elif input_number < 0:
    positive_number = -input_number
    negative_number = input_number
    print(f"양수: {positive_number}, 음수: {negative_number}, {ZERO}")
else:
    print("숫자는 0입니다.")
'''

# 점수를 입력받아 70~90점이면 "추천 대상", 아니면 "대상 아님"

input_score = int(input("숫자 입력: "))

if input_score >= 70 and input_score <= 90: # if 70 <= input_score <= 90:
    print("추천 대상")
else:
    print("대상 아님")