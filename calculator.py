import tkinter as tk
import math

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        if "/0" in calculation:
            raise ValueError("Cannot divide by zero")
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title('Calculator')
root.geometry("325x400")
root.configure(bg='lightgrey')

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#Number pad button placement and initialization
btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn7.grid(row=3,column=0)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn8.grid(row=3,column=1)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn9.grid(row=3,column=2)
btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn4.grid(row=4,column=0)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn5.grid(row=4,column=1)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn6.grid(row=4,column=2)
btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn1.grid(row=5,column=0)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn2.grid(row=5,column=1)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn3.grid(row=5,column=2)
btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, height=2, font=("Arial", 14), bg='black', fg='white')
btn0.grid(row=6,column=1)

#Operator and other miscellaneous buttons placement and initialization
btnDiv = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, height=2, font=("Arial", 14))
btnDiv.grid(row=2,column=3)
btnMul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, height=2, font=("Arial", 14))
btnMul.grid(row=3,column=3)
btnSub = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, height=2, font=("Arial", 14))
btnSub.grid(row=4,column=3)
btnAdd = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, height=2, font=("Arial", 14))
btnAdd.grid(row=5,column=3)
btnLef = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, height=2, font=("Arial", 14))
btnLef.grid(row=2,column=1)
btnRig = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, height=2, font=("Arial", 14))
btnRig.grid(row=2,column=2)
btnClr = tk.Button(root, text="C", command=clear_field, width=5, height=2, font=("Arial", 14), bg='red', fg='white')
btnClr.grid(row=2,column=0)
btnEqu = tk.Button(root, text="=", command=evaluate_calculation, width=5, height=2, font=("Arial", 14), bg='blue', fg='white')
btnEqu.grid(row=6,column=3)
btnDec = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, height=2, font=("Arial", 14))
btnDec.grid(row=6,column=2)
btnSqr = tk.Button(root, text="x²", command=lambda: add_to_calculation("**2"), width=5, height=2, font=("Arial", 14))
btnSqr.grid(row=4,column=4)

# Square root button
btnSqrt = tk.Button(root, text="√", command=lambda: add_to_calculation("math.sqrt("), width=5, height=2, font=("Arial", 14))
btnSqrt.grid(row=3, column=4)

# Percentage button
btnPerc = tk.Button(root, text="%", command=lambda: add_to_calculation("/100"), width=5, height=2, font=("Arial", 14))
btnPerc.grid(row=2, column=4)

root.mainloop()