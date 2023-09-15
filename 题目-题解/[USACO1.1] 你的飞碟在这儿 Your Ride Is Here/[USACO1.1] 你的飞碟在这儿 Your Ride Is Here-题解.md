（*有同学说我代码太长了，于是于2018.12.18简化了代码，麻烦管理员重审一下...*）

一道挺简单的题的呢...刚刚接触noip的时候难得我吃xiang，现在回头一看，真的感觉不一样了
#用string就好了，再注意一下ASCII的转换，就轻松ac啦

      #include <iostream>
      #include <cstring>
      using namespace std ;
      
      string a , b ;
      int ans = 1 , num = 1 ; \/\/这里要注意起始值必须为1，要是0的话所有的数乘出来都是0了....

      main(){
          cin >> a >> b ; \/\/ 输入
          for( int i = 0 ; i < a.length() ; i ++ ) ans *= a[i] - '@' ; 
          \/\/ @的编号为64 ，A的编号65-@的编号64不就是所对应的英语字母序号了嘛...
          for( int i = 0 ; i < b.length() ; i ++ ) num *= b[i] - '@' ; 
          \/\/ 同上
          ans %= 47 , num %= 47 ; \/\/ 根据题意，mod 47
          if( ans == num ) cout << "GO" ; 
          else cout << "STAY" ; \/\/输出
          return 0 ; \/\/完美结束
      }
PS:如果不知道@的ASCII的值的话，可以直接减A的ASCII码然后再+1（其实是一个效果啦...）