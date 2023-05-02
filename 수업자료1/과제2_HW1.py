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

    def insert_last(self, item):  # 문제 2.35 맨 뒤에 삽입
        new_node = self.Node(item, None)
        if self.is_empty():
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
        self.size += 1


    def print_list(self):  # 연결 리스트를 한 줄에 출력
        p = self.head
        while p:
            if p.next is not None:
                print(p.item, ' -> ', end=' ')
            else:
                print(p.item)
            p = p.next


s = SList()  # 연결 리스트 만들기
s.insert_last(50)
s.print_list()
s.insert_last(100)
s.insert_last(200)
s.insert_last(300)
s.insert_last(400)
s.insert_last(500)
s.print_list()
s.insert_last(1000)
s.print_list()
