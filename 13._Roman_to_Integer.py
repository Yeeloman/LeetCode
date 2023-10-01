class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        pre_val = 0
        rom_num = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
        for char in reversed(s):
            val = rom_num[char]
            if val < pre_val:
                result -= val
            else:
                result += val
            pre_val = val
        return result

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0
#         rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
#         for i in range(len(s) - 1):
#             if rom_num[s[i]] < rom_num[s[i + 1]]:
#                 result -= rom_num[s[i]]
#             else:
#                 result += rom_num[s[i]]
#         result += rom_num[s[-1]]
#         return result
