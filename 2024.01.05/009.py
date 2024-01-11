list1 = [15, 20, 30, 90]

# list1의 길이 출력 -> len() 쓰지 말고
a = 0
for x in list1:
    a += 1
print(a)

# list1의 합계 출력 -> sum() 쓰지 말고
b = 0
for x in list1:
    b += x
print(b)

# list1의 평균(합계/개수) 출력
list1 = [15, 20, 30, 90]
hap = 0
cnt = 0
avg = 0

for i in list1:
    hap += i
    cnt += 1
avg = hap/cnt
print(avg)

