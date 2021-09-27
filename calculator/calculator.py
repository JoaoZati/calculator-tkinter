import tkinter as tk

LARGE_FONT_STYLE = ('Arial', 40, 'bold')
SMALL_FONT_STYLE = ("Arial", 16)

LIGHT_GRAY = '#F5F5F5'
LABEL_COLOR = '#25265E'

BUTTON_BG = '#CAF0F8'
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')

DEFAULT_FONT_STYLE = ("Arial", 20)
SYMBOLS_BG = '#F8FAFF'

EQUAL_BG = '#CCEDFF'


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2),
        }
        self.create_digit_buttons()

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_operator_buttons()

        self.create_clear_button()
        self.create_equals_button()

        self.create_square_button()
        self.create_sqrt_button()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               bg=BUTTON_BG, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)  # NSEW fill the entire cell

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                               bg=SYMBOLS_BG, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C",
                           bg=SYMBOLS_BG, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, columnspan=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=",
                           bg=EQUAL_BG, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2",
                           bg=EQUAL_BG, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.square_button)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax",
                           bg=EQUAL_BG, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.sqrl_button)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def update_total_lebel(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_lebel()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_lebel()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_lebel()

        self.current_expression = str(eval(self.total_expression))

        self.total_expression = ""
        self.update_label()

    def square_button(self):
        self.current_expression = eval(f"{self.current_expression}**2")
        self.update_label()

    def sqrl_button(self):
        self.current_expression = eval(f"{self.current_expression}**0.5")
        self.update_label()

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
