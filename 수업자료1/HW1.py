# 1~20 정수 순환 출력
def seq_printer(n):
    if n <= 20:
        print(n, end=' ')
        seq_printer(n + 1)
        
        
seq_printer(1)