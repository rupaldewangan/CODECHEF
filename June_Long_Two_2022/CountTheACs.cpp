#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int p;
        cin>>p;
        if(p>100)
        {
            if(p/100>0)
            {
                if(p/100+p%100 <=10)
                    cout<<p/100+p%100;
                else
                    cout<<-1;
            }
        }
        else if (p>=0 && p<=10)
            cout<<p;
        else
            cout<<-1;
    }
    return 0;
}
    