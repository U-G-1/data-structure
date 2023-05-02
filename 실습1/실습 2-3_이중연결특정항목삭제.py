class DList:
    class Node:
        def __init__(self, item, prev, link):  # 노드 생성자
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):  # 이중 연결 리스트 생성자
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0  # 항목 수

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self, p, item):  # p 앞에 삽입
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, p, item):  # p 다음에 삽입
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, target):  # target을 item으로 가진 노드 삭제하는 함수
        if self.size < 0:  # 리스트가 비어있는 경우
            print("리스트가 empty임")
        else:
            p = self.head.next  # head 다음 노드부터 시작
        while p != self.tail and p.item != target:  # tail까지 찾아도 target이 없으면
            p = p.next  # 다음 노드로 이동
        if p == self.tail:  # target이 없는 경우
            print("연결 리스트에 ", target, " 없음")
        else:
            f = p.prev  # p의 이전 노드
            r = p.next  # p의 다음 노드
            f.next = r  # f의 다음 노드는 r
            r.prev = f  # r의 이전 노드는 f
            self.size -= 1  # 리스트 크기 -1

    def print_list(self):  # 리스트 출력
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next


class EmptyError(Exception):  # underflow 시 에러 처리
    pass


s = DList()
s.insert_after(s.head, 300)
s.insert_after(s.head, 100)
s.insert_before(s.tail, 500)
s.insert_before(s.tail, 600)
s.insert_before(s.tail, 700)
s.insert_before(s.tail, 800)
s.insert_before(s.tail, 900)
s.print_list()
print('500 삭제 후: ', end='')
s.delete(500)
s.print_list()
s.delete(200)

s.delete(100)
print('100 삭제 후: ', end='')
s.print_list()
s.delete(900)
print('900 삭제 후: ', end='')
s.print_list()

#2차원 리스트 a에서 a[0][0]에서 a[n-1][n-1]까지 경로를 찾기 위해 스택을 이용한 파이썬 프로그램을 작성하라. 단, 리스트 a의 원소는 0 또는 1을 가지며, 0은 통과 가능한 열린 공간이고, 1은 통과할 수 없는 블록이다. 또한 리스트의 한 원소에서는 상하좌우 방향으로만 진행할 수 있다. 그리고 n은 5와 50 사이의 양수이다.2차원 리스트 a에서 a[0][0]에서 a[n-1][n-1]까지 경로를 찾기 위해 스택을 이용한 파이썬 프로그램을 작성하라. 단, 리스트 a의 원소는 0 또는 1을 가지며, 0은 통과 가능한 열린 공간이고, 1은 통과할 수 없는 블록이다. 또한 리스트의 한 원소에서는 상하좌우 방향으로만 진행할 수 있다. 그리고 n은 5와 50 사이의 양수이다.