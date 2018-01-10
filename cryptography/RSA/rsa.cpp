#include <iostream>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#define ll long long
using namespace std;

int Plaintext[100];//明文
ll Ciphertext[100];//密文
int n, e = 0, d;

//二进制转换
int binTransform(int num, int bin[])
{

    int i = 0,  mod = 0;

    //转换为二进制，逆向暂存temp[]数组中
    while(num != 0)
    {
        mod = num%2;
        bin[i] = mod;
        num = num/2;
        i++;
    }

    //返回二进制数的位数
    return i;
}

//反复平方求幂
ll powMod(ll a, int b, int n)
{
    int c = 0, bin[1000];
    ll d = 1;
    int k = binTransform(b, bin)-1;

    for(int i = k; i >= 0; i--)
    {
        c = 2*c;
        d = (d*d)%n;
        if(bin[i] == 1)
        {
            c = c + 1;
            d = (d*a)%n;
        }
    }
    return d;
}

//生成1000以内素数
int genPrime(int prime[])
{
    int c = 0;
	bool vis[1001];
    memset(vis, 0, sizeof(vis));
    for(int i = 2; i <= 1000; i++)
		if(!vis[i])
	    {
	        prime[c++] = i;
	        for(int j = i*i; j <= 1000; j+=i)
	            vis[j] = true;
	    }

    return c;
}


//欧几里得扩展算法
int egcd(int m,int n,int &x)
{
    int x1,y1,x0,y0, y;
	y0 = x1 = x = 0;
	x0 = y1 = y = 1;
    int r=m%n;
    int q=(m-r)/n;
    while(r)
    {
        x=x0-q*x1; y=y0-q*y1;
        x0=x1; y0=y1;
        x1=x; y1=y;
        m=n; n=r; r=m%n;
        q=(m-r)/n;
    }
    return n;
}

//RSA初始化
void RSA_Init()
{
    //取出1000内素数保存在prime[]数组中
    int prime[200];
    int cntPrime = genPrime(prime);
	cout << "\n\n\n";
	// for(int i = 0; i < 5000; i++)
		// cout << prime[i] << " ";
	// cout << "\n\n\n";

    //随机取两个素数p,q
    srand((unsigned)time(NULL));
    int ranNum1 = rand() % cntPrime;
    int ranNum2 = rand() % cntPrime;
    int p = prime[ranNum1], q = prime[ranNum2];

    n = p * q;

    int On = (p - 1) * (q - 1);


    //用欧几里德扩展算法求e,d
	//保证e足够大
    for(int j = 3; j < On; j+=1331)
    {
        int gcd = egcd(j, On, d);
        if( gcd == 1 && d > 0)
        {
            e = j;
            break;
        }

    }

}

//RSA加密
void Encrypt()
{
    cout<<"Public Key (e, n) : e = "<<e<<" n = "<<n<<'\n';
    cout<<"Private Key (d, n) : d = "<<d<<" n = "<<n<<'\n'<<'\n';

    int i = 0;
    for(i = 0; i < 100; i++)
        Ciphertext[i] = powMod(Plaintext[i], e, n);

    cout<<"Use the public key (e, n) to encrypt:"<<'\n';
    for(i = 0; i < 100; i++)
        cout<<Ciphertext[i]<<" ";
    cout<<'\n'<<'\n';
}

//RSA解密
void Decrypt()
{
    int i = 0;
    for(i = 0; i < 100; i++)
        Ciphertext[i] = powMod(Ciphertext[i], d, n);

    cout<<"Use private key (d, n) to decrypt:"<<'\n';
    for(i = 0; i < 100; i++)
        cout<<Ciphertext[i]<<" ";
    cout<<'\n'<<'\n';
}


//算法初始化, 生成100个不大于1000的整数
void Init()
{
    srand((unsigned)time(NULL));
    cout<<"Generate 100 random numbers:"<<'\n';
    for(int i = 0; i < 100; i++)
	{
        Plaintext[i] = rand()%1000;
        cout<<Plaintext[i]<<" ";
	}

	cout << "\n";
}

int main()
{
    Init();
    while(!e)
        RSA_Init();

    Encrypt();

    Decrypt();

    return 0;
}
