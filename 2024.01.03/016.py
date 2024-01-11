# 숫자를 입력받아 음수면 양수로 바꿔 출력

num = int(input("숫자 입력: "))

if num <0:
    print(-num)
# chatgpt 물어보기
    
# 길이를 입력받아 센티미티면 인치로, 인치면 센티미터로 변경
# 센티미터 = (인치값) * 2.54
# 인치 = 100/254*(센티미터값)
    

value_length = float(input("길이 입력: "))
type_length = input("종류 입력: ")
changed_value = 0

if type_length == "cm":
    changed_value = value_length*100/254 # value_length/2.54
    print(f"{value_length}cm는 {changed_value}inch입니다.")
elif type_length == "inch":
    changed_value = value_length*2.54
    print(f"{value_length}inch는 {changed_value}cm입니다.")
else:
    print("cm, inch 중 하나만 입력하시오")


'''
value_length = float(input("길이 입력: "))
type_length = input("종류 입력: ")
changed_value = 0
CONSANT_VALUE = 2.54

if type_length == "cm":
    changed_value = value_length/CONSANT_VALUE
    print(f"{value_length}cm는 {changed_value}inch입니다.")
elif type_length == "inch":
    changed_value = value_length*CONSANT_VALUE
    print(f"{value_length}inch는 {changed_value}cm입니다.")
else:
    print("cm, inch 중 하나만 입력하시오")
'''
