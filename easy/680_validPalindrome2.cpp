#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

/*
* We have to find if we can del a char and make is a valid palindrome.
* Same logic, recursive function call
* However, we maintain if we have already deleted a char or not.
* P.S. Don't use substr function to pass substrings, not memory efficient
* instead work with the same string and index next to match!
*/

class Solution {
public:
    bool validPalindrome(string s) {
        if (s.length()<=2) return true;
        return validPalindromeHelper(s,0,s.length()-1,false);
    }
    
    bool validPalindromeHelper(string &s, int i, int j, bool del) {
        if (i==j)
            return true;
        if (s[i]==s[j]) {
            if (i==j-1) 
                return true;
            else
                return validPalindromeHelper(s,i+1,j-1,del);
        }
        else {
            if (del==true) 
                return false;
            else {
                return validPalindromeHelper(s,i,j-1,true)
                        || validPalindromeHelper(s,i+1,j,true);
            }
        }
    }
};

int main () {
	string str = "junkjunk";
    Solution* s = new Solution();
    cout << "input:" << str << "\t output:" << s->validPalindrome(str) << endl;
    str = "abca";
    cout << "input:" << str << "\t output:" << s->validPalindrome(str) << endl;
    return 0;
}



