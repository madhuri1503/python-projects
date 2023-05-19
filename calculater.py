import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # create a string variable to hold the calculator input
        self.input_str = tk.StringVar()
        self.input_str.set("")

        # create a label to display the input
        self.input_label = tk.Label(self.master, textvariable=self.input_str, font=("Arial", 20), width=20, anchor="w", bg="white", bd=5)
        self.input_label.grid(row=0, column=0, columnspan=4)

        # create the calculator buttons
        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "="
        ]

        # set up the button grid
        for i, button in enumerate(self.buttons):
            row = i // 4 + 1
            col = i % 4
            button = tk.Button(self.master, text=button, width=5, height=2, font=("Arial", 20), command=lambda button=button:self.handle_button(button))
            button.grid(row=row, column=col)

    # define a function to handle button clicks
    def handle_button(self, button):
        # get the current input string
        current_input = self.input_str.get()

        if button == "C":
            # clear the input
            self.input_str.set("")
        elif button == "=":
            # evaluate the expression and display the result
            try:
                result = eval(current_input)
                self.input_str.set(str(result))
            except:
                self.input_str.set("ERROR")
        else:
            # append the button text to the input
            self.input_str.set(current_input + button)

# create the GUI window and run the mainloop
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
