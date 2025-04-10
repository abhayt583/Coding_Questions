class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.size();
        vector<vector<bool>>dp(n,vector<bool>(n));
        for(int i=0;i<n;i++)
        {
            dp[i][i]=true;
        }
        auto ans=make_pair(0, 0);
        for(int i=0;i<n-1;i++)
        {
            if(s[i]==s[i+1])
            {
                dp[i][i+1]=true;
                ans.first=i;
                ans.second=i+1;
            }
        }
        for(int diff=2;diff<n;diff++)
        {
            for(int i=0;i<n-diff;i++)
            {
                int j=i+diff;
                if(s[i]==s[j] && dp[i+1][j-1])
                {
                    dp[i][j]=true;
                    ans.first=i;
                    ans.second=j;
                }
            }
        }
        int i=ans.first;
        int j=ans.second;
        return s.substr(i,j-i+1);
    }
};