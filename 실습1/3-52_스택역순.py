class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.top.item
        self.top = self.top.next
        self.size -= 1
        return item


    def reverse(self):
        # new_stack = Stack()
        # while not self.is_empty():
        #     new_stack.push(self.pop())
        #return new_stack
        new_stack = Stack()
        while not self.is_empty():
            new_stack.push(self.pop())
        
        global it2
        while not self.is_empty():
            it2 = self.pop()
            new_stack.push(it2)
            print(it2)

        p = new_stack.top
        while p:
            if p.next != None:
                print(p.item, end='')
            else:
                print(p.item, end='')
            p = p.next
        print(new_stack)

        # result = []
        # while not new_stack.is_empty():
        #     item = new_stack.pop()
        #     print(item)
        #     result.append(item)
        # return result

s = Stack()
print('문자열 입력:', end='')
s.push(input())
s.push(input())
s.push(input())
print('역순 문자열:', end='')
print(s.pop(), end='')
print(s.pop(), end='')
print(s.pop(), end='')
