class SList:
    class Node:
        def __init__(self, item, link):  # 노드 생성자
            self.item = item
            self.next = link

    def __init__(self):  # 연결 리스트 생성자
        self.head = None
        self.size = 0

    def size(self):  # 연결 리스트의 노드 수 리턴
        return self.size

    def is_empty(self):  # 연결 리스트가 empty인지 검사
        return self.size == 0

    def insert_front(self, item):  # 연결 리스트의 맨 앞에 노드 삽입
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def delete_last(self):  # 문제 2.36  마지막 노드 삭제
        if self.is_empty():  # empty 리스트에서 삭제 불가
            return None
        else:
            p = self.head
            q = None
            while p.next:
                q = p
                p = p.next
            q.next = None       # 마지막 노드를 리스트에서 연결 끊음
            self.size -= 1
            return p            # 마지막 노드 레퍄런스 반환

    def print_list(self):  # 연결 리스트를 한 줄에 출력
        p = self.head
        while p:
            if p.next is not None:
                print(p.item, ' -> ', end=' ')
            else:
                print(p.item)
            p = p.next


s = SList()  # 연결 리스트 만들기
if s.delete_last() == None:
    print('underflow')
s.print_list()
s.insert_front(900)
s.insert_front(800)
s.insert_front(700)
s.insert_front(600)
s.insert_front(500)
s.insert_front(400)
s.insert_front(300)
s.insert_front(200)
s.insert_front(100)
s.print_list()
print(s.delete_last().item, '삭제 후: ', end='')
s.print_list()
print(s.delete_last().item, '삭제 후: ', end='')
s.print_list()
print(s.delete_last().item, '삭제 후: ', end='')
s.print_list()