## CALCULATOR APP ##

import tkinter as tc

calculation = ""

# Creating functions
def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_calculation()
        text_result.insert(1.0, "Error")    

def clear_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    

# Main window
root = tc.Tk()
root.geometry("300x275")

text_result = tc.Text(root, height=2, width= 16, font=("Arial", 24)) 
text_result.grid(columnspan=5)

# Creating Buttons
btn_1 = tc.Button(root, text="1", command=lambda: add_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tc.Button(root, text="2", command=lambda: add_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tc.Button(root, text="3", command=lambda: add_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tc.Button(root, text="4", command=lambda: add_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tc.Button(root, text="5", command=lambda: add_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tc.Button(root, text="6", command=lambda: add_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tc.Button(root, text="7", command=lambda: add_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tc.Button(root, text="8", command=lambda: add_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tc.Button(root, text="9", command=lambda: add_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tc.Button(root, text="0", command=lambda: add_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = tc.Button(root, text="+", command=lambda: add_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tc.Button(root, text="-", command=lambda: add_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multi = tc.Button(root, text="*", command=lambda: add_calculation("*"), width=5, font=("Arial", 14))
btn_multi.grid(row=4, column=4)
btn_div = tc.Button(root, text="/", command=lambda: add_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open = tc.Button(root, text="(", command=lambda: add_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tc.Button(root, text=")", command=lambda: add_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_equal = tc.Button(root, text="=", command= evaluate_calculation, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)
btn_clear = tc.Button(root, text="C", command= clear_calculation, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
