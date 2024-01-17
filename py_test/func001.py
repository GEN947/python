def sample():
    return 10

def is_major(nai:int) -> bool:
    return nai >= 18

def get_fee(nai:int) -> int:
    if nai >= 25 and nai <= 74:
        return 3000
    elif nai < 25 or nai > 74:
        return 0

# def is_adult(nai):
#     if nai >= 25 and nai <= 74:
#         print(f"귀하의 나이는 {nai}세로 3000원입니다.")
#         return True
#     elif nai < 25 or nai > 74:
#         print(f"귀하의 나이는 {nai}세로 무료입니다.")
#         return True

def how_price(per:int) -> int:
    if per >= 10:
        return 2400*per
    else:
        return 3000*per