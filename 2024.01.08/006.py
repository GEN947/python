# collection 타입: list, tuple, set, dictionary
# sequence 타입: list, tuple

# list와 tuple의 차이점
# list는 mutable(가변), tuple은 immutable(불변)

list1 = [1, 3, 5]
tuple1 = tuple(list1)
list2 = list(tuple1)

print(list1)
print(tuple1)
print(list2)

# 데이터가 있다 -> Create Read Update Delete

# Create Read
list1.append(100)
print(list1)

# for 변수 in 컬렉션:
for i in list1:
    print(i)

for i in list1:
    pass
print("1111")


# index(리스트에서 값의 위치)로 Update
list1[1] = 200
print(list1)

# Delete
list1.remove(200)   # method
print(list1)
# 값을 찾아서 지움

del list1[2]        # 함수가 아니고 연산자
print(list1)
# n번째의 값을 지움

# 게시판에 글 번호가 있는 이유가 이거였다...............

# Create -> 추가
# Read -> 하나씩
# Update, Delete -> 찾아서 ..

# Update와 Delete는 Read가 따라온다 보면 된다