def lengthOfLongestSubstring(s: str) -> int:
    tempSubstring = ""
    longestSubstring = ""
    for index, x in enumerate(s):
        for y in range(index, len(s)):      
            if(s[y] not in tempSubstring):
                tempSubstring = tempSubstring + s[y]
                
                if len(longestSubstring) == 0: 
                    longestSubstring = tempSubstring
                elif(len(longestSubstring) < len(tempSubstring)): 
                    longestSubstring = tempSubstring
            else:
                tempSubstring = ""

    return len(longestSubstring)

print("Test Case 1: ", lengthOfLongestSubstring("abcabcbb") == 3)
print("Test Case 2: ", lengthOfLongestSubstring("bbbbb") == 1)
print("Test Case 3: ", lengthOfLongestSubstring("pwwkew") == 3)
print("Test Case 4: ", lengthOfLongestSubstring("dvdf") == 3)
print("Test Case 5: ", lengthOfLongestSubstring("jbpnbwwd") == 4)