# 변수의 이름이 겹치면 덮어쓴다
# 변수의 이름은 쉬워야한다 (주의..짧은게 쉬운게 아님)

a = 10
a = 20
a+=1
print(a)

# =: 같다는 뜻이 아니다. 오른쪽에서 왼쪽으로 대입

this_year = 2024
living_city = "Incheon"

seoul_latitude = 37.33 # latitude_of_seoul
seoul_longitude = 127.00 # longitude_of_seoul

seoul_latitude = seoul_latitude + 1
seoul_longitude = seoul_longitude + 1

print(seoul_latitude, seoul_longitude)

