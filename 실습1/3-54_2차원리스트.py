def find_path(a):
    n = len(a)
    stack = [(0, 0)]
    visited = set()

    while stack:
        x, y = stack.pop()
        visited.add((x, y))

        if x == n-1 and y == n-1:
            return True

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))

    return False

# 입력 예시
# 첫 줄에는 정수 n이 주어지고, 다음 n줄에 걸쳐서 n개의 정수가 주어진다.
# 각 정수는 0 또는 1이며, 0은 통과 가능한 열린 공간이고, 1은 통과할 수 없는 블록이다.

# 입력 예시
# 5
# 0 1 0 1 0
# 0 0 0 0 0
# 1 1 1 1 0
# 1 0 0 0 0
# 1 1 1 1 0

n = 5
a = [[0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 0]]

if find_path(a):
    print("Yes")
else:
    print("No")
