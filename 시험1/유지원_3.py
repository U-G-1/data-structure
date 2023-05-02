stack = []  # 스택 초기화

# 사용자로부터 문자열 입력 받기
input_str = input("문자열을 입력하세요: ")

# 스택에 문자열을 역순으로 삽입
for char in input_str:
    stack.append(char)

# 스택에서 문자열을 꺼내어 출력
output_str = ""
while stack:
    output_str += stack.pop()

print("입력한 문자열의 역순: ", output_str)
