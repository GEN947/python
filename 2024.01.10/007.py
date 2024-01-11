# 1에서 10까지 합계
y = 0
for x in range(1,11):
    y += x
print(y)

# 1에서 10까지의 3의 배수 출력
for i in range(1,11):
    if i %3 == 0:
        print(i)
    else:
        pass        # "아무것도 하지 말고 지나가라"

for i in range(1,11):
    if i %3 != 0:
        continue    # 현재 반복을 중단하고 다음 반복으로 이동
    print(i)

# 1에서 10사이의 3의 배수 합계
y = 0

for i in range(1,11):
    if i % 3 == 0:
        y += i
        continue
print(y)

# 1에서 100 사이의 3과 5의 공배수 출력
y = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        y += i
        print(i, " ")
        continue
print(y)

# 1에서 100 사이의 5과 7의 공배수 출력
y = 0

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        y += i
        print(i, " ")
        continue
print(y)

# 1에서 100사이의 5의 배수와 7의 배수 출력 단 공배수 제외

for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        if i % 35 != 0:
            print(i, end = " ")
            continue

for i in range(1,101):
    if (i % 5 == 0 or i % 7 == 0) and i % 35 != 0:
        print(i, end = " ")
        continue

for i in range(1,101):
    if i % 5 == 0 and i % 7 == 0:
        continue
    if i % 5 == 0 or i % 7 == 0:
        print(i, end = " ")