from tkinter import *


def circle(can, x, y, r):
    can.create_oval(x - r, y - r, x + r, y + r)


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.w1 = None
        self.w2 = None
        self.w3 = None
        self.w4 = None
        self.can = Canvas(self, width=475, height=130, bg="white")
        self.can.pack(side=TOP, padx=5, pady=5)
        Button(self, text="Train", command=self.drawing).pack(side=LEFT)
        Button(self, text="Hello", command=self.kukucs).pack(side=LEFT)

    def drawing(self):
        self.w1 = Wagon(self.can, 10, 30)
        self.w2 = Wagon(self.can, 130, 30)
        self.w3 = Wagon(self.can, 250, 30)
        self.w4 = Wagon(self.can, 370, 30)

    def kukucs(self):
        if self.w1 is not None:
            self.w1.perso(3)
            self.w2.perso(2)
            self.w3.perso(1)
            self.w4.perso(2)
            self.w4.perso(3)


class Wagon:
    def __init__(self, canvas, x, y):
        """egy kis vagon rajza a <canvas_> vásznon <x,y> -ban"""

        # paraméterek tárolása példány-változókban :
        self.canvas, self.x, self.y = canvas, x, y

        # alap téglalap : 95x60 pixel :
        canvas.create_rectangle(x, y, x + 95, y + 60)

        # 3 ablak 25x40 pixel, 5 pixel távolságra :
        for xf in range(x + 5, x + 90, 30):
            canvas.create_rectangle(xf, y + 5, xf + 25, y + 40)

        # két 12 pixel sugarú kerék :
        circle(canvas, x + 18, y + 73, 12)
        circle(canvas, x + 77, y + 73, 12)

    def perso(self, wind):
        """egy emberke megjelenése a <wind> ablakban"""

        # minden egyes ablak közepe koordinátájának a kiszámítása :
        xf = self.x + wind * 30 - 12
        yf = self.y + 25

        circle(self.canvas, xf, yf, 10)  # arc
        circle(self.canvas, xf - 5, yf - 3, 2)  # balszem
        circle(self.canvas, xf + 5, yf - 3, 2)  # jobbszem
        circle(self.canvas, xf, yf + 5, 3)  # száj


app = Application()
app.mainloop()
