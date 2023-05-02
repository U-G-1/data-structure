def push(item): # 삽입 연산
    stack.append(item)  #리스트 맨 뒤에 항목 추가
    
def peek(): # top 항목 접근
    if len(stack) != 0:     #리스트 길이가 0이 아닐 때
        return stack[-1]    #리스트 맨 뒤 항목 반환

def pop(): # 삭제 연산
    if len(stack) != 0:     #리스트 0 아닐 때
        item = stack.pop(-1) #리스트 맨 뒤에 있는 항목 제거
        return item


stack = []  #리스트 선언
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후: \t', end='')
print(stack, '\t<- top')
print('top 항목: ', end='')
print(peek())
push('pear')
print('배 push 후: \t\t', end='')
print(stack, '\t<- top')
pop()
push('grape')
print('포도 push 후: \t\t', end='')
print(stack, '\t<- top')


