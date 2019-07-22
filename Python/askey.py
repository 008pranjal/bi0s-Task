def askey():
    a,b=input().split(' ')
    c = list(a)
    d = list(b)
    s1 = 0;s2=0
    for i in c:
        s1+=ord(i)
    for j in d:
        s2+=ord(j)
    if s1 == s2:
        print("They are equal")
    else:
        print("They are not equal")            

if __name__=="__main__":
    askey()
