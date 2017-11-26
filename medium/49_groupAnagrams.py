# Approach 1:
# Prepare character map of each word
# str(char_map): id
# hash_map[id] = [list of anagrams]
# However, we don't even need to make a character map
# Approach 2: sorted form of words which are anagrams will be same
# sorted(word): id
# Rest is all same

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    x = {}
    result = []
    for word in strs:
        '''char_map = [0]*26
        for char in word:
            char_map[ord(char)-97]+=1
        id = str(char_map)'''
        id = ''.join(sorted(word))
        if id not in x:
            result.append([word])
            x[id] = len(result)-1
        else:
            result[x[id]].append(word)
    return result

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
                