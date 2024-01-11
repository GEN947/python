# 숫자를 입력받아 처리하는 프로그램 작성
# 1. 숫자 추가
# 2. 숫자 출력
# 3. 합계
# 4. 숫자 삭제
# 999. 종료

numbers = []
while True:
    print("1. 숫자 추가, 2: 숫자 출력, 3: 합계, 4: 숫자 삭제, 5: 최댓값 - 최솟값, 999: 종료")
    input_number = input("값 입력: ")
    if input_number == "1":
        append_number = int(input("추가할 숫자 입력: "))
        numbers.append(append_number)
        print(f"추가한 숫자: {append_number}")
    elif input_number == "2":
        print(f"숫자: {numbers}")
        '''
        for number in numbers:
            print(number, end = ", ")
        print()     # 들여쓰기에 따라 어떻게 되는지 보는것도 낫뱃
        '''
    elif input_number == "3":
        print(f"{sum(numbers)}")
    elif input_number =="4":
        delete_number = int(input("삭제할 숫자 입력: "))
        if delete_number in numbers:
            numbers.remove(delete_number)
            print(f"삭제한 숫자: {delete_number}")
        else:
            print("현재 있는 숫자만 입력해주세요")
    elif input_number == "5":
        print(f"최댓값 - 최솟값 = {max(numbers)-min(numbers)}")
    elif input_number == "999":
        break
    else:
        print("메뉴 안의 숫자만 입력해주세요.")