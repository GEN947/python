# control: 순서를 바꾼다
# 조건: 결과가 이럴수도 저럴수도 있다

# jumsu가 짝수인지 홀수인지 출력

jumsu = int(input("점수 입력: "))

if jumsu % 2 == 0:
    print("점수 짝수")
else:
    print("점수 홀수")
 
if jumsu >= 90:
    print("우수")
elif jumsu >= 70:
    print("합격")
else:
    print("불합격")