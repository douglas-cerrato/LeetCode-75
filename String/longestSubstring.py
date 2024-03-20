def lengthOfLongestSubstring(s: str) -> int:
    # Declare tempSubstring to use for creating substrings, and longestSubString for comparison
    tempSubstring = ""
    longestSubstring = ""
    
    for index, x in enumerate(s):
        for y in range(index, len(s)):

            # add current variable we are looking at to tempSubstring
            # if there is no repeat     
            if(s[y] not in tempSubstring):
                tempSubstring = tempSubstring + s[y]
                
                # if longestSubstring is empty, populate with current tempSubstring we have
                if len(longestSubstring) == 0: 
                    longestSubstring = tempSubstring
                # if longestSubstring exists and it is smaller then our current tempSubstring
                elif(len(longestSubstring) < len(tempSubstring)): 
                    longestSubstring = tempSubstring
            else:
                # We found a duplicate in our tempSubstring
                # Reset temp to nothing and break out of this loop
                tempSubstring = ""
                break

    return len(longestSubstring)

print("Test Case 1: ", lengthOfLongestSubstring("abcabcbb") == 3)
print("Test Case 2: ", lengthOfLongestSubstring("bbbbb") == 1)
print("Test Case 3: ", lengthOfLongestSubstring("pwwkew") == 3)
print("Test Case 4: ", lengthOfLongestSubstring("dvdf") == 3)
print("Test Case 5: ", lengthOfLongestSubstring("jbpnbwwd") == 4)