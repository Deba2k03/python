#include<stdio.h>
int k=9,l=9;
void main()
{
    for(int i=0;i<18;i+=2)
    {
        for (int j = 0; j <=i; j+=1)
         {  
             if(i==2*j)
             {
                   printf("0");
                   k=k-1;
             }
             if(i=2*j+1)
             {  
                 printf("9");
                 
             }
            //  else if((i+j)%2!=0)
            //  {
            //      printf("%d",l-=1);
            //  }
            //  else if()
         }
            printf("\n"); 
            k-=1;
    }
}