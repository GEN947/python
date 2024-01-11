# 임의로 가정
# 남자의 적정체중은 키-100, 여자의 적정체중은 키-105
# 키를 입력받아 적정체중을 출력하시오

input_gender = input("성별 입력: ")
input_height = int(input("키 입력: "))

if input_gender == "남자" or input_gender == "남성":
    appropriate_weight = input_height - 100
    print(f"적정체중: {appropriate_weight}")
elif input_gender == "여자" or input_gender == "여성":
    appropriate_weight = input_height - 105
    print(f"적정체중: {appropriate_weight}")
else:
    print("올바른 성별만을 입력하시오")