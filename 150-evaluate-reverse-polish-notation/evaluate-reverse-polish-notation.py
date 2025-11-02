class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+','-','*','/']
        stack=[]
        for symbol in tokens:
            if symbol in op:
                op1=stack.pop()
                op2=stack.pop()
                if symbol=='+':
                    stack.append(op1+op2)
                elif symbol=='-':
                    stack.append(op2-op1)
                elif symbol=='*':
                    stack.append(op2*op1)
                elif symbol=='/':
                    stack.append(int(op2 / op1))
            else:
                stack.append(int(symbol))

        return stack[-1]