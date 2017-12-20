#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <unordered_set>
#include <queue>
#include <algorithm>

using namespace std;

/* Prob: input=(str1,str2)
 * Find smallest sub-string from parent string containing all
 * elements from str2
 *
 * Logic: Sliding window approach
 * Prepare char map of str2 (one time only)
 * Find a window which satisfies the condition
 * Check if we can reduce the window size: remove elements from the front
 * if it is not in str 2 "map2[str1_i]==0"
 * or char count is greater than what is required "map1[str1_i]>map2[str1_i]: map1[str1_j]--"
 * do i++ till the first element which violates the above condition
 * This i marks the start of smalles window SO FAR!!
 * Time complexity: O(n) 'coz traversing the bigger string only once! 
 */

string getSmallestWindow(string str1, string str2) {
    int n = str1.length();
    int m = str2.length();
    
    if (n<m) return "";

    int map1[256] = {0};
    int map2[256] = {0};
    for (int i=0;i<m;i++)
        map2[str2[i]]++;

    int i_max = -1, min_len = INT_MAX;
    int start = 0;
    int count = 0;
    for (int j=0;j<n;j++) {
        map1[str1[j]]++;

        if (map2[str1[j]]!=0 && map1[str1[j]]<=map2[str1[j]])
            count++;

        if (count==m) {
            //Window Found
            /* while condition: remove elements from start of window 
             * which are either not in str2 or occur more than str2 */
            while (map1[str1[start]]>map2[str1[start]] || map2[str1[start]]==0) {
                if (map1[str1[start]]>map2[str1[start]])
                    map1[str1[start]]--;
                start++;
            }
            if (j-start+1<min_len) {
                min_len = j-start+1;
                i_max = start;
            }
        }
    }
    if (i_max==-1) return "";
    else return str1.substr(i_max,min_len);
}

int main () {
	string str1 = "this is a test string";
    string str2 = "esstri";
    string smallestSub = getSmallestWindow(str1,str2);
    cout << smallestSub << endl;
}



