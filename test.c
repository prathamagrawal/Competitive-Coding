#include <stdio.h>

struct emp{
    int sno;
    char sname[100];
}s[2];

int main()
{
    FILE *ptr;
    char temp[100];
    char filename[]="test.txt";
    ptr = fopen(filename,"w");
    for (int i=0; i<2; i++){
        printf ("enter details of student %d\n", i+1);
        printf("student number:");
        scanf("%d",&s[i].sno);
        printf("student name:");
        gets(s[i].sname);
        fwrite(&s[i], sizeof(s[i]),1,ptr);
    }
    fclose(ptr);
}
