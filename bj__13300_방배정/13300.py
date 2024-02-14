import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
female = [0] * 7
male = [0] * 7
# N: 학생수, K: 방 최대 인원수
for _ in range(N):
    S, Y = map(int, input().split())
    # S: 성별 0=여 1=남, Y: 학년
    if S == 0:
        female[Y] += 1
    else:
        male[Y] += 1

for i in range(1, 6+1):
    if female[i] % K == 0:
        female[i] = female[i] // K
    else:
        female[i] = (female[i] // K) + 1

    if male[i] % K == 0:
        male[i] = male[i] // K
    else:
        male[i] = (male[i] // K) + 1

print(sum(female) + sum(male))