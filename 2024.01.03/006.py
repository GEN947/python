# 비교연산: 조건 1개
kor, eng = 75, 80
print(kor > 70, kor >= 70)
print(kor < 70, kor <= 70)
print(kor == 70, kor != 70)
# 논리연산
print(not kor > 70)
# 조건들을 연결
# and: 하나만 거짓이면 거짓 (모두 참이면 참) (조건이 여러개일때 하나씩 참거짓 판별하다 하나라도 거짓이 나오면 중지하고 빠져나옴 / 실행문 실행 X)
# or: 하나만 참이면 참 (모두 거짓이면 거짓) (조건이 여러개일때 하나씩 참거짓 판별하다 하나라도 참이 나오면 중지하고 빠져나옴 / 실행문 실행)