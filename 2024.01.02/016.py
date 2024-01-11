# 숫자 2개를 입력받아 다음과 같이 출력
# ex) 3과 8의 합은 11, 곱은 24

num1 = int(input("첫번째 수 입력: "))
num2 = int(input("두번째 수 입력: "))
sum1 = num1 + num2
mul1 = num1 * num2

print(f"{num1}와(과) {num2}의 합은 {sum1}, 곱은 {mul1}입니다.")

# 숫자 2개를 입력 받아 큰 수와 작은 수 출력
# ex 5와 8중 큰 수는 8, 작은 수는 5

num1 = int(input("첫번째 수 입력: "))
num2 = int(input("두번째 수 입력: "))
max = max(num1, num2)
min = min(num1, num2)

print(f"{num1}와(과) {num2}중 큰 수는 {max}, 작은 수는 {min}")
# 이름 겹쳐서 좀 그렇다.. large와 small 정도면 괜찮지 않았을까..