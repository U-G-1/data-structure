def is_palindrome(input_string):
    token_list = list(input_string)
    flag = True
    while len(token_list) > 1 and flag == True:
        first_char = token_list.pop(0)  #첫 노드
        last_char = token_list.pop(-1)  #마지막 노드
        if first_char != last_char: #비교
            flag = False
    return flag

print(is_palindrome('racecar'))
print(is_palindrome('raddar'))
print(is_palindrome('wasitacatisaw'))
