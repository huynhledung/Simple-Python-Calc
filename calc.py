calc.py: A simple command
import sys
filename, num1, op, num2 =sys.argv num1, num2 = int(num1), int (num2)
if op == '+': #only support addition now print(num1, num2)
elif op == '-': print (num1-num2)
elif op == "*": print(num1*num2)
else: print"0"
#end of file 
