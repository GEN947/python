# 몇일인지 입력 받아 몇개월 며칠인지 출력
# 333일 11개월 3일

input_days = int(input("몇일인지 입력하시오. "))

DAYS_PER_MONTH = 30
month = input_days//DAYS_PER_MONTH
days = input_days%DAYS_PER_MONTH

print(f"{month}개월 {days}일")

# 코드에 값이 직접 나타나는 것: literal
