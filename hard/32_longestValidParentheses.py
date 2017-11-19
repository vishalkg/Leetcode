# Maintain a stack of indices which are not a part of balanced sub-string
# Calculate the max length as differences of those indices
def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s=='(' or s == ')':
            return 0
        stack = []
        for i, char in enumerate(s):
            if char=='(':
                stack.append(i)
            else:
                if len(stack)!=0:
                    if s[stack[-1]] == '(':
                        stack.pop(-1)
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        longest = 0
        if stack==[]:
            longest = len(s)
        else:
            a = len(s); b = 0
            for i in range(len(stack)-1,-1,-1):
                b = stack[i]
                longest = max(longest, a-b-1)
                a = b            
            longest = max(longest,a)
        return longest