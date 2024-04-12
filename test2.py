"""
每输入一个字符串，检查括号是否匹配。如果只有左括号没有右括号，我们就在它下面标一个x
，如果只有右括号，我们就在它下面标一个问号。每行为单独测试用例。
样例输入：
bge)))))))))
((IIII))))))
()()()()(uuu
))))UUUU((()
样例输出：
bge)))))))))
   ?????????
((IIII))))))
        ????
()()()()(uuu
        x
))))UUUU((()
????    xx
"""


#   栈匹配括号，最后补充x即可
#   时间复杂度O(n)，空间复杂度O(n)
def check_brackets(s):
    stack = []
    ans = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
            ans.append(" ")
        elif s[i] == ")":
            if stack:
                stack.pop()
                ans.append(" ")
            else:
                ans.append("?")
        else:
            ans += " "
    for i in stack:
        ans[i] = "x"
    return "".join(ans)


#   读文件也行其实，这里为了方便直接输入
num = int(input("请输入样例行数："))
record = []
ans = []
for i in range(num):
    s = input()
    record.append(s)
    ans.append(check_brackets(s))
for i in range(num):
    print(record[i])
    print(ans[i])
