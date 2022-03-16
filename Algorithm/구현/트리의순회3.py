def preorder(v):
    if v:
        print(v)
        preorder(ch1[v])
        preorder(ch2[v])
def inorder(v):
    if v:
        inorder(ch1[v])
        print(v)
        inorder(ch2[v])
def postorder(v):
    if v:
        postorder(ch1[v])
        postorder(ch2[v])
        print(v)

E = int(input())
arr = list(map(int,input().split()))
V = E+1
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
# 자식 번호를 인덱스로 부모번호를 저장
par = [0] * (V+1)
for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    par[c] = p

'''
4
2 1 2 4 4 3 4 5
'''
print(*par)

# root 찾기
root = 0
for i in range(1,V+1):
    if par[i] == 0:
        root = i
        break
print(root)
preorder(2)