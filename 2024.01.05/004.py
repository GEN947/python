리스트=[3,"hello",5>3,True]
튜플=tuple(리스트)

# CRUD - 삭제는 del 연산자
# method: 객체(파이썬을 구성하는 부품)에 소속된 함수
print(리스트)       # 아직 아무것도 안 건드림
리스트.append(100)          # 값 추가 (Create) / append는 함수 method / .은 뒤의 함수가 앞의 객체에 소속됐다는 뜻이다 / 즉, append는 리스트에 소속돼있다.
리스트[0]=리스트[0]*10      # 값 변경 (Update)
print(리스트)               # 함수 print와 함수 append에 마우스를 올려보자 ...
del 리스트[0]               # 값 삭제 (Delete)
print(리스트)

