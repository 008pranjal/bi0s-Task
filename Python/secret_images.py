def secret_images():
    n=int(input())
    png=0
    bmp=0
    jpeg=0
    count=0
    f= open("secret_images.txt","r")
    for i in range(0,n):
        for i in f:
            
            if (count>n):
                break
            elif ".png" in str(i):
                png+=1
            elif ".bmp" in str(i): 
                bmp+=1
            elif ".jpeg" in i:
                jpeg+=1
            count+=1    
            
    print(png)  
    print(bmp)
    print(jpeg)              


if __name__=="__main__":
    secret_images()

