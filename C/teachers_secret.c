#include<stdio.h>
#include<string.h>

void teachers_secret() {
    int n;
    char *check;
    int marks=0;
    scanf("%d",&n);
    char s[n][10];
    for(int i=0;i<n;i++)
     scanf("%s",s[i]);
     
    int m[n];
    for(int i=0;i<n;i++)
    scanf("%d ",&m[i]);
    
    char ans[100];
    fgets(ans, sizeof(ans), stdin);
    printf("%s",ans);

    for(int i=0;i<n;i++)
    {check = strstr(ans,s[i]);
       if(check!=NULL)
         marks+=m[i];

     }
      printf("%d",marks);
     
}

int main() {
    teachers_secret();
    return 0;
}
