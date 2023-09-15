#### 写这篇题解,我只想告诉大家,

#### 有一个东西叫做,


## \_\_gcd(x,y);

干什么用的呢？

gcd认识吧，这玩意儿就是求x,y的最大公约数的~

有没有觉得逼格满满！

用于这种约分题目异常简单！


``` cpp
#include<iostream>
#include<cstdio>
#include<algorithm> \/\/就我所知，__gcd()应该在这里面
#include<string>
#include<cstring>

using namespace std;

int a1,a2,b1,b2;
char spc;

int main()
{
    scanf("%d",&a1); spc=getchar(); scanf("%d",&b1); 
    \/\/spc用于读掉除号
    scanf("%d",&a2); spc=getchar(); scanf("%d",&b2);
    int c1=a1*a2,c2=b2*b1;
    printf("%d %d\n",c2 \/ __gcd(c1,c2),c1 \/ __gcd(c1,c2)); 
    \/\/约分
    return 0;
}

```