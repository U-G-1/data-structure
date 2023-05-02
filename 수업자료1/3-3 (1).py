def add(item):  # 삽입 연산
    q.append(item)

def remove():  # 삭제 연산
    if len(q) != 0:
        item = q.pop(0)      
        return item

def print_q():  # 큐 출력
    print('front ->  ', end='')
    for i in range(len(q)):
        print('{:<8}'.format(q[i]), end='')
    print('  <- rear')