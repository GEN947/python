lang = "python"
### slicing

print(lang[0])  #p
print(lang[5])  #n

print("a" in lang)
print("p" in lang)
print("P" in lang)

print(lang[-1]) #n
print(lang[-1]) #n

string = "123456789"
# 문자열[시작위치:끝위치+1]
print(string[1:3])

# 문자열[시작위치:None]
print(string[2:])

# 문자열[시작위치:끝위치+1:간격]
print(string[1::5])

# 짝수만 출력
print(string[1::2])