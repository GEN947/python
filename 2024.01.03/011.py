# 월급을 입력받아 연봉 출력
# 소득세율 3.3%, 실수령액 출력
month_salary = int(input("월급 입력: "))
annual_salary = month_salary*12
annual_income_tax = annual_salary*0.033 # literal 소득세율 3.3%는 상수로 설정하는게 야무졌다
# INCOME_TAX_RATE = 0.033
# annual_income_tax = annual_salary*INCOME_TAX_RATE
actual_salary = annual_salary - annual_income_tax
print(f"세전 연봉은 {annual_salary}원, 소득세는 {annual_income_tax}원, 세후 연봉은 {actual_salary}원입니다.")

if actual_salary < 30000000:
    print("그지새끼시네요 ㅋㅋ")
elif actual_salary >= 30000000 and actual_salary < 50000000:
    print("입에 풀칠은 하고 사시나봐요 ㅋㅋ")
elif actual_salary >= 50000000 and actual_salary < 70000000:
    print("좀 치시네요?")
elif actual_salary >= 70000000 and actual_salary < 100000000:
    print("정말 잘 버시네요!")
elif actual_salary >= 100000000:
    print("억!!")