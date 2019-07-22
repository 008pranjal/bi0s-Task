def jumbled_letters():
    n=int(input())

    for i in range(0,n):
        odd=''
        even=''
        s=input()
        s1=s.replace(" ","")
        j=1
        for i in s1:
            if j%2==0:
                even+=str(i)
            else:
                odd+=str(i)
            j+=1
        print(odd+even[::-1])
               

       
        
if __name__=="__main__":
    jumbled_letters()