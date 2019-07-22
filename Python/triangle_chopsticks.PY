def triangle_chopsticks():
    n=int(input())
    arr=[]
    for i in range(0,n):
        a, b, r=input().split(' ')
        num=int(input())
        arr = list(map(int,input().split(' ')))
        count =0
        for i in arr:
                if int(a) + int(b) > int(i) and int(a) + int(i) > int(b) and int(b) + int(i) > int(a):
                        count=count+1

        print(count)
        if count>int(r):
                print("Natsu")
        elif count<int(r):
                print("Grey")                   

            
    

if __name__=='__main__':
    triangle_chopsticks()