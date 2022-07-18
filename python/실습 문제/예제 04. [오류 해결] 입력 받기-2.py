# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# words = list(map(int, input().split()))
# print(words)

# 원인 : ValueError: invalid literal for int() with base 10: "I'm"
# 원인 : int형 입력으로 형변환을 했는데 string형식을 입력함

# 수정 코드 
words = list(map(str, input().split()))
print(words)