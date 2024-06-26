# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1unFvdj7vD0RR6rVefUloO76uHNpoZAzO

**postfix** *(후위연산식)* **calculator** *(계산기)*
"""

class ListStack:
	def __init__(self):
		self.__stack = []

	def push(self, x):
		self.__stack.append(x)

	def pop(self):
		return self.__stack.pop()

	def top(self):
		if self.isEmpty():
			return None
		else:
			return self.__stack[-1]

	def isEmpty(self) -> bool:
		return not bool(self.__stack)

	def popAll(self):
		self.__stack.clear()

	def printStack(self):
		print("Stack from top:", end = ' ')
		for i in range(len(self.__stack)-1, -1, -1):
			print(self.__stack[i], end = ' ')
		print()

def evaluate(p):
	s = ListStack()
	digitPreviously = False
	for i in range(len(p)):
		ch = p[i]
		if ch.isdigit():
			if digitPreviously:
				tmp = s.pop()
				tmp = 10 * tmp + (ord(ch) - ord('0'))

				s.push(tmp)
			else:
				s.push(ord(ch) - ord('0'))
				digitPreviously = True
		elif isOperator(ch):
			s.push(operation(s.pop(), s.pop(), ch))
			digitPreviously = False
		else:
			digitPreviously = False
	return s.pop()

def isOperator(ch) -> bool:
	return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(opr2:int, opr1:int, ch) -> int:
		return {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2}[ch]

def main():
	postfix = "  "
	print("Input string: ", postfix);
	answer = evaluate(postfix)
	print("Answer: ", answer)

if __name__ == "__main__":
	main()

"""**checkbrackets** *(괄호검사)*"""

class ArrayStack :
    def __init__( self, capacity ):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty( self ) :
       return self.top == -1

    def isFull( self ) :
       return self.top == self.capacity-1

    def push( self, item ):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass
    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass

    def peek( self ):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

    def __str__(self ) :
        return str(self.array[0:self.top+1][::-1])

    def size( self ) : return self.top+1

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        # if ch in ('{', '[', '('):
        # if ch in '{[(':
        if ch=='{' or ch=='[' or ch=='(' :
            stack.push(ch)
        # elif ch in ('}', ']', ')'):
        # elif ch in '}])':
        elif ch=='}' or ch==']' or ch==')' :
            if stack.isEmpty() :
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False

    return stack.isEmpty()

s1 = " 입력 "
print(s1, " ---> ", checkBrackets(s1))

# Commented out IPython magic to ensure Python compatibility.
# %%writefile postbracket/postbrack.py