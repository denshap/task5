import random
N=int(input("size: "))
m=[[random.randint(0,10) for j in range(N)] for i in range(N)]
def find(m, n):
    for i, itemi in enumerate(m):
        for j, itemj in enumerate(itemi):
            if itemj==int(n):
                return(i,j)
    return("Element not found")

print(find(m,input()))