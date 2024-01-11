# 두 숫자를 입력받아 큰 수를 가리는 함수

def is_large(first_input_number:int, second_input_number:int):
    if first_input_number > second_input_number:
        return first_input_number
    elif first_input_number < second_input_number:
        return second_input_number
    else:
        print("다시 입력해주세요")

def abs_number(input_number:int):
    if input_number >= 0:
        return input_number
    return -input_number

def abs_number(input_number:int):
    if input_number >= 0:
        return input_number
    else:
        return -input_number