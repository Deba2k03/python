#include<stdio.h>
void main()
{   
    int a,i,j,k=1;
    printf("Enter a number:");
    scanf("%d",&a);
    // int u=2*a-1;
    for ( i = 1; i<=a; i++)
    {
        for ( j = 1; j<=2*a;j++)
        {   
            if ((i==j) || ((i+j)==2*a))
            {
                printf("%d",k);
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
        k+=1;
    }
    k=a-1;
    for ( i = a-1; i>0; i--)
       {
         for ( j = 2*a; j>0;j--)
         {   
             if ((i==j) || ((i+j)==2*a))
             {
                 printf("%d",k);
             }
             else
             {
                 printf(" ");
             }
         }
         printf("\n");
          k-=1;
        }
    
    
}