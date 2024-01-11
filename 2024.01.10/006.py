# for문
# hello를 for를 이용해 3번 출력

for x in (1,2,3):
    print("hello")

for x in range(3):
    print(x)

# for를 이용해서 0부터 10까지 출력
for x in range(11):
    print(x)

# for를 이용해서 0부터 10까지 짝수만 출력
for x in range(11):
    if x % 2 == 0:
        print(x)
    else:
        pass

# 1부터 10까지의 합계를 출력

y = 0
for x in range(1,11):
    y += x
print(y)