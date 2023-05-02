class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min_value = None

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
            self.min_value = value
        else:
            new_node.next = self.top
            self.top = new_node
            if value <= self.min_value:
                self.min_value = value

    def pop(self):
        if not self.top:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            if popped_node.value == self.min_value:
                self._update_min_value()
            return popped_node.value

    def get_min(self):
        return self.min_value

    def _update_min_value(self):
        current_node = self.top
        self.min_value = current_node.value
        while current_node is not None:
            if current_node.value < self.min_value:
                self.min_value = current_node.value
            current_node = current_node.next

# 입력 예시
stack = Stack()
stack.push(5)
stack.push(2)
stack.push(8)
print(stack.get_min()) # 출력 예시: 2
stack.pop()
print(stack.get_min()) # 출력 예시: 2
stack.pop()
print(stack.get_min()) # 출력 예시: 5
