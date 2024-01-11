todos = [
    {"tno": 1, "title": "자바공부", "finish": False},
    {"tno": 3, "title": "파이썬공부", "finish": False}
]

# Create
tno=4
title = input("할일 입력: ")
todo = {"tno": tno, "title": title, "finish": False}
todos.append(todo)
tno += 1

# Read
# f1or로 todos 출력
for todo in todos:
    print(todo)

# Update
# tno로 찾아 todos를 찾아 finish를 toggle(스위치)
# 못 찾으면 아무것도 하지 않는다
input_tno = int(input("변경할 할일 번호: "))
for todo in todos:
    if todo["tno"] == input_tno:
        todo["finish"] = not todo["finish"]
        break       # 생각보다 break가 중요
for todo in todos:
    print(todo)

# Delete
# 입력한 tno에 해당하는 todo를 찾아 삭제한다
input_tno = int(input("tno 입력: "))
for todo in todos:
    if todo["tno"] == input_tno:
        todos.remove(todo)
        break
for i in todos:
    print(i)