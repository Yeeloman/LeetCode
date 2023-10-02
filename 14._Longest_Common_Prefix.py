class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        min_word = min(strs, key=len)
        for i, char in enumerate(min_word):
            for word in strs:
                if char != word[i]:
                    return word[:i]
        return min_word
