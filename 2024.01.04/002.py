a = '345'
b = int(a)  # 345
c = float(a)    # 345.0
d = str(b)  # '345' ..?

print(a)
print(b)
print(c)
print(d)

ar = [3,4,5]
br = tuple(ar)  # 함수이름() -> 국선변호사

# 리스트에 원소를 추가한다: append
# .은 멤버 연산자
# append는 프리랜서가 아니라 ar에 소속된 함수 -> method
ar.append(10) # ??.() -> 사내 변호사 (aka. 삼성 변호사)
print(ar) 

xr = (10, 20, 30)
# xr에 40을 추가한 다음 출력
xr = list(xr)
xr.append(40)
xr = tuple(xr)
print(xr)
# 튜플에 값을 추가하는법 chatgpt에게 물어보기