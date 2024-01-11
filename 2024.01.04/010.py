# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
# 23->21 21->21
input_number = int(input("숫자 입력: "))
calculated_number=input_number//7*7
print(calculated_number)

'''
input_number = int(input("숫자 입력: "))
quo_number=input_number//7
calculated_number=quo_number*7
print(calculated_number)
'''
'''
input_number = int(input("숫자 입력: "))
rem_number=input_number%7
calculated_number = input_number-rem_number
print(calculated_number)
'''

# 자연수를 입력받아 그 숫자보다 작은 최대 7의 배수
input_number = int(input("숫자 입력: "))
calculated_number = (input_number-1)//7*7
print(calculated_number)
