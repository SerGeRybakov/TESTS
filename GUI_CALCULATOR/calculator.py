from tkinter import *
from decimal import Decimal, ROUND_HALF_DOWN


class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.build()

    def dec(self, result):
        return Decimal(str(result)).quantize(Decimal("1.00"), ROUND_HALF_DOWN)

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula,
                         font=("Times New Roman", 30, "bold"),
                         bg="#000",
                         foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "+/-", "*", "x^2",
            "1", "2", "3", "/", "2√x",
            "4", "5", "6", "+", '(',
            "7", "8", "9", "-",')',
            "0", "00", ".", "=","",
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 20),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 500:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "+/-":
            if self.formula.startswith("-"):
                self.formula = self.formula[1:]
            else:
                self.formula = "-"+self.formula
        elif operation == "x^2":
            self.formula = str(self.dec((eval(self.formula))**2))
        elif operation == "2√x":
            self.formula = str(self.dec((eval(self.formula)) ** 0.5))
        elif operation == "=":
            self.formula = str(self.dec(eval(self.formula)))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("585x630+0+0")
    root.title("Калькулятор")
    root.resizable(TRUE, TRUE)
    app = Main(root)
    app.pack()
    root.mainloop()
