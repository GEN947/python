# 1, 값 추가, 2. 값 출력, 3. 삭제, 999. 종료

numbers = []

def add_value():
    input_number = int(input("추가할 값 입력: "))
    numbers.append(input_number)

def print_value():
    for item in numbers:
        print(item, end =" ")

def delete_value():     # 값 찾아 제거
    input_number = int(input("제거할 값 입력: "))
    if input_number in numbers:
        numbers.remove(input_number)
    else:
        print("존재하는 값만 입력해주세요")

# def delete_value():     # 위치 찾아 제거
#     index = 0
#     input_number = int(input("제거할 값 입력: "))
#     for item in numbers:
#         if item == input_number:
#             del numbers[index]
#         index += 1

while True:
    print("=============== 메뉴 선택 ===============")
    print("1, 값 추가, 2. 값 출력, 3. 값 제거, 999. 종료")
    input_select = input("번호 입력: ")
    
    if input_select == "1":
        add_value()
    elif input_select == "2":
        print_value()
    elif input_select == "3":
        delete_value()
    elif input_select == "999":
        print("이용해주셔서 감사합니다")
        break
    else:
        print("올바른 번호를 입력해주세요")