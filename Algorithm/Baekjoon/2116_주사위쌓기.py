'''
입력순서는 ABCDEF
전개도 순서는
  A
B C D E
  F
A(0)-F(5) / B(1)-D(3) / C(2)-E(4)
'''

N = int(input())

# 주사위받기
dice_arr = [list(map(int,input().split())) for _ in range(N)]
