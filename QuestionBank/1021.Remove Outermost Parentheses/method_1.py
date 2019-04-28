#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/24 10:05
# @Author   : cancan
# @File     : method_1.py
# @Function : 删除最外层的括号

"""
Question:
有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。

Example 1：
输入："(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。

Example 2：
输入："(()())(())(()(()))"
输出："()()()()(())"
解释：
输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
删除每隔部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。

Example 3：
输入："()()"
输出：""
解释：
输入字符串为 "()()"，原语化分解得到 "()" + "()"，
删除每个部分中的最外层括号后得到 "" + "" = ""。

Note：
S.length <= 10000
S[i] 为 "(" 或 ")"
S 是一个有效括号字符串
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        n = 0
        ret = ''

        for i, v in enumerate(S):
            if v == '(':
                n += 1
                if n > 1:
                    ret += v
            else:
                n -= 1
                if n > 0:
                    ret += v

        return ret