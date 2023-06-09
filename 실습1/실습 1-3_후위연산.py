def push(item): # 삽입 연산
    stack.append(item) 
def peek(): # top 항목 접근
    if len(stack) != 0:
        return stack[-1]
def pop(): # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1)      
        return item
def compute(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def evaluation(input_expression):
    token_list = input_expression.split()

    for token in token_list:
        if token in "0123456789":
            push(int(token))
        else:
            operand2 = pop()
            operand1 = pop()
            result = compute(token,operand1,operand2)
            push(result)
    return pop()

stack = []
print(evaluation('7 8 + 3 2 + /'))       # 3.0
print(evaluation('2 3 5 * 6 4 - / +'))   # 9.5
