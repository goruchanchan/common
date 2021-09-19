#include<stdio.h>
#define N 5

void swap(int *a,int *b)
{
    int tmp = *a;
    int tmp2 = *b;

    if(tmp > tmp2)
    {
        *a = tmp2;
        *b = tmp;
    }
}

void shortSort(int *a)
{
    int i,j;
    for(i=0;i<N;i++)
    {
        for(j=0;j<(N-1);j++)
        {
            swap(&a[j],&a[j+1]);
        }
    }
}

void bigSort(int *a)
{
    int i,j;
    for(i=0;i<N;i++)
    {
        for(j=N;j>1;j--)
        {
            swap(&a[j-1],&a[j-2]);
        }
    }
}

int main()
{
    int i = 0;
    int a_var[N] = {0};

    for(i=0;i<N;i++)
    {
        scanf("%d",&a_var[i]);
    }

    shortSort(a_var);
    printf("shortSort\n");
    for(i=0;i<N;i++)
    {
        printf("%d\n",a_var[i]);
    }

    bigSort(a_var);
    printf("bigSort\n");
    for(i=0;i<N;i++)
    {
        printf("%d\n",a_var[i]);
    }


}