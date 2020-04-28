# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
from functools import partial
#import constant value from math
from math import  *
expression = ""


#will activate on pressing any button
def press(num):
   global expression
   expression = expression + str(num)

   # update the expression by using set method
   equation.set(expression)


def factorial(n):
    f = 1
    if n == 0:
        return 1
    else:
        while n != 1:
            f = f * n
            n = n - 1
        return f

def sin(x):
    x = str(x)
    x = eval(x)
    print("in sine")
    a = 0.0
    p = 0
    for i in range(1, 10, 2):
        a = a + (((-1) ** p) * ((x ** i) / factorial(i)))
        p += 1
    return a

def tan(x):
    a=sin(x)/cos(x)
    return a
def cos(x):
    print("in cosine")
    x=str(x)
    x=eval(x)
    a = 0.0
    p = 0
    for i in range(0, 11, 2):
        a = a + (((-1) ** p) * ((x ** i) / factorial(i)))
        p += 1
    return a

# Function to evaluate the final expression
def equalpress():
   try:

      global expression
      # eval function evaluate the expression
      # and str function convert the result
      # into string

      #Replace all the symbols with values to pass through eval() function
      expression=expression.replace('^','**')
      expression=expression.replace('Π','3.141592653')


      print("EXPRESSION B4 :",expression)
      total = str(eval(expression))

      equation.set(total)

      # initialze the expression variable by previously calculated value
      expression = total

   # if error is generate then handle
   # by the except block
   except:

      equation.set(" error ")
      expression = ""

# to erase last entered character of string
def backy():
    global expression
    expression=expression[:-1]
    print(expression)
    equation.set(expression)
#to calculate log
def ln(x):
    return log(x,e)
# Function to clear the contents
# of text entry box
def clear():
   global expression
   expression = ""
   equation.set("")

def reverse(string):
    string = "".join(reversed(string))
    print(string)
    return string

def fact():
    global expression
    f = 1
    n=0
    flag=0
    ns=''
    exprev=reverse(expression)
    for i in range(len(exprev)):
        if exprev[i].isdigit():
            ns=ns+exprev[i]
        else:
            n=int(reverse(ns))
            g=len(expression)-len(ns)
            expression=expression[:g]
            flag=1
            break
    if flag==0:
        n=int(expression)
        expression=""
    if n == 0:
        f=1
    else:
        while n != 1:
            f = f * n
            n = n - 1
    expression=expression+str(f)
    equation.set(expression)


# Driver code
if __name__ == "__main__":
   # create a GUI window
   gui = Tk()

   # set the background colour of GUI window
   gui.configure(background="light blue")

   # set the title of GUI window
   gui.title("Simple Calculator")

   # set the configuration of GUI window
   gui.geometry("490x360")

   equation = StringVar()

   # create the text entry box for
   # showing the expression .
   expression_field = Entry(gui, textvariable=equation,width="5")
   expression_field.grid(columnspan=10, ipadx=180)
   equation.set('Enter Your Expression')
   # create a Buttons and place at a particular
   # location inside the root window .
   buttons=['1','2','3','+','4','5','6','-','7','8','9','*','0','.','^','/','(',')','e','%']
   i = 2
   j = 0
   for btn in buttons:
       if (j == 4):
           i = i + 1
           j = 0
       print(btn)
       onClick = partial(press, btn)
       Button(gui, text=btn, command=onClick, height=2,width=16,bg='white').grid(row=i, column=j)
       j = j + 1

   clear = Button(gui, text='Clear', fg='black', bg='white',
            command=clear, height=2, width=16)
   clear.grid(row=8, column=0)
   back = Button(gui, text=' <- ', fg='black', bg='white', command=backy, height=2, width=16)
   back.grid(row=8, column=3)
   pie = Button(gui, text=' Π ', fg='black', bg='white', command=lambda: press('Π'), height=2, width=16)
   pie.grid(row=8, column=1)
   e = Button(gui, text=' ln( ', fg='black', bg='white', command=lambda: press('ln('), height=2, width=16)
   e.grid(row=8, column=2)
   fact = Button(gui, text='!', fg='black', bg='white', command=fact, height=2, width=16)
   fact.grid(row=7, column=3)
   sine = Button(gui, text='sine ', fg='black', bg='white', command=lambda :press('sin('), height=2, width=16)
   sine.grid(row=7, column=0)
   cosine = Button(gui, text=' cos ', fg='black', bg='white', command=lambda :press('cos('), height=2, width=16)
   cosine.grid(row=7, column=1)
   tangent = Button(gui, text=' tan ', fg='black', bg='white', command=lambda: press('tan('), height=2, width=16)
   tangent.grid(row=7, column=2)
   equal = Button(gui, text=' = ', fg='black', bg='white',
                  command=equalpress, height=2, width=16)
   equal.grid(row=9, column=3)
   # start the GUI until execution is stopped or user presses close on application window
   gui.mainloop()