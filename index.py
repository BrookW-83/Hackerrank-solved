class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        def is_num(s):
                try:
                        int(s)
                        return True
                except:
                        return False
        for n in tokens:
                
                if is_num(n):
                        stack.append (n)
                else:
                        a = int(stack.pop())
                        b = int(stack.pop())
                        
                        if n =="+" :
                                c = a + b
                        elif n== "-":
                                c= b - a
                        elif n== "*" :
                                c= b* a
                        elif n== "/":
                                c=int(b/a)
                                
                        stack.append(c)
        return stack[-1]
                