def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    
    if num1=='0' or num2=='0':
        return '0'
    if num1=='1' or num2=='1':
        return num1 if num2=='1' else num2
    
    if len(num2)>len(num1):
        num1,num2 = num2,num1
    
    def mult(str1,digit):
        ans = ''
        carry = 0
        digit = int(digit)
        for char in reversed(str1):
            temp = int(char)*digit+int(carry)
            if temp>=10:
                carry = temp//10
                temp = temp%10
            else:
                carry = 0
            ans = str(temp)+ans
        while carry>0:
            ans = str(carry%10)+ans
            carry = carry//10
        return ans
    
    def add(sum_sofar,product):
        ans = ''
        carry = 0
        i = len(sum_sofar)-1
        for char in reversed(product):
            if i>=0:#len(sum_sofar):
                temp = int(char)+int(sum_sofar[i])+carry
                i-=1
            else:
                temp = int(char)+carry
            if temp>=0:
                carry = temp//10
                temp = temp%10
            ans = str(temp)+ans
            #print(ans)
        while carry>0:
            ans = str(carry%10)+ans
            carry = carry//10
        return ans
            
    sum_sofar = ''
    product = ''
    for i, digit in enumerate(reversed(num2)):
        product = mult(num1,digit)
        for j in range(i):
            product += '0'
        #print(product)
        sum_sofar = add(sum_sofar,product)
    return sum_sofar
    