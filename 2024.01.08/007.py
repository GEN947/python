# 숫자를 입력받아 CR(합계, 평균)UD

# 메뉴를 띄운다 (1: 숫자 추가, 2: 숫자 출력, 999: 종료)
# 어떤 걸 만들든 while문은 종료문부터 만든다.
numbers = []
while True:
    print("========== 메뉴 선택 ==========")
    print("(1: 추가, 2. 현재 값 출력: 3: 합계 출력, 4: 평균 출력, 5: 삭제, 999: 종료)")
    input_number = input("번호 입력: ")
    if input_number == "1":
        append_number = int(input("추가할 값 입력: "))
        numbers.append(append_number)
        print(f"{append_number}을(를) 추가하였습니다.")
    elif input_number == "2":
        print(f"{numbers}")
    elif input_number == "3":
        print(f"합계: {sum(numbers)}")
    elif input_number == "4":
        print(f"평균: {sum(numbers)/len(numbers)}")
    elif input_number == "5":
        delete_number = int(input("삭제할 값 입력: "))
        if delete_number in numbers:
            numbers.remove(delete_number)
            print(f"{delete_number}을(를) 삭제하였습니다")
        else:
            print("현재 있는 값만 입력해주세요")
    elif input_number == "6":
        abs(max(numbers)) - abs(min(numbers))
    elif input_number == "999":
        print("이용해주셔서 감사합니다")    
        break
    else:
        print("메뉴에 있는 번호만 입력해주세요")
    