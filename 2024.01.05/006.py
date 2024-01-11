list1 = [1,3,5]

# 10 in list1: 결과가 참거짓(list1 안에 10이 들었니?)

# list1의 원소를 하나씩 꺼내 item에 담는 반복문
for item in list1:
    print(item)
# 위 같은 경우는 list1의 첫번째인 1을 꺼내 item에 담은 후 print(item) 실행 / list1의 두번째인 3을 꺼내 item에 담은 후 print(item) 실행 ...
    
# while 종료조건
index = 0
while index<3:
    print(list1[index])
    index += 1