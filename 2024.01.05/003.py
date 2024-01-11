# jumin = input("주민등록번호 입력: ")
# gender = jumin[7]

# # 남자인지 여자인지
# if gender == "1" or "3":
#     print("남자")
# elif gender == "2" or "4":
#     print("여자")

# # 둘 중의 하나 if문을 한줄로 -> 삼항연산자
# # 복잡한 조건 삼항연산은 쓰지 말자 (스파게티 코드 되버린다..)
# "남자" if gender == "1" else "여자"

# '''
# if gender == 1:

# else:
    
# '''

# "남자" if gender == "1" or gender == "3" or gender == "5" else "여자"
# "남자" if gender in ("1", "3", "5") else "여자"

# 주민번호로 나이 출력
# 1. 올해의 년도
# 2. 태어난 년도
#   주민번호 앞 2자리를 슬라이싱
#   주민번호 7번째가 1 또는 2면 19xx
#   주민번호 7번째가 2 또는 4면 20xx


jumin = input("주민등록번호 입력: ") # 123456-7898765
gender = jumin[7] # 7
back_year = jumin[0:2] # 12
# birth_year, age = 0, 0
THIS_YEAR = 2024

if gender == "1" or "2":
    birth_year = "19" + back_year
elif gender == "3" or "4":
    birth_year = "20" + back_year
else:
    print("당신은 외계인입니까?")

birth_year = int(birth_year)
age = THIS_YEAR - birth_year
2024 - 1977
print(f"{age}살")
'''
강사님의 해결법
import datetime
this_year = datetime.datetime.now().year
year = jumin[0:2]

if jumin[7] in ("1", "2"):
    year = int("19" + year)
elif jumin[7] in ("3", "4"):
    year = int("20" + year)
print(f"{this_year-year}세")
'''