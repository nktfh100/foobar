

# The cake is not a lie!
# ======================

# Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big trouble. 

# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string:
#  each possible letter (between a and z) corresponds to a unique color, 
# and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

# Write a function called solution(s) that,
#  given a non-empty string less than 200 characters in length describing the sequence of M&Ms,
#  returns *the maximum number of equal parts* that can be cut from the cake without leaving any leftovers.

# =========

def count_substring(s, substr):
    if(len(s) == 1):
        if(s == substr):
            return 1
        return 0
    if(substr == ""): # TODO
        return 0
    return len(s.split(substr)) - 1

def has_left_overs(s, substr):
    substr_count = count_substring(s, substr)
    if(substr_count * len(substr) != len(s)):
        return True
    return False

def solution(s):
    solution = 0

    for i in range(0, len(s)):
        for i2 in range(0, len(s)):
            substr = s[i:i2 + 1]
            if(substr == ""):
                continue
            if(has_left_overs(s, substr)):
                continue
            substr_count = count_substring(s, substr)
            if(substr_count > solution):
                solution = substr_count
    return solution
            

if __name__ == "__main__":
    cases = [
        ("abcabcabcabc", 4),
        ("abccbaabccba", 2),
        ("abcdaabcdaabcda", 3),
        ("abc", 1),
        ("a", 1),
        ("aa", 2),
        ("abcdea", 1),
    ]
    
    for case in cases:
        print("Testing", case[0], "==", case[1] , "OK" if solution(case[0]) == case[1] else "FAIL")
