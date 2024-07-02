import sys
sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    num_x = int(''.join(map(str, x)))
    num_y = int(''.join(map(str, y)))

    cnt = 0
    # for i in range(n - m + 1):
    #     z = int(str(i)+str(i+1)+str(i+2))
    #     if num_x <= z <= num_y:
    #         cnt += 1
    # for i in range(n - m + 1):
    #     z = int(''.join(map(str, arr[i:i + m])))
    #     if num_x <= z <= num_y:
    #         cnt += 1
    # 돌림판 상태에서 가능한 모든 M자리 수를 확인
    for i in range(n):
        # 돌림판이 원형이므로, 시작 위치가 배열 끝을 넘어갈 수 있음
        z_list = arr[i:i + m] # i부터 i+m-1까지의 부분 리시트를 가져온다.
        if len(z_list) < m: # 만약 가져온 부분 리스트의 길이가 m보다 작다면
            z_list += arr[:m - len(z_list)] # 리스트의 앞 부분을 이어 붙여서 길이 맞춘다.
        z = int(''.join(map(str, z_list))) # 부분 리스트를 하나의 정수로 변환한다.

        if num_x <= z <= num_y:
            cnt += 1
    print(cnt)