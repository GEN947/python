# 1. 할일 목록, 2. 할일 추가, 3. 할일 변경, 4. 할일 삭제, 5. finish 변경, 999. 종료
# 할일은 할일 번호, 할일, 완료여부로 구성

# def 써서 해보기

todos = []

todos.append({"tno":1, "title": "자바공부", "finish": False})
todos.append({"tno":2, "title": "스프링공부", "finish": False})
todos.append({"tno":3, "title": "파이썬공부", "finish": False})

is_find = True

while True:
    print("### 할일 관리 ###")
    print("1. 할일 목록, 2. 할일 추가, 3. 할일 변경, 4. 할일 삭제, 5. finish 변경, 999. 종료")
    select_number = input("메뉴 선택: ")
    if select_number == "1":
        for item in todos:
            print(item)
    elif select_number == "2":
        tno = todos[-1]["tno"] + 1
        title = input("할일: ")
        finish = False
        todos.append({"tno": tno, "title": title, "finish": finish})
    elif select_number == "3":
        select_change_number = int(input("변경할 할일 번호: "))
        for item in todos:
            if item["tno"] == select_change_number:
                change_todo = input("변경할 할일: ")
                item["title"] = item["title"].replace(item["title"], change_todo)
                is_find = True
                break
            else:
                is_find = False
        if is_find == False:
            print("할일 목록에 있는 번호만을 입력해주세요")
            continue
        else:
            pass
    elif select_number == "4":
        select_delete_number = int(input("삭제할 할일 번호: "))
        for item in todos:
            if item["tno"] == select_delete_number:
                todos.remove(item)
                is_find = True
                break
            else:
                is_find = False
        if is_find == False:
            print("할일 목록에 있는 번호만을 입력해주세요")
            continue
    elif select_number == "5":
        select_finish_number = int(input("finish 변경할 할일 번호: "))
        for item in todos:
            if item["tno"] == select_finish_number:
                item["finish"] = not item["finish"]
                is_find = True
                break
            else:
                is_find = False
        if is_find == False:
            print("할일 목록에 있는 번호만을 입력해주세요")
            continue
    elif select_number == "999":
        print("이용해주셔서 감사합니다")
        break
    else:
        print("메뉴를 제대로 입력해주세요")

'''
def 쓰기

todos = []

todos.append({"tno":1, "title": "자바공부", "finish": False})
todos.append({"tno":2, "title": "스프링공부", "finish": False})
todos.append({"tno":3, "title": "파이썬공부", "finish": False})
is_find = True
        
def print_list():
    global is_find
    for item in todos:
        print(item)

def add_todo():
    global is_find
    tno = todos[-1]["tno"] + 1
    title = input("할일: ")
    finish = False
    todos.append({"tno": tno, "title": title, "finish": finish})

def change_todo():
    global is_find
    select_change_number = int(input("변경할 할일 번호: "))
    for item in todos:
        if item["tno"] == select_change_number:
            change_todo = input("변경할 할일: ")
            item["title"] = item["title"].replace(item["title"], change_todo)
            is_find = True
            break
        else:
            is_find = False

def delete_todo():
    global is_find
    select_delete_number = int(input("삭제할 할일 번호: "))
    for item in todos:
        if item["tno"] == select_delete_number:
            todos.remove(item)
            is_find = True
            break
        else:
            is_find = False

def toggle_finish():
    global is_find
    select_finish_number = int(input("finish 변경할 할일 번호: "))
    for item in todos:
        if item["tno"] == select_finish_number:
            item["finish"] = not item["finish"]
            is_find = True
            break
        else:
            is_find = False

while True:
    print("### 할일 관리 ###")
    print("1. 할일 목록, 2. 할일 추가, 3. 할일 변경, 4. 할일 삭제, 5. finish 변경, 999. 종료")
    select_number = input("메뉴 선택: ")
    if select_number == "1":
        print_list()
    elif select_number == "2":
        add_todo()
    elif select_number == "3":
        change_todo()
        if is_find == False:
            print("할일 목록에 있는 번호만을 입력해주세요")
            continue
    elif select_number == "4":
        delete_todo()
        if is_find == False:
            print("할일 목록에 있는 번호만을 입력해주세요")
            continue
    elif select_number == "5":
        toggle_finish()
        if is_find == False:
            print("할일 목록에 있는 번호만을 입력해주세요")
            continue
    elif select_number == "999":
        print("이용해주셔서 감사합니다")
        break
    else:
        print("메뉴를 제대로 입력해주세요")
'''
