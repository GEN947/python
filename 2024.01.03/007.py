num = 70
if num >= 0:
    print(f"{num}은 0 이상입니다")
if num <= 100:
    print(f"{num}은 100 이하입니다.")
if num >= 0 and num <= 100:
    print(f"{num}은 0이상 100 이하입니다.")
if num < 0 or num > 100:        # not(num >= 0 and num <= 100)
    print(f"{num}은 0 미만, 100 초과 입니다.")
