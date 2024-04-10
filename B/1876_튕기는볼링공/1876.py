import sys
sys.stdin = open('input.txt')
import math
N = int(input())
for tc in range(N):
    T, X = map(float, input().split())  # T = 거리, X = 각도
    # 중앙을 (0, 0) 이라고 하면
    start = (T*100/2, 52.5)
    end = (-T*100/2, 52.5)
    a = abs(float(T*100/2))  # x 중간값
    b = abs(float(52.5))  # y 좌표의 차이 (레인과 볼링공 중심)
    # 범퍼에 맞고 튕겨나갈 때 중심기준으로 16, -16 이내인 범위내에서 충돌
    r = math.sqrt(a ** 2 + b ** 2)

    # 아크탄젠트는 math.atan 함수를 이용하면 계산할 수 있음
    # math.atan의 결과는 radian으로 반환됨 (degree가 아님)
    radian = math.atan(b / a)
    # π radian = 180 degree
    # print(radian)
    # radian을 degree로 변경을 해야 실제 각도를 얻을 수 있음
    # print(r, math.degrees(radian))
    # 901.5299495857029 3.3384705437643523
    # 821.1799437394949 3.6655563378982325



    # if:
    #     print('yes')
    # else:
    #     print('no')


