class Solution {
public:
    bool isPalindrome(int x)
{
    long int num,rem,rev=0;
    num=x;
    if(x<0)
    {
        return false;
    }
    else
    {
        while(num!=0)
        {
            rem=num%10;
            rev=rev*10+rem;
            num/=10;
        }
        if(rev==x)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
};