def stud_list():
    d=dict()
    a=int(input("No of records: "))
    for i in range(0,a):
        s=input("Enter Name: ")
        m=int(input("Enter Marks: "))
        d[s]=m
    lk=list(d.keys())
    lv=list(d.values())
    lv.sort(reverse=True)
    d1=dict(zip(lk, lv))
    print(d1)


     

    
    
    



if __name__=="__main__":
    stud_list()