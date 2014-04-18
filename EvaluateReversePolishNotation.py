"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        temp = []
        operations = {
            '+': (lambda x,y: x+y),
            '-': (lambda x,y: x-y),
            '*': (lambda x,y: x*y),
            '/': (lambda x,y: x/y if x/y>=0 or x%y==0 else x/y+1)
        }
        for element in tokens:
            if element not in operations:
                temp.append(element)
            else:
                latter = int(temp.pop())
                former = int(temp.pop())
                temp.append(operations[element](former, latter))
        return int(temp[0])