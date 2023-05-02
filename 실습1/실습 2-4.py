class CList:
    class Node:
        def __init__(self, item, link):  # 노드 생성자
            self.item = item
            self.next = link

    def __init__(self):  # 원형 연결 리스트 생성자
        self.last = None  # CList의 마지막 노드
        self.size = 0  # 항목 수

    def no_items(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self.Node(item, None)
        if self.is_empty():  # 리스트가 empty일 때
            n.next = n
            self.last = n
        else:  # 정상적인 삽입
            n.next = self.last.next  # 새 노드가 last가 참조하는 노드의 다음 노드를 참조
            self.last.next = n  # last가 참조하는 노드의 다음 노드가 새 노드가 되도록
        self.size += 1

    def first(self):  # 첫 노드 접근
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next
        return f.item

    def delete(self):  # 첫 노드 삭제
        if self.is_empty():
            raise EmptyError('Underflow')
        x = self.last.next
        if self.size == 1:  # 1개뿐인 노드 제거
            self.last = None  # empty 리스트가 됨
        else:
            self.last.next = x.next  # 첫 노드 제거
        self.size -= 1
        return x.item

    def find_k_th(self, k):  # k = 0, 1, 2, ...
        if self.size - 1 < k:
            print(k, "번째 항목은 리스트에 없음")
            return None
        else:
            p = self.last.next
            for i in range(k, 0, -1):
                p = p.next
            return p.item

    def print_list(self):  # 연결 리스트 출력
        if self.is_empty():
            print('리스트 비어있음')
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, ' -> ', end='')
                p = p.next
            print(p.item)


class EmptyError(Exception):  # underflow 시 에러 처리
    pass


s = CList()
s.insert(900)
s.insert(800)
s.insert(700)
s.insert(600)
s.insert(500)
s.insert(400)
s.insert(300)
s.insert(200)
s.insert(100)
s.insert(0)
s.print_list()
print('s의 길이 =', s.no_items())
print(s.last.item)
print('0번째 항목 = ', end='')
print(s.find_k_th(0))
print('1번째 항목 = ', end='')
print(s.find_k_th(1))
print('4번째 항목 = ', end='')
print(s.find_k_th(4))
print('10번째 항목 = ', end='')
s.find_k_th(10)

