import sys
sys.stdin = open('input.txt')

# def is_hansu(n):
#     n = str(n)
#     if len(n) <= 2:
#         return True
#     dif = int(n[1]) - int(n[0])
#     for i in range(1, len(n)-1):
#         if int(n[i+1]) - int(n[i]) != dif:
#             return False
#     return True
#
# def count_hansu(n):
#     hansu_count = 0
#     for i in range(1, n+1):
#         if is_hansu(i):
#             hansu_count += 1
#     return hansu_count


# print(count_hansu(n))
def count_hansu(n):
    cnt = 0
    if n <= 99:
        return n
    else:
        cnt = 99
        for i in range(100, n+1):
            num_str = str(i)
            if (int(num_str[0]) - int(num_str[1])) == (int(num_str[1]) - int(num_str[2])):
                cnt += 1
    return cnt

n = int(input())
print(count_hansu(n))