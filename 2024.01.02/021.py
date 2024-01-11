# 섭씨를 입력 받아 화씨로 출력
# (n°C * 9/5) + 32 = m°F
'''
input_celsius = int(input("섭씨 입력: "))

fahrenheit = (input_celsius*9/5) + 32

print(f"{input_celsius}°C는 {fahrenheit}°F")
'''
# 온도와 종류를 입력받으시오.
# ex) 온도: 35
# ex) 종류: 화씨
# 종류가 섭씨면 화씨로 변환 / 화씨면 종류로 변환
# n°C = 5/9(m°F - 32)

input_temperature = int(input("온도 입력: "))
input_type_temperature = input("종류 입력: ")
if input_type_temperature == "섭씨":
    celsius = input_temperature
    fahrenheit = (celsius*9/5) + 32
    print(f"{celsius}°C는 {fahrenheit}°F")
elif input_type_temperature == "화씨":
    fahrenheit = input_temperature
    celsius = 5/9*(fahrenheit - 32)
    print(f"{fahrenheit}°F는 {celsius}°C")
else:
    print("섭씨와 화씨중 하나만 고르시오.")
    
'''
if input_type_temperature == "섭씨":
    celsius = input_temperature
    fahrenheit = (celsius*9/5) + 32
    print(f"{celsius}°C는 {fahrenheit}°F")
else:
    if input_type_temperature == "화씨":
        fahrenheit = input_temperature
        celsius = 5/9*(fahrenheit - 32)
        print(f"{fahrenheit}°F는 {celsius}°C")
    else:
        print("섭씨와 화씨중 하나만 고르시오.")
'''