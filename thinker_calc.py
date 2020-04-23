# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
expression = ""
cosf=0
sinf=0

#will activate on pressing any button
def press(num):
   global expression,sinf,cosf
   if num=='sin(':
       sinf=1
   elif num=='cos(':
       cosf=1
   else:
       print("not sine or cosine present")
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

def sinefunction(x):
    a = 0.0
    p = 0
    for i in range(1, 10, 2):
        a = a + (((-1) ** p) * ((x ** i) / factorial(i)))
        p += 1
    return a


def cosine(x):
    a = 0.0
    p = 0
    for i in range(0, 11, 2):
        a = a + (((-1) ** p) * ((x ** i) / factorial(i)))
        p += 1
    return a

# Function to evaluate the final expression
def equalpress():
   try:

      global expression,sinf,cosf
      # eval function evaluate the expression
      # and str function convert the result
      # into string

      #Replace all the symbols with values to pass through eval() function
      expression=expression.replace('^','**')
      expression=expression.replace('Π','3.141592653')
      expression=expression.replace('e','2.7182')
      num = ''

      #check if sin or cosine in present in equation
      if sinf==1 or cosf==1:
          i=len(expression)-1
          while expression[i]!='(':
              num=expression[i]+num
              i-=1
          expression=expression[:(i-3)]
          s = int(num)
          if cosf==1:
              add=cosine(s)            # calling cosine to calculate value
              expression = expression + str(add)
          else:
              add=sinefunction(s)      # calling sine to calculate value
              expression = expression + str(add)
          sinf=cosf=0

      print("EXPRESSION B4 =:",expression)
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
   gui.configure(background="black")

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
   button1 = Button(gui, text=' 1 ', fg='black', bg='white',
               command=lambda: press(1), height=2, width=16)
   button1.grid(row=2, column=0)

   button2 = Button(gui, text=' 2 ', fg='black', bg='white',
               command=lambda: press(2), height=2, width=16)
   button2.grid(row=2, column=1)

   button3 = Button(gui, text=' 3 ', fg='black', bg='white',
               command=lambda: press(3), height=2, width=16)
   button3.grid(row=2, column=2)

   button4 = Button(gui, text=' 4 ', fg='black', bg='white',
               command=lambda: press(4), height=2, width=16)
   button4.grid(row=3, column=0)

   button5 = Button(gui, text=' 5 ', fg='black', bg='white',
               command=lambda: press(5), height=2, width=16)
   button5.grid(row=3, column=1)

   button6 = Button(gui, text=' 6 ', fg='black', bg='white',
               command=lambda: press(6), height=2, width=16)
   button6.grid(row=3, column=2)

   button7 = Button(gui, text=' 7 ', fg='black', bg='white',
               command=lambda: press(7), height=2, width=16)
   button7.grid(row=4, column=0)

   button8 = Button(gui, text=' 8 ', fg='black', bg='white',
               command=lambda: press(8), height=2, width=16)
   button8.grid(row=4, column=1)

   button9 = Button(gui, text=' 9 ', fg='black', bg='white',
               command=lambda: press(9), height=2, width=16)
   button9.grid(row=4, column=2)

   button0 = Button(gui, text=' 0 ', fg='black', bg='white',
               command=lambda: press(0), height=2, width=16)
   button0.grid(row=5, column=0)

   plus = Button(gui, text=' + ', fg='black', bg='white',
            command=lambda: press("+"), height=2, width=16)
   plus.grid(row=2, column=3)

   minus = Button(gui, text=' - ', fg='black', bg='white',
            command=lambda: press("-"), height=2, width=16)
   minus.grid(row=3, column=3)

   multiply = Button(gui, text=' * ', fg='black', bg='white',
               command=lambda: press("*"), height=2, width=16)
   multiply.grid(row=4, column=3)

   divide = Button(gui, text=' / ', fg='black', bg='white',
               command=lambda: press("/"), height=2, width=16)
   divide.grid(row=5, column=3)

   equal = Button(gui, text=' = ', fg='black', bg='white',
            command=equalpress, height=2, width=16)
   equal.grid(row=7, column=3)

   clear = Button(gui, text='Clear', fg='black', bg='white',
            command=clear, height=2, width=16)
   clear.grid(row=7, column=0)

   Decimal= Button(gui, text='.', fg='black', bg='white',command=lambda: press('.'), height=2, width=16)
   Decimal.grid(row=6, column=1)

   back = Button(gui, text=' <- ', fg='black', bg='white', command=backy, height=2, width=16)
   back.grid(row=6, column=0)

   expo = Button(gui, text=' ^ ', fg='black', bg='white', command=lambda :press('^'), height=2, width=16)
   expo.grid(row=6, column=2)

   pie = Button(gui, text=' Π ', fg='black', bg='white', command=lambda: press('Π'), height=2, width=16)
   pie.grid(row=7, column=1)

   e = Button(gui, text=' e ', fg='black', bg='white', command=lambda: press('e'), height=2, width=16)
   e.grid(row=7, column=2)

   fact = Button(gui, text='!', fg='black', bg='white', command=fact, height=2, width=16)
   fact.grid(row=6, column=3)

   sine = Button(gui, text='sine ', fg='black', bg='white', command=lambda :press('sin('), height=2, width=16)
   sine.grid(row=5, column=1)

   cos = Button(gui, text=' cos ', fg='black', bg='white', command=lambda :press('cos('), height=2, width=16)
   cos.grid(row=5, column=2)

   # start the GUI until execution is stopped or user presses close on application window
   gui.mainloop()
