# 정수 2개를 인자로 받아 덧셈해서 출력

def hap(a:int | float, b:int | float):
    print(a+b)

# 강제로 출력하는거기 때문에 바람직하지 않은 함수다

def hap2(a:int|float, b:int|float):
    # return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a+b

# 값으로 바꿔 저장하는게 바람직한 함수다

print(hap2(3, 4))