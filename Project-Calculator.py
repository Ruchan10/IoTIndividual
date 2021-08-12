# Import all the required libraries
from tkinter import*

# Create a user interface
root = Tk()

# Set a title of the window
root.title("Calculator")

# Image for the window
root.iconbitmap("calc.ico")

# Set the size of the window
root.geometry("485x590")
root.maxsize(width=500, height=600)
root.minsize(width=470, height=550)

# Background color of window
root.config(bg="grey")

# Creating a screen to display all the contents
e = Entry(root, width=12, bg="grey", justify=RIGHT, font=('times', 50, 'bold'))
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)


def b_click(number):
    current = e.get()
    e.delete(0, END)
    global exp
    exp = str(current) + str(number) # String concatenation
    e.insert(0, exp)


def b_cls():
    e.delete(0, END)


def b_add():
    firstnumber = e.get()
    global fnum
    global math
    math = "addition"
    fnum = int(firstnumber)
    e.delete(0, END)


def b_pwr():
    firstnumber = e.get()
    global fnum
    global math
    math = "power"
    fnum = int(firstnumber)
    e.delete(0, END)


def b_mod():
    firstnumber = e.get()
    global fnum
    global math
    math = "modulus"
    fnum = int(firstnumber)
    e.delete(0, END)


def b_sub():
    firstnumber = e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = int(firstnumber)
    e.delete(0, END)


def b_mul():
    firstnumber = e.get()
    global fnum
    global math
    math = "multiply"
    fnum = int(firstnumber)
    e.delete(0, END)


def b_div():
    firstnumber = e.get()
    global fnum
    global math
    math = "division"
    fnum = int(firstnumber)
    e.delete(0, END)


# This calculates the given inputs
def b_eql():
    secondnumber = int(e.get())
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, fnum + secondnumber)
    elif math == 'subtraction':
        e.insert(0, fnum - secondnumber)
    elif math == 'division':
        e.insert(0, fnum / secondnumber)
    elif math == 'power':
        e.insert(0, fnum ** secondnumber)
    elif math == 'subtraction':
        e.insert(0, fnum - secondnumber)
    elif math == 'multiply':
        e.insert(0, fnum * secondnumber)
    elif math == 'modulus':
        e.insert(0, fnum % secondnumber)


# Creating frame for buttons
frame = LabelFrame(root, width=312, height=272.5, bg="grey")
frame.grid()

font0 = ("times", 15, 'bold')
font1 = ("verdana", 15,'bold')

# Creating all the required buttons
b1 = Button(frame, text="1", padx=40, pady=20, command=lambda: b_click(1), bg='black', fg='white', bd=7, font=font0)
b2 = Button(frame, text="2", padx=40, pady=20, command=lambda: b_click(2), bg='black', fg='white', bd=7, font=font0)
b3 = Button(frame, text="3", padx=40, pady=20, command=lambda: b_click(3), bg='black', fg='white', bd=7, font=font0)
b4 = Button(frame, text="4", padx=40, pady=20, command=lambda: b_click(4), bg='black', fg='white', bd=7, font=font0)
b5 = Button(frame, text="5", padx=40, pady=20, command=lambda: b_click(5), bg='black', fg='white', bd=7, font=font0)
b6 = Button(frame, text="6", padx=40, pady=20, command=lambda: b_click(6), bg='black', fg='white', bd=7, font=font0)
b7 = Button(frame, text="7", padx=40, pady=20, command=lambda: b_click(7), bg='black', fg='white', bd=7, font=font0)
b8 = Button(frame, text="8", padx=40, pady=20, command=lambda: b_click(8), bg='black', fg='white', bd=7, font=font0)
b9 = Button(frame, text="9", padx=40, pady=20, command=lambda: b_click(9), bg='black', fg='white', bd=7, font=font0)
b0 = Button(frame, text="0", padx=40, pady=20, command=lambda: b_click(0), bg='black', fg='white', bd=7, font=font0)
bcls = Button(frame, text="CLS", padx=84, pady=20, command=b_cls, bg='black', fg='orange', bd=7, font=font1)
badd = Button(frame, text="+", padx=38, pady=20, command=b_add, bg='black', fg='orange', bd=7, font=font1)
bsub = Button(frame, text="-", padx=42, pady=20, command=b_sub, bg='black', fg='orange', bd=7, font=font1)
bmul = Button(frame, text="*", padx=40, pady=20, command=b_mul, bg='black', fg='orange', bd=7, font=font1)
bdiv = Button(frame, text="/", padx=40, pady=20, command=b_div, bg='black', fg='orange', bd=7, font=font1)
bpwr = Button(frame, text="^", padx=35, pady=20, command=b_pwr, bg='black', fg='orange', bd=7, font=font1)
bmod = Button(frame, text="mod", padx=20, pady=20, command=b_mod, bg='black', fg='orange', bd=7, font=font1)
beql = Button(frame, text="=", padx=96, pady=20, command=b_eql, bg='black', fg='orange', bd=7, font=font1)

# First row
bcls.grid(row=1, column=0, columnspan=2)
bpwr.grid(row=1, column=2)
bdiv.grid(row=1, column=3)

# Second row
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
bmul.grid(row=2, column=3)

# Third row
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
bsub.grid(row=3, column=3)

# Fourth row
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
badd.grid(row=4, column=3)

# Fifth row
bmod.grid(row=5, column=0)
b0.grid(row=5, column=1)
beql.grid(row=5, column=2, columnspan=2)

root.mainloop()
