# 나이를 입력받아 성년 또는 미성년 출력

def is_adult():
    input_age = int(input("나이 입력: "))

    if input_age >= 18:
        return True
    else:
        return False

if is_adult() == True:
    print("당신은 출입가능합니다")