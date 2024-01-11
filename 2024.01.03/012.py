# 반지름을 입력 받아 원의 넓이를 출력하시오
# 반지름을 입력 받아 원의 둘레를 출력하시오

PI = 3.14
radius = int(input("반지름 입력: "))
area_of_circle = PI*radius*radius
circumference_of_circle = 2*PI*radius

print(f"원의 넓이: {area_of_circle}, 원의 둘레: {circumference_of_circle}")
