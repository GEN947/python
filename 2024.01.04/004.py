any_list = [10, 20, 30, 40]

len(any_list) # .append와 달리 다른 것들도 다 len 함수 써서 길이를 잴 수 있기 때문에 len() 함수 사용 가능 (chatgpt 도와줘요 !)

# len 쓰지 말고 길이 측정
length = 0
for item in any_list:
    length += 1
print(length)