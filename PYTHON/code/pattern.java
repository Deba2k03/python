import java.util.Scanner;
public class pattern
{
    public static void main(String args[])
    {   
        try
        {
            int k=1;
            System.out.print("Enter n:");
            Scanner Sc=new Scanner(System.in);
            int a=Sc.nextInt();
            for(int i=1;i<=a;i++)
            {
                for(int j=0;j<2*a;j++)
                {
                    if(i==j || i+j==2*a)
                    {
                        System.out.print(k);
                    }
                    else
                    {
                        System.out.print(" ");
                    }
                }
                System.out.println();
                k+=1;
            }
            k=a-1;
            for(int i=a-1;i>0;i--)
            {
                for(int j=2*a;j>0;j--)
                {
                    if(i==j || i+j==2*a)
                    {
                        System.out.print(k);
                    }
                    else
                    {
                        System.out.print(" ");
                    }
                }
                System.out.println();
                k-=1;
            }
        }
        catch (Exception e) 
        {
           System.out.print(e);
        }
    }
}
