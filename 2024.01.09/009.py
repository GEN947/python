# 숫자 리스트 - 추가, 출력, 변경, 삭제

numbers = []

def print_menu():
    print("=============== 메뉴 선택 ===============")
    print("1, 값 추가, 2. 값 출력, 3. 삭제, 999. 종료")

def input_select():
    return input("번호 입력: ") # 결과를 input_select에 넣은거다

def add_value():
    value = int(input("추가할 값 입력: "))
    numbers.append(value)

def list_numbers():
    for num in numbers:
        print(num, end=", ")
    print()

def delete_numbers():
    value = int(input("제거할 값 입력: "))
    numbers.remove(value)

def finish():
    print("이용해주셔서 감사합니다. ")

while True:
    print_menu()
    select = input_select()
    if select == "1":
        add_value()
    elif select == "2":
        list_numbers()
    elif select == "3":
        delete_numbers()
    elif select == "999":
        finish()
        break