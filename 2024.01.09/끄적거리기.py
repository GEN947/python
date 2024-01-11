# 메뉴(1. 할일 했나 안 했나, 2. 할일 변경 3. 할일 추가, 4. 할일 삭제, 999. 탈출)

todos = [
    {"tno": 1, "title": "자바공부", "finish": False},
    {"tno": 3, "title": "파이썬공부", "finish": False},
    {"tno": 4, "title": "오라클공부", "finish": False}
]

is_find = True
while True:
    print("==========================================================")
    print("1. 할일 했나 안 했나, 2. 할일 변경 3. 할일 추가, 4. 할일 삭제, 999. 탈출")
    input_number = input("번호 입력: ")
    if input_number == "1": # 할일 했나 안 했나 (finish 변경)
        input_tno = int(input("몇번 할일에서 했는지 안 했는지 변경: "))
        for tno in todos:
            if tno["tno"] == input_tno:
                tno["finish"] = not tno["finish"]
                is_find = True
                break
            else:
                is_find = False
        if is_find == True:
            print(f"{todos}")
        else:
            print(f"올바른 값만 입력해주세요")
    elif input_number =="2": # 할일 변경 (title 변경)
        input_title = input("변경할 할 일: ")
        for tno in todos:
            if tno["title"] == input_title:
                input_change_title = input("변경한 할 일: ")
                tno["title"] = tno["title"].replace(tno["title"], input_change_title)
                is_find = True
                break
            else:
                is_find = False
        if is_find == True:
            print(f"{todos}")
        else:
            print("올바른 값만 입력해주세요")
    elif input_number == "3": # 할일 추가 (Create)
        new_todo = int(input("추가할 번호: "))
        if tno > 4:
            new_title = input("추가할 할일 입력: ")
            append_todo = {"tno": new_todo, "title": new_title, "finish": False}
            todos.append(append_todo)
            is_find = True
        else:
            is_find = False
        if is_find == True:
            print(f"{todos}")
        else:
            print("올바른 값만을 입력해주세요")
    elif input_number == "4": # 할 일 삭제(Delete)
        delete_todo = int(input("삭제할 할일 번호: "))
        for item in todos:
            if item["tno"] == delete_todo:
                todos.remove(item)
                is_find = True
            else:
                is_find = False
        if is_find == True:
            print(f"{todos}")
        else:
            print("올바른 값만을 입력해주세요")
    elif input_number == "999":
        print("이용해주셔서 감사합니다")
        break