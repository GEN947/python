# 집의 가로와 세로 길이를 입력받아 너비를 평으로 출력
# 3.3제곱미터가 1평

width_of_house = int(input("집의 가로 입력: "))
length_of_house = int(input("집의 세로 입력: "))

mul_width_length = width_of_house*length_of_house
square_footage_house = mul_width_length/3.3

print(f"집의 평수는{square_footage_house}입니다")
