class SList:    #단순연결 리스트 클래스 생성
    class Node: #노드 클래스 생성
        def __init__(self, item, link):     #노드 객체 생성자
            self.item = item        #인스턴스 변수 #나(노드) 항목
            self.next = link        #가르키는 항목, 다음 노드 레퍼런스

    def __init__(self):     #단순 연결 리스트 생성자
        self.head = None    #헤드
        self.size = 0   #항목 수
    
    def size(self):
        return self.size
            
    def is_empty(self):
        return self.size==0

    #### 리스트 추가

    def insert_front(self, item):   #리스트 제일 앞에 추가하는 경우
        if self.is_empty():         #리스트가 비었으면
            self.head = self.Node(item, None) #헤드가 아이템 가리키고 다음 노드는 없음
        else:       #리스트가 있을 경우 앞으로 오는 경우
            self.head = self.Node(item, self.head)
        self.size += 1      #항목 수 증가
    
    def insert_after(self, item, p):        # 리스트 중간에 삽입하는 경우 p 다음 삽입
        p.next = self.Node(item, p.next)    #원래 p 다음 노드는 node의 다음 노드가 되고 노드가 p 다음 노드가 됨
        self.size += 1

    def insert_last(self, item):    # 리스트 맨 뒤에 삽입
        new_node = self.Node(item, None)    #다음 노드가 없는 노드 생성
        if self.is_empty():         # 노드가 비어있을 경우
            self.head = new_node    #해드를 뉴노드로
        else:       #리스트가 있을 경우
            p = self.head       #p를 헤드로 지정
            while p.next:       #p 다음이 존재하면 반복하여 마지막 노드로 이동
                p = p.next      #p다음으로 이동
            p.next = new_node   #p 다음 노드를 새 노드로 지정
        self.size += 1

    #### 리스트 삭제

    def delete_front(self):     # 리스트 맨 앞 삭제
        if self.is_empty():     #리스트가 비었을 때 오류 처리
            raise EmptyError('Underflow')
        else: 
            self.head=self.head.next    #헤드를 다음 노드로 이동
            self.size -=1 
    
    def delete_after(self, p):  #리스트 중간 삭제 p 다음값 삭제
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next          #t는 p 다음 노드
        p.next = t.next     #p 다음 노드를 다다음 노드로 변경
        self.size -= 1

    def delete_last(self):  # 마지막 노드 삭제
        if self.is_empty():  # 리스트가 비었을 때 오류처리
            raise EmptyError('Underflow')
        else:
            p = self.head
            q = None
            while p.next:   #p 다음 노드가 있을때까지 p는 마지막 노드 가르킴, q는 마지막 전 노드 가르킴
                q = p       #q=p
                p = p.next  #p는 다음 노드를 가리킴
            q.next = None       # 마지막 전 노드의 다음 노드 끊기, 마지막 노드를 리스트에서 연결 끊음
            self.size -= 1
            return p            # 마지막 노드 레퍄런스 반환

    #### 기타
                       
    def search(self, target): # 순차탐색
        p = self.head
        for k in range(self.size):
            if target == p.item: return k
            p = p.next
        return None
            
    def print_list(self): #출력
        p=self.head
        while p:
            if p.next != None:
                print(p.item, '->', end='')
            else:
                print(p.item)
            p=p.next
                
class EmptyError(Exception):
    pass

#### 실행문

if __name__ == '__main__':
    s = SList()
s.insert_front('orange')
s.insert_front('apple')
s.insert_after('cherry', s.head.next)
s.insert_front('pear')
s.print_list()
print('cherry는 %d 번째' % s.search('cherry'))
print('kiwi는', s.search('kiwi'))
print('배 다음 노드 삭제 후: \t\t', end='')
s.delete_after(s.head)
s.print_list()
print('첫 노드 삭제 후: \t\t', end='')
s.delete_front()
s.print_list()
print('첫 노드로 망고, 딸기 삽입 후: \t', end='')
s.insert_front('mango')
s.insert_front('strawberry')
s.print_list()
s.delete_after(s.head.next.next)
print('오렌지 다음 노드 삭제 후: \t', end='')
s.print_list()
