# scope: 변수의 사용 범위, 파이썬은 함수 스코프

x = 10

def func1():
    x = 30
    print(f"함수 안에서: {x}")

print(f"함수 밖에서: {x}")
func1()

while True:
    print(10)
    