def lengthOfLongestSubstring(s: str) -> int:
    tempSubstring = ""
    longestSubstring = ""
    for index, x in enumerate(s):
        if(x not in tempSubstring): 
            tempSubstring = tempSubstring + x       
            if len(longestSubstring) == 0: 
                longestSubstring = tempSubstring
            elif(len(longestSubstring) < len(tempSubstring)): 
                longestSubstring = tempSubstring
        else:
            tempSubstring = x
        
    return len(longestSubstring)


print("Test Case 1: ", lengthOfLongestSubstring("abcabcbb") == 3)
print("Test Case 2: ", lengthOfLongestSubstring("bbbbb") == 1)
print("Test Case 3: ", lengthOfLongestSubstring("pwwkew") == 3)
print("Test Case 4: ", lengthOfLongestSubstring("dvdf") == 3)