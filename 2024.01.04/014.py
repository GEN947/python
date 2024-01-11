# 1900년대생은 일곱번째자리 1, 2 / 2000년대생은 일곱번째자리 3, 4
resident_registration_number = input("주민등록변호 입력: ")

if resident_registration_number[7] == "1" or resident_registration_number[7] == "2":
    birth_year = "19"+resident_registration_number[0:2]
    print(f"태어난 년도: {birth_year}년")
elif resident_registration_number[7] == "3" or resident_registration_number[7] == "4":
    birth_year = "20"+resident_registration_number[0:2]
    print(f"태어난 년도: {birth_year}년")
else:
    print("당신은 외계인입니까?")

'''
resident_registration_number = input("주민등록변호 입력: ")

if resident_registration_number[7] in ("1", "2"):
    birth_year = "19"+resident_registration_number[0:2]
    print(f"태어난 년도: {birth_year}년")
elif resident_registration_number[7] in ("3", "4"):
    birth_year = "20"+resident_registration_number[0:2]
    print(f"태어난 년도: {birth_year}년")
else:
    print("당신은 외계인입니까?")
    
-----------------------------------------------------------------------------------------------------------------------------

java 스타일 

resident_registration_number = input("주민등록변호 입력: ")
birth_year = 0

if resident_registration_number[7] == "1" or resident_registration_number[7] == "2":
    birth_year = "19"+resident_registration_number[0:2]
    print(f"태어난 년도: {birth_year}년")
elif resident_registration_number[7] == "3" or resident_registration_number[7] == "4":
    birth_year = "20"+resident_registration_number[0:2]
    print(f"태어난 년도: {birth_year}년")
else:
    print("당신은 외계인입니까?")
'''