# 정수 변수를 2개 만들어, 나눗셈 결과를 출력
# 예외 처리가 필요하면 예외 처리

try:
    print("양식: 첫번째 값 / 두번째 값")
    first_input_number = int(input("첫번째 값 입력: "))
    second_input_number = int(input("두번째 값 입력: "))

    divided_number = first_input_number / second_input_number
    print(divided_number)
except:
    print("0으로 나눌 수 없습니다.")