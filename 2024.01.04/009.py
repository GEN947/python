# 숫자를 입력받아 1의 자리까지 버리고 출력

input_number = int(input("숫자 입력: "))
calculated_number = input_number//10*10

print(f"{input_number}을(를) 1의자리에서 내림하면 {calculated_number}입니다.")

input_number = int(input("숫자 입력: "))
rem_number = input_number % 10
calculated_number = input_number-rem_number
# 35번과 36번을 합친다 -> calculated_number = input_number-input_number % 10
print(f"{input_number}을(를) 1의자리에서 내림하면 {calculated_number}입니다.")

