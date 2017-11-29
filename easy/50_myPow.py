# Simple recursion
# Only edge case to be taken care of is n<0

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n==0:
        return 1
    if n<0:
        n = -1*n
        x = 1/x
    if n%2 == 0: return self.myPow(x*x,n/2)
    else: return x*self.myPow(x*x,(n-1)/2)