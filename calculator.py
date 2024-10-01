import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry for showing the expression
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', 'Del', '+',
            '=', '(', ')', '%'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:  # Move to the next row after 4 buttons
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_var.set("")
        elif char == 'Del':
            self.expression = self.expression[:-1]  # Remove the last character
            self.result_var.set(self.expression)
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.result_var.set(self.expression)
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
