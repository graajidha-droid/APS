class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length=0
        seen=set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            current_length=right-left+1
            if current_length>max_length:
                max_length=current_length
        return max_length