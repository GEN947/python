"""
    1. 값 추가
    2. 리스트 출력
    999. 종료 메시지 출력 -> 종료
"""
user_list = []

while True:
    print("1. 값 추가")
    print("2. 리스트 출력")
    print("3. 리스트 합산")
    print("999. 종료")
    input_num = input("번호 입력: ")
    if input_num == "1":
        list_append = int(input("추가할 값 입력: "))
        user_list.append(list_append)
        print(f"{list_append}을(를) 리스트에 추가하였습니다.")
    elif input_num == "2":
        print(user_list)
    elif input_num == "3":      # 되게 해보자 -> 009.py에서 바로 해버렸고..
        for user_list in (user_list):
            user_list += int(user_list)
            print(user_list)
    elif input_num == "999":
        print("감사합니다.")
        break
    else:
        print("다른 번호를 입력해주세요.")

'''
# 강사님의 해설
user_list = []

while True:
    print("1. 값 추가")
    print("2. 리스트 출력")
    print("3. 리스트 합산")
    print("4. 리스트 평균")
    print("999. 종료")
    input_num = input("번호 입력: ")        # 이걸 숫자 말고 str로 처음부터 받고 아래에 if 조건문을 str로 받아도 된다.
    if input_num == "1":
        list_append = int(input("추가할 값 입력: "))
        user_list.append(list_append)
        print(f"{list_append}을(를) 리스트에 추가하였습니다.")
    elif input_num == "2":
        print(user_list)
    elif input_num == "3":
        print(f"합산: {sum(user_list)}")
    elif input_num == "4":
        print(f"입력값의 합계: {sum(user_list)/len(user_list)}")
    elif input_num == "999":
        print("감사합니다.")
        break
    else:
        print("다른 번호를 입력해주세요.")
'''