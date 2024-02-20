import sys
sys.stdin = open('input.txt')


N = 5
b = [list(map(int, input().split())) for _ in range(N)] # 문제판
c = [list(map(int, input().split())) for _ in range(N)] # 정답
temp = []
for i in range(N):
    for j in range(N):
        temp.append(c[i][j])
# print(temp)
# temp 리스트에서 하나씩 뽑아서 빙고판의 수를 없앤다.
# 행이나 열을 대각선을 5개 지우면 카운트가 1씩 증가하고
# 3이상 되는 순간 끝난다.
n = len(temp)
count = 0
bingo = 0
num = 0
for k in range(n):
    for i in range(N):
        for j in range(N):
            if temp[k] == b[i][j]:
                b[i][j] = 0
        #     print(b[i][j], end= ' ')
        # print()
                if b[i][i] == 0:
                    num += b[i][i]
                    count += 1
                    if num == 0:
                        bingo += 1
                elif b[i][4-i] == 0:
                    num += b[i][4-i]
                    count += 1
                    if num == 0:
                        bingo += 1
                elif b[i][j] == 0:
                    num += b[i][j]
                    count += 1
                    if num == 0:
                        bingo += 1
                elif b[j][i] == 0:
                    num += b[j][i]
                    count += 1
                    if num == 0:
                        bingo += 1
            if bingo == 3:
                break
print(count)
