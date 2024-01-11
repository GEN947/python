# 길이를 입력받아 센티미터 또는 인치로 변환해 출력
# 길이가 양수인 경우 "센티미터에서" 인치로 변환
# 길이가 음수인 경우 "인치에서" 센티미터로 변환
input_length = int(input("길이 입력: "))
result_length = None

if input_length > 0:
    result_length = input_length/2.54
    print(f"{result_length}inch")
elif input_length < 0:
    result_length = input_length*2.54
    print(f"{result_length}cm")
else:
    print("0은 입력할 수 없습니다.")

'''
input_length = int(input("길이 입력: "))
result_length = None

if input_length > 0:
    result_length = input_length/2.54
    print(str(result_length)+"inch")
elif input_length < 0:
    result_length = input_length*2.54
    print(str(result_length)+"cm")
else:
    print("0은 입력할 수 없습니다.")
'''

'''
input_length = int(input("길이 입력: "))

if input_length > 0:
    input_length = input_length/2.54
    print(f"{input_length}inch")
elif input_length < 0:
    input_length = input_length*2.54
    print(f"{input_length}cm")
else:
    print("0은 입력할 수 없습니다.")

'''

# 길이를 입력받아 센티미터 또는 인치로 변환해 출력
# 길이가 양수인 경우 인치로 변환
# 길이가 음수인 경우 센티미터로 변환
'''
input_length = int(input("길이 입력: "))

if input_length > 0:
    print(f"{input_length}inch")
elif input_length < 0:
    print(f"{input_length}cm")
else:
    print("0은 입력할 수 없습니다.")
'''
# scope: 변수를 사용할 수 있는 범위
# 블록이 스코프를 생성하는 언어: java       ex) if문 안에서 쓴 것과 그 밖에서 쓴 것을 혼용해서 쓰면 에러..? (chatgpt 도와줘요)
# 함수가 스코프를 생성하는 언어: python
'''
java 스타일

첫번째

input_length = int(input("길이 입력: "))
result_length = None

if input_length > 0:
    result_length = input_length/2.54
elif input_length < 0:
    result_length = input_length*2.54
else:
    result_length = 0
print(result_length)

result_length = None 실행문이 없었다면 이 전체 실행문은 맨 아래의 print(result_length) 실행문이 java에서 안 보였을 것이다.
즉, 에러가 났을 것이라는 것이다.

두번째

input_length = int(input("길이 입력: "))

if input_length > 0:
    result_length = input_length/2.54
    print(result_length)
elif input_length < 0:
    result_length = input_length*2.54
    print(result_length)
else:
    result_length = 0
    print(result_length)

print(result_length) 함수를 처음부터 모든 조건문에 다 넣는것이다 이러면 스코프가 블록인 java에게 어거지로 보여주면서 실행하게 하는것이다.

-----------------------------------------------------------------------------------------------------------------------------

python 스타일

input_length = int(input("길이 입력: "))

if input_length > 0:
    result_length = input_length/2.54
elif input_length < 0:
    result_length = input_length*2.54
else:
    result_length = 0
print(result_length)

파이썬 이녀석은 스코프가 넓기 때문에(?) 어떤 조건문에 있든 파이썬에게 result_length가 다 보인다.
즉 처음에 result_length = 0 이라는 실행문을 넣지 않아도 print(result_length)라는 실행문을 if 조건문마다 넣지 않아도 실행이 되는것이다.
'''