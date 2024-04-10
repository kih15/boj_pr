import sys
sys.stdin = open('input.txt')

vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input()
    if s == '#':
        break
    cnt = 0
    for i in s:
        if i.lower() in vowel:
            cnt += 1
    print(cnt)
