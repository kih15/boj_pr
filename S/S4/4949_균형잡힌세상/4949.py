import sys
sys.stdin = open('input.txt')

while True:
    s = input()
    check = []
    answer = "yes"
    if s == '.':
        break

    for i in s:
        if i == '(' or i == '[':
            check.append(i)
        elif i == ')':
            if len(check) == 0:
                answer = "no"
                break
            else:
                if check.pop() != '(':
                    answer = "no"
                    break
        elif i == ']':
            if len(check) == 0:
                answer = "no"
                break
            else:
                if check.pop() != '[':
                    answer = "no"
                    break
        else:
            continue
    if len(check):
        answer = "no"
    print(answer)





