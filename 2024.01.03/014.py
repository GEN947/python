# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오
input_num = int(input("숫자 입력: "))

if input_num % 3 == 0:
    print(f"{input_num}은(는) 3의 배수입니다.")
else:
    print(f"{input_num}은(는) 3의 배수가 아닙니다.")

# 점수를 입력받아 90점 이상이면 우수 70점 이상이면 패스, 70점미만이면 낙제
input_jumsu = int(input("점수 입력: "))

if input_jumsu >= 90:
    print(f"{input_jumsu}점으로 우수입니다")
elif input_jumsu >=70:
    print(f"{input_jumsu}점으로 패스입니다.")
else:
    print(f"{input_jumsu}점으로 낙제입니다.")
    