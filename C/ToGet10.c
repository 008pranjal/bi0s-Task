#include<stdio.h>

void ToGet10() {
    int prev;
    int sum=0;
    int count=0; 
    float avg =0;
    scanf("%d",&prev);
    int m [prev];
    for(int i=0;i<prev;i++)
    { 
        scanf("%d",&m[i]);
    }
    for(int i=0;i<prev;i++)
    { 
       sum+=m[i]; 
    }
    for(int i=1;;i++)
     {
         avg = (float)(sum+(10*i))/(2+i);
         count = i;
         if(avg>=9.5)
          break;
     }
     printf("%d",count);
    
    }

int main() {
    ToGet10();
    return 0;
}


