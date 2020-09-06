
#include <iostream>

using namespace std;

class Kmp
{
private:
    int *next;

public:
    Kmp(/* args */);
    int *GetNext(string p);
    int Find(string s, string p);
    ~Kmp();
};

Kmp::Kmp(/* args */)
{
}

Kmp::~Kmp()
{
    // free(this->next);
}

int *Kmp::GetNext(string p)
{
    int n = p.length();
    this->next = new int[n];
    this->next[0] = -1;

    for (int i = 0, j = -1; i < p.length() - 1;)
    {
        if (j == -1 || p[i] == p[j])
        {
            i++;
            j++;
            this->next[i] = j;
        }
        else
        {
            i++;
            j = this->next[j];
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     cout << this->next[i] << " ";
    // }
    // cout << endl;
    return this->next;
}

int Kmp::Find(string s, string p)
{
    int pos = -1;
    int i = 0, j = 0;
    if (s.length() == 0 || p.length() == 0 || p.length() > s.length())
    {
        return -1;
    }

    this->next = this->GetNext(p);

    while (j < p.length())
    {
        if (s[i] == p[j])
        {
            i++;
            j++;
            if (j == p.length()){
                pos = i - j;
                return pos;
            }
        }
        else
        {
            j = this->next[j];
            if (j == -1)
            {
                j++;
                i++;
            }
            if (s.length() - i < p.length() - j){
                return -1;
            }
        }
    }

    return pos;
}

int main(int argc, char const *argv[])
{
    Kmp k;
    cout << k.Find("abcdaaaabcabcdebbb", "abcabcde") << endl;
    return 0;
}
