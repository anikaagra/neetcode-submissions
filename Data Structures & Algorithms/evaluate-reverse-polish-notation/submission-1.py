class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["*", "+", "-", "/"])
        stack = []

        for token in tokens:
            if token in operators:
                first = stack.pop()
                sec = stack.pop()
                if token == "*":
                    stack.append(int(first) * int(sec))
                elif token == "/":
                    stack.append(int(sec) // int(first))
                elif token == "+":
                    stack.append(int(first) + int(sec))
                elif token == "-":
                    stack.append(int(sec) - int(first))
            else:
                stack.append(int(token))

        return stack.pop()