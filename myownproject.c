#include<stdio.h>
int main()
{
    struct createrecord
    {
        char name[20];
        int rollno;
        float marks;
    }r[11]={"x"};

    FILE *mp;
    int i,i1,i2;
    start:
    printf("\npress:-\n 1- create record\n 2- search record\n 3- modify record\n 4- delete record\n 5- show records\n 6- to save record \n 7- to exit.\n your input- ");
    scanf("%d",&i);
    switch (i)
    {
    case 1:
        printf("\n (max 10)  no of students data, you want to enter- ");
        scanf("%d",&i1);
        for (int i = 1; i <= i1; i++)
        {
            printf("\n(donot use space instead use '_')\nname of student%d- ",i);
            
            scanf("%s",&r[i].name);
            fflush;
            
            printf("\nroll no of student%d- ",i);
            scanf("%d",&r[i].rollno);

            printf("\nmarks obtained by student%d- ",i);
            scanf("%f",&r[i].marks);

            
            
        }
        goto start;
        
        break;
    case 2:
        printf("enter roll of student- ");
        scanf("%d",&i2);
        int count=0;
        for (int i = 1; i <= 10; i++)
        {
            if(r[i].rollno==i2){
                    printf("student name is- %s\n",r[i].name);
                    
                    printf("student marks is- %f\n",r[i].marks);
            }
            else{
                count+=1;
            }
            
        }
        if (count==10){
            printf("\n --------no data found---------\n");
        }
        goto start;
        break;
    case 3:
        printf("enter roll no.- ");
        int i3;
        scanf("%d",&i3);
        for (int i = 1; i <= 10; i++)
        {
            if(i3==r[i].rollno){
                printf("\nname of student- ");
                scanf("%s",&r[i].name);
                fflush;
                printf("\nmarks obtained by student- ");
                scanf("%f",&r[i].marks);
            }
        }
        
        goto start;
        break;
    case 4:
        
        printf("\nenter roll no- ");
        int i4,count1=0;
        scanf("%d",&i4);
        for (int i = 1; i <= 10; i++)
        {
            if(i4==r[i].rollno){
                r[i].rollno=0;
                
            }
            else{
                count1+=1;
            }

        }
        if(count1==10){
            printf("-------no data found--------");
        }
        printf("\ndata deleted");

        goto start;
        break;
    case 5:

        for (int i = 1; i <= 10; i++)
        {
            if(r[i].rollno==0){
                continue;
            }
            else{
                printf("\nname of student- %s",r[i].name);
                printf("\nroll no of student- %d",r[i].rollno);
                printf("\nmarks of student- %f",r[i].marks);
                printf("\n--------------------------------------------------");
            }
        }
        goto start;
    case 6:
        
        mp=fopen("myproject.txt","a");
           for (int i = 1; i <= 10; i++)
        {
            if(r[i].rollno==0){
                continue;
            }
            else{
                fprintf(mp,"\nname of student- %s",r[i].name);
                fprintf(mp,"\nroll no of student- %d",r[i].rollno);
                fprintf(mp,"\nmarks of student- %f",r[i].marks);
                fprintf(mp,"\n--------------------------------------------------");
            }
        }
        printf("Record saved");
        fclose(mp);
        goto start;
            
    case 7:
        goto end;
    default:
        printf("\ninvalid input");
        break;
    }
    end:
    printf("\n-----Thanks for using it-----------");

    return 0;
}

