class LinkedQueue:

    class _Node:
        def __init__(self, item, next):  # 노드 생성자
            self._item = item
            self._next = next

    def __init__(self): # 큐 생성자
        self._front = None
        self._rear  = None
        self._size  = 0

    def size(self): return self._size
    def is_empty(self): return self._size == 0

    def add(self, item): # 삽입 연산
        newnode = self._Node(item, None) 
        if self.is_empty():
            self._front = newnode   
        else:
            self._rear._next = newnode
        self._rear = newnode
        self._size += 1
        
    def remove(self): # 삭제 연산
        if self.is_empty():
            raise EmptyError('Queue 비어있음')
        fitem = self._front._item
        self._front = self._front._next
        self._size -= 1
        if self.is_empty(): 
            self._rear = None 
        return fitem
    
    def print_q(self): # 큐 출력
        p = self._front
        print('front:  ', end='')
        while p:
            if p._next != None:
                print('{!s:7}'.format(p._item), '->   ', end = '')
            else:
                print(p._item, end = '')
            p = p._next
        print('  :rear')
            
class EmptyError(Exception):  # underflow 시 에러 처리
    pass

if __name__ == '__main__':
    l = LinkedQueue()
l.add('불고기')
l.add('비빔밥')
l.add('잡채')
l.add('떡볶이')
l.print_q()
l.remove()
l.print_q()
l.remove()
l.print_q()
l.add('짜장면')
l.print_q()