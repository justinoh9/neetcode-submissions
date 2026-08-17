class Solution:
    def intToRoman(self, num: int) -> str:
        # basically correclty implement a butt load of conditionals
        # use a dict for the symbols
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], 
                    ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                    ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                    ["M", 1000]]

        res = ""
        #iterate through list in reverse order
        for sym, val in reversed(symList):
            if num // val: # integer div
                count = num // val
                res += (sym * count)
                num = num % val
        return res