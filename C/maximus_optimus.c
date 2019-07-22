#include<stdio.h>

void maximus_optimus() {
    int a[3];
    int n;
    int p=0;
    int s=0;
    
    for(int i=0;i<3;i++)
    scanf("%d",&a[i]);
    
    scanf("%d",&n);

    for(int j=0;j<n;j++){
        int max = 0;
        for(int i=1;i<3;i++)
        {
             if(a[max]<a[i])
             max = i;
        }
        p+=a[max];
        a[max]--;
    }
    printf("%d",p);
    
    
}

int main() {
    maximus_optimus();
    return 0;
}
