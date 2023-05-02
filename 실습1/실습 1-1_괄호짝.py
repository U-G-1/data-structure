a = ['(', '(', '{', '}', '(', ')', ')', '{', '{', '}', '(', ')', '}', ')']
print('입력:', a)

s = []
N = len(a)      #a의 길이
result = True   #결과는 T
for i in range(N):      # 길이만큼 반복
    if a[i] == '(' or  a[i] == '{':     #왼쪽 괄호일때 스택에 쌓음
        s.append(a[i])              
    else:                               #오른쪽 괄호일때
        popped_paren = s.pop()          #팝 실행하고 저장
        if a[i] == ')' and popped_paren != '(': #짝이 안맞으면 false 맞으면 계속
            result = False
            break
        elif a[i] == '}' and popped_paren != '{':
            result = False
            break

if len(s) == 0 and result == True:      #
    print('True')
else:
    print('False')   