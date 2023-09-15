# 题解 P1150

因为k个烟蒂=1根烟+1个烟蒂

所以k-1个烟蒂=1根烟

注意减掉最后一根烟的烟蒂

(因这题并没有借烟蒂换烟再还回这一说)

此解法为小学4~6年级水平


```cpp
     #include <bits\/stdc++.h>
     using namespace std;
     int main(){
         int n,k;
         cin>>n>>k;
         cout<<n+(n-1)\/(k-1);
         return 0;
     } 

```