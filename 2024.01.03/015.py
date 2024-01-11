# 국어, 영어 모두 70점 이상이면 합격, 아닐 시 불합격
kor = int(input("국어 점수 입력: "))
eng = int(input("영어 점수 입력: "))

if kor >= 70 and eng >= 70:
    print(f"국어 {kor}점, 영어 {eng}점으로 합격하셨습니다.")
else:
    print(f"국어 {kor}점, 영어 {eng}점으로 불합격하셨습니다.") 