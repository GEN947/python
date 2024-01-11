# 숫자 타입 -> 타입마다 사용할 수 있는 연산, 함수가 다르다
# 산술 연산: +, -, *, /

# 10과 3.14 변수 / 결과 출력 (한줄로)
num1, num2 = 10, 3.14

print(f"""
{num1} + {num2} = {num1+num2}, {num1} - {num2} = {num1-num2},
{num1} * {num2} = {num1*num2}, {num1} / {num2} = {num1/num2}
""")

print(
    f"{num1} + {num2} = {num1+num2}, "
    f"{num1} - {num2} = {num1-num2}, "
    f"{num1} * {num2} = {num1*num2}, "
    f"{num1} / {num2} = {num1/num2}, "
)


num2 = 3
print(f"몫: {num1//num2}")
print(f"나머지: {num1 % num2}")

print(-num1)

# 함수: 이름을 가진 기능 -> 재사용, 내장함수(import X)
abs     # 절댓값
print(abs(-100))
print(abs(100))

