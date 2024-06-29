import sys
sys.stdin = open('input.txt')


while True:
    num = int(input())
    cnt = 1
    if num == 0:
        break
    else:
        for i in str(num):
            cnt += 1
            if i == '1':
                cnt += 2
            elif i == '0':
                cnt += 4
            else:
                cnt += 3

    print(cnt)


