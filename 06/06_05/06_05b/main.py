from collections import deque

def match_parentheses(expression):
    stack = deque(expression)
    right = []
    left = []
    while stack:
      last = stack.pop()
      if last == ')':
        right.append(last)
      elif last == '(':
        left.append(last)
  
    if len(right) == len(left):
     return True
    else:
     return False
            
print("sholud true",match_parentheses("(test)"))
print("sholud false", match_parentheses("(test"))
print("sholud true",match_parentheses("((test))"))
print("sholud false",match_parentheses(")test))"))
print("sholud false",match_parentheses("(test))"))
print("sholud false",match_parentheses("() PK )"))
print("sholud false",match_parentheses("(() PK )"))
