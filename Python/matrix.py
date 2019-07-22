import random


def matrix():
    c = list()   
    s = list()                                                          
    for i in range (0, 6):                               
        r = []              
        for m in range (0,6):
            r1=random.randint(0,10)
            r.append(int(r1))
            
        c.append(r)
    for a in c:
        print(a)

      

    for j in c:
        s.append(sum(j))
    print("Sum of rows: "+str(s))      
    maxi=s.index(max(s)) 
    s.pop(maxi)
    maxi2=s.index(max(s))
    
    print("Entry @ row"+str(maxi2))
    print("Exit @ row"+str(maxi))    








if __name__=="__main__":
    matrix()   