"""
A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Given two strings source and target, return the minimum number of subsequences of source
such that their concatenation equals target. If the task is impossible, return -1.
Example 1:
Input: source = "abc", target = "abcbc"Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of
source "abc".
Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string
due to the character "d" in target string.
Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
"""

from collections import defaultdict


#   贪心
#   对target串不断扫描，每次都在源串里找子串，尽可能多的向target后找
#   空串也是子串，target是空，也得是source的子串构成，1
#   有个很极端的问题，每次find都是到最后一个，那么就是O(n*m)的复杂度
#   可以做个哈希，记录每个字符出现的位置
def minimum_subsequence(source, target) -> int:
    ans = 1
    i = 0
    record = defaultdict(set)
    for c in target:
        #   find找到的是第一个，然后直接跳到find找到的位置+1
        l = list(record[c])
        l.sort()
        for j in l:
            if j >= i:
                i = j
                break
        i = source.find(c, i) + 1

        # 没找到,可能是要重来
        if i == 0:
            if record.get(c) is not None:
                for j in record[c]:
                    if j >= i:
                        i = j
                        break
            i = source.find(c, i) + 1
            if i == 0:
                return -1
            else:
                if c == target[0] and (0 not in record[c]):
                    record[c].add(0)
            ans += 1
        else:
            if i - 1 not in record[c]:
                record[c].add(i - 1)
    return ans


source = input("请输入source串:")
target = input("请输入target串:")
ans = minimum_subsequence(source, target)
print(ans)
