def add(item):  # 삽입 연산
    q.append(item)  #마지막에 삽입

def remove():  # 삭제 연산
    if len(q) != 0:
        item = q.pop(0)      #맨 앞 항목 삭제
        return item

def print_q():  # 큐 출력
    print('front ->  ', end='')
    for i in range(len(q)):
        print('{:<8}'.format(q[i]), end='')
    print('  <- rear')

q = []

add('apple')
add('orange')
add('cherry')
add('pear')
print('사과, 오렌지, 체리, 배, 삽입 후: \t', end='')
print_q()
remove()
print('remove 한 후:\t\t', end='')
print_q()