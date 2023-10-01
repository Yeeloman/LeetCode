class Solution:
    def reverseWords(self, s: str) -> str:
        tokens = s.split()
        result = ""
        for word in tokens:
            reversed_word = word[::-1]
            print(reversed_word)
            if result == "":
                result = reversed_word
            else:
                result += " " + reversed_word
        return result
