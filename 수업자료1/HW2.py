#순환을 이용하여 1에서 10까지의 정수의 합

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        res = n + sum_to_n(n - 1)
        return res
        
print(sum_to_n(10))
