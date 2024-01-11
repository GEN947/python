numbers = [100, 300, 500, 700]

# 값을 입력받아 위치를 찾아 삭제

value = 500
index = 0

for num in numbers:
    if value == num:
        del numbers[index]
    index += 1

for item in numbers:
    print(item, end = " ")