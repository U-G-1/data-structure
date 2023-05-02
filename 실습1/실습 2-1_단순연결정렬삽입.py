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


    def insert(self, target):
        print('삽입할 항목 =', target)  # 삽입할 값을 출력
        if self.is_empty():  # 리스트가 empty인 경우
            self.head = self.Node(target, None)  # 첫 노드로 삽입
        else:
            p = self.head  # 리스트의 첫 번째 노드
            q = None
            while p:
                if p.item > target:  # 현재 노드의 값보다 삽입할 값이 작을 경우
                    if p != self.head:  # 첫 번째 노드가 아닐 경우
                        q.next = self.Node(target, p)  # 이전 노드(q)와 삽입 노드(p) 사이에 새 노드 삽입
                    break
                q = p  # 이전 노드를 현재 노드로 변경
                p = p.next  # 현재 노드를 다음 노드로 변경
            if q is None:  # 리스트가 비어있는 경우
                self.head = self.Node(target, self.head)  # 첫 노드로 삽입
            elif p is None:  # 리스트의 마지막에 삽입하는 경우
                q.next = self.Node(target, None)  # 이전 노드(q)의 다음 노드로 새 노드 삽입
        self.size += 1  # 리스트의 크기 증가


    def print_list(self):  # 연결 리스트를 한 줄에 출력
        p = self.head
        while p:
            if p.next is not None:
                print(p.item, ' -> ', end=' ')
            else:
                print(p.item)
            p = p.next


s = SList()  # 연결 리스트 생성

s.insert(10)
s.print_list()
s.insert(450)
s.print_list()
s.insert(900)
s.print_list()
s.insert(5)
s.print_list()
s.insert(350)
s.print_list()
s.insert(1000)
s.print_list()