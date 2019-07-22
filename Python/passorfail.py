def passorfail():
    print("Enter the no. of students")
    m = int(input())
    print("Enter the no. of subjects")
    n = int(input())
    d1=dict()
    d2=dict()
   
    for i in range(0,m):
        c=0
        print("Enter name")
        s=input()
        print("Enter marks")
        arr = list(map(float,input().split(' ')))[:n]
        for i in arr:
            if i<40:
                avg=sum(arr)/n
                d2[s]=avg
                c=1
        if c==0:
            avg = sum(arr)/n
            d1[s]=avg
	    
    print("PASSED")
    d3 = [(k, d1[k]) for k in sorted(d1, key=d1.get, reverse=True)]
    for key,value in d3: 
         print(key)
    print("FAILED")
    for i in d2:
        print(i)



if __name__=="__main__":
    passorfail()
