import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    box = int(input())
    box_arr = []
    for i in range(box):
        arr = list(map(int,input().split()))
        box_arr.append(arr)

    for i in box_arr:
