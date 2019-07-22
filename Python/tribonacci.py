def tribonacci():
    n=int(input())
    for i in range(0,n):
        n=int(input())
        k=1
        a=0;b=0;c=1
        while k!=0:
            
            count = 0
            
            d=a+b+c
            a=b;b=c;c=d
            for j in range(1,d+1):
                if(d%j==0):
                    count+=1
            if count>n:
                break
        print(d)


if __name__=="__main__":
    tribonacci()
