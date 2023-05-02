class SList:    
    class Node: 
        def __init__(self, item, link):     
            self.item = item        
            self.next = link        

    def __init__(self):     
        self.head = None    
        self.size = 0  
    
    def size(self):
        return self.size
            
    def is_empty(self):
        return self.size==0


#############노드 맨 뒤에 삽입##################
    def insert_last(self, item):    
        new_node = self.Node(item, None)    
        if self.is_empty():         
            self.head = new_node   
        else:      
            p = self.head   
            while p.next:      
                p = p.next    
            p.next = new_node  
        self.size += 1

     
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
s.insert_last(100)
print('100 추가: ', end='')
s.print_list()
s.insert_last(200)
print('200 추가: ', end='')
s.print_list()
s.insert_last(300)
print('300 추가: ', end='')
s.print_list()
s.insert_last(400)
print('400 추가: ', end='')
s.print_list()
s.insert_last(500)
print('최종 생성된 연결 리스트: ', end='')
s.print_list()

