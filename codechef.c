#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int * testcases=(int *)malloc(sizeof(int));
    scanf("%d", testcases);
    while(*testcases--){
        int flag=0;
        char str[100];
        scanf("%s", str);
        for (int i=0; i<strlen(str); i++){
            if(strcmp(&str[i], &str[i+1])==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==1){
            printf("Yes");

        }
        else{
            printf("No");
        }
    }

}