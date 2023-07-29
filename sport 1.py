A = [int(i) for i in input().split()]
for i in range(len(A)):
    m = A[i]
    p = i
    for x in range(i+1,len(A)):
        if A[x] < m :
            m = A[x]
            p = x
    A[p]=A[i]
    A[i]=m
print(A)
