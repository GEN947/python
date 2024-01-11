# 주민등록번호를 입력받아 성별 출력

resident_registration_number = input("주민등록번호 입력: ")

if resident_registration_number[7] == "1" or resident_registration_number[7] == "3": # 문자열이기 때문에 조건도 문자열로 걸기
    print("남자/남성")
elif resident_registration_number[7] == "2" or resident_registration_number[7] == "4":
    print("여자/여성")
else:
    print("당신은 외계인입니까?") 

'''
resident_registration_number = input("주민등록번호 입력: ")

if resident_registration_number[7] in ("1", "3"):
    print("남자/남성")
elif resident_registration_number[7] in ("2", "4"):
    print("여자/여성")
else:
    print("당신은 외계인입니까?") 

# for문의 in과는 다른 것 resident_registration_number[7]이 문자열 "2", "4" 중 하나이느냐?
'''