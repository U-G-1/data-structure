class Node: # Node 클래스  
    def __init__(self, item, link): # Node 생성자     
        self.item = item           
        self.next = link
                                
def push(item): # push 연산
    global top
    global size
    top = Node(item, top)  #마지막 노드는 새 노드 next, 새 노드가 탑 
    size += 1
    
def peek(): # peek 연산
    if size != 0:
        return top.item 
              
def pop(): # pop 연산
    global top
    global size
    if size != 0:
        top_item = top.item     #탑 노드
        top = top.next          #탑을 탑 다음 노드로 지정하여 탑 삭제
        size -= 1               
        return top_item         #삭제된 탑 아이템 리턴
        
def print_stack(): # 스택 출력
    print('top ->\t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item, '-> ', end='')
        else:
            print(p.item, end='')
        p = p.next
    print()
top = None
size = 0


push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후:\t', end='')
print_stack()
print('top 항목: ', end='')
print(peek())
push('pear')
print('배 push 후:\t\t', end='')
print_stack()
print(pop())
push('grape')
print('pop(),포도 push 후:\t\t', end='')
print_stack()
