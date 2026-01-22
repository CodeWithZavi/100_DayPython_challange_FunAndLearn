import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Display
        self.display = tk.Entry(root, font=('Arial', 24), justify='right', bd=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 1
        col = 0
        
        for button in buttons:
            cmd = lambda x=button: self.on_button_click(x)
            btn = tk.Button(root, text=button, font=('Arial', 18), 
                          command=cmd, height=2, width=5)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights for responsive layout
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            # Clear the display
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            # Evaluate the expression
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            # Add character to expression
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
