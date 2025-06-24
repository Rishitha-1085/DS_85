# BALANCED

def isBalanced(s):
    stack=[]
    bracketDict= {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }
    for b in s:
        if b in bracketDict and stack and bracketDict[b] == stack[-1]:
            stack.pop()
        else:
            stack.append(b)
    if stack:
        return("No")
    else:
        return("Yes")
s="{( )})"
ans = isBalanced(s)
print(ans)
