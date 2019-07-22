def decrypt():
    a=input()
    i=1
    s=''
    for j in a:
        if i%2!=0:
            if j==' ':
                s = s + j
            elif  j.isupper():
                s = s + chr((ord(j) + 13 - 65) % 26 + 65)
            else:
                s = s + chr((ord(j) + 13 - 97) % 26 + 97)
        else:
            s = s + j
        i+=1        
    print(s)






if __name__=="__main__":
    decrypt()

