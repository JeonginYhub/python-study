import string

# 1. 먼저 파일을 읽기 모드로만 열기
with open("D:/news.txt", "r", encoding="utf-8") as infile:
    s = infile.read()

# 2. 소문자로 변환
s = s.lower()

# 3. 구두점 제거
for punct in string.punctuation:
    s = s.replace(punct, "")

# 4. 단어 분리
words = s.split()

# 5. 출력
print("✅ 정리된 단어 목록:")
print(words[:20])
