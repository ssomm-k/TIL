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
v = E+1
ch1 = [0]*(v+1)
ch2 = [0]*(v+1)
for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

inorder(2)