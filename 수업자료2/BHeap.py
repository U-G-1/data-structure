class BHeap:
    def __init__(self, a): # 이진 힙 생성자
        self.a = a
        self.N = len(a) - 1

    def create_heap(self):  # 초기 힙 만들기
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):  # 삽입 연산
        self.N += 1
        self.a.append(key_value)  # 리스트에 추가
        self.upheap(self.N)       # 위로 올라가며 힙 속성 회복시키기 위해

    def delete_min(self):  # 최솟값 삭제
        if self.N == 0:
            print('힙이 비어 있음')
            return None
        minimum = self.a[1]  # a[1]의 최솟값을 minimum에 저장하여 반환
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        self.downheap(1)  # 힙 속성을 회복시키기 위해
        return minimum

    def downheap(self, i):  # 힙을 내려가며 힙 속성을 회복
        while 2*i <= self.N:
            k = 2*i    # k는 왼쪽자식의 인덱스
            if k < self.N and self.a[k][0] > self.a[k+1][0]:
                k += 1 # k가 승자의 인덱스
            if self.a[i][0] < self.a[k][0]:
                break  # 현재 노드가 자식 승자보다 작으면, 루프 중단
            self.a[i], self.a[k] = self.a[k], self.a[i] # 현재 노드와 자식 승자와 교환
            i = k      # 자식 승자가 현재 노드가 되어 다시 반복하기 위해
        
    def upheap(self, j): # 힙을 올라가며 힙 속성 회복
        while j > 1 and self.a[j//2][0] > self.a[j][0]:  # 현재 노드가 루트가 아니고 동시에 부모가 크면
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]  # 부모와 현재 노드 교환
            j = j // 2  # 현재 노드가 한 층 올라감

    def print_heap(self):  # 힙 출력
        for i in range(1, self.N+1):
            print('[%2d' % self.a[i][0], self.a[i][1],']', end = '')
        print('\n힙 크기 =', self.N)

if __name__ == '__main__':
    a = [None] * 1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])
    b = BHeap(a)
    print('하비 만들기 전:')
    b.print_heap()
    b.create_heap()
    print('최소힙:')
    b.print_heap()
    print('최솟값 삭제 후:')
    print(b.delete_min())
    b.insert([5, 'apple'])
    print('5 삽입 후')
    b.print_heap
