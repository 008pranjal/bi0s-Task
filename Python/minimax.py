def minimax():
    a=list(map(int,input().split(' ')))
    print(a)
    min = 0
    max = 0
    a.sort()
    for i in range(0,4):
        min+=a[i]
    for j in range(1,5):
        max+=a[j]    
    print(str(min)+" "+str(max))

if __name__=="__main__":
    minimax()
