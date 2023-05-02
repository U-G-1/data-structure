class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def infix_to_postfix(infix):
    # 연산자들의 우선순위를 정의합니다.
    # 왼쪽 괄호와 오른쪽 괄호는 우선순위가 없으며 0으로 정의합니다.
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
    
    # 연산자를 저장할 스택을 생성합니다.
    operator_stack = Stack()
    
    # 후위 표기식으로 변환한 결과를 저장할 리스트를 생성합니다.
    postfix_list = []
    
    # 중위 표기식에서 문자를 한 개씩 읽어옵니다.
    for item in infix:
        if item.isdigit():
            # 읽어온 문자가 피연산자(숫자)인 경우, 결과 리스트에 추가합니다.
            postfix_list.append(item)
        elif item == "(":
            # 읽어온 문자가 왼쪽 괄호인 경우, 스택에 저장합니다.
            operator_stack.push(item)
        elif item == ")":
            # 읽어온 문자가 오른쪽 괄호인 경우,
            # 왼쪽 괄호가 나올 때까지 스택에서 연산자를 꺼내 결과 리스트에 추가합니다.
            while operator_stack.peek() != "(":
                postfix_list.append(operator_stack.pop())
            # 왼쪽 괄호는 결과 리스트에 추가하지 않고 스택에서 제거합니다.
            operator_stack.pop()
        else:
            # 읽어온 문자가 연산자인 경우,
            # 자신의 우선순위보다 낮은 우선순위를 가진 연산자가 스택에 있을 때까지 꺼내 결과 리스트에 추가합니다.
            while (not operator_stack.is_empty()) and (precedence[item] <= precedence[operator_stack.peek()]):
                postfix_list.append(operator_stack.pop())
            # 읽어온 연산자를 스택에 저장합니다.
            operator_stack.push(item)
    
    # 중위 표기식을 모두 읽었으면, 스택에 남아있는 모든 연산자를 꺼내 결과 리스트에 추가합니다.
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    
    # 결과 리스트를 문자열로 변환하여 반환합니다.
    return " ".join(postfix_list)


# 사용자로부터 중위 표기식을 입력받습니다.
infix = '(1+2)*3'

# 중위 표기식을 후위 표기식으로 변환합니다.
postfix = infix_to_postfix(infix)

# 변환한 결과를 출력합니다.
print(f"중위 표기식: {infix}")
print(f"후위 표기식: {postfix}")
