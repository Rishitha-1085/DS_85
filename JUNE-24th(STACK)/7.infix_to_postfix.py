# CONVERSION OF INFIX TO POSTFIX EXPRESSION
OPERATORS=set(['+','-','*','/',(', '),'^'])    #set of operators
PRIORITY={'+':1,'-':1,'*':2,'/':2,'^':3}          #dictionary having priorities

def infix_to_postfix(expression):   #input expression
    stack=[]        #initially stack empty
    output=''       #initially output empty
    for ch in expression:
        if ch not in OPERATORS and ch not in ('(', ')'):   #if an operand(data item) then put it directly in postfix
            output+=ch
        elif ch=='(':              #else operators should be  put in stack
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:            # lessor priority cann't be on top higher or equal priority
                        # so pop and put in output
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:    #stack[-1]=top
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
expression=input('Enter infix expression: ')
print('infix expression: ',expression)
print('Postfix Expression: ',infix_to_postfix(expression))