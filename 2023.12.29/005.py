# 파이썬은 타입을 바꿀 수 있고, 어떤 경우는 파이썬이 알아서 바꾸는 경우도 있다.

# int, float, bool, str

# 타입을 바꾸는 함수는 타입의 이름과 같다.
print(type("3"))
print(type(int("3")))

print(3+int('3'))

print(3+float('3.14'))
# 실수는 무수히 많기 떄문에 컴퓨터가 모든 실수를 저장할 수가 없다 / 즉, 근사값으로 처리하게 된다.

print('3'+'3')
print('5'+str(5))

print('당신은 성인입니까? ' + str(True))

print(bool('당신은 성인입니까? ') + True)
print(bool('당신은 성인입니까? ') + False)
print(True+True)