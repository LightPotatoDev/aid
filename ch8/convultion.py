n1,m1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n1)] #입력
n2,m2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(n2)] #커널
Ans = [[0]*(n1-n2+1) for _ in range(m1-m2+1)]

def convultion(r,c):
    s = 0
    for i in range(n2):
        for j in range(m2):
            s += A[r+i][c+j]*B[i][j]
    return s

for i in range(n1-n2+1):
    for j in range(m1-m2+1):
        Ans[i][j] = convultion(i,j)

for row in Ans:
    print(row)