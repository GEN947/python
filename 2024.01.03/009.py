# 국어, 영어 점수 입력받아 합계, 평균 출력
kor_score = int(input("국어 점수 입력: "))
eng_score = int(input("영어 점수 입력: "))
sum_score = kor_score+eng_score
avg_score = sum_score/2

print(f"합계: {sum_score}, 평균: {avg_score}")
# print("합계: " + str(sum_score) + "점, 평균: " + str(avg_score) + "점") # "합계: "는 str, sum_score는 int기에 안 됨..? 이유 뭐임
