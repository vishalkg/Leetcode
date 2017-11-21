# Base case: when len(digits)=2
# Else: call recursively with digits[1:]
# combine digits[0] with returned list
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    d = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }
    
    if digits=='':
        return []
    if len(digits) == 1:
        return list(d[digits[0]])
    
    result = []
    if len(digits)==2:
        for char1 in list(d[digits[0]]):
            for char2 in list(d[digits[1]]):
                result.append(char1+char2)
    else:
        sub_list = letterCombinations(digits[1:])
        for char in list(d[digits[0]]):
            for str in sub_list:
                result.append(char+str)
    return result

result = letterCombinations("243")
print (result)

'''
Output: ['agd', 'age', 'agf', 'ahd', 'ahe', 'ahf', 'aid', 'aie', 'aif', 'bgd', 'bge', 'bgf', 'bhd', 'bhe', 'bhf', 'bid', 'bie', 'bif', 'cgd', 'cge', 'cgf', 'chd', 'che', 'chf', 'cid', 'cie', 'cif']
'''
