class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["*", "+", "-", "/"])
        stack = []

        for token in tokens:
            if token in operators:
                first = stack.pop()
                sec = stack.pop()
                if token == "*":
                    stack.append(first * sec)
                elif token == "/":
                    stack.append(int(float(sec)/first))
                elif token == "+":
                    stack.append(first + sec)
                elif token == "-":
                    stack.append(sec - first)
            else:
                stack.append(int(token))

        return stack.pop()