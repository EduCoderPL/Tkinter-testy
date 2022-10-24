class Ball:

    def __init__(self, canvas, x, y, diameter, xVel, yVel, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVel = xVel
        self.yVel = yVel

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0:
            self.xVel *= -1

        if coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0:
            self.yVel *= -1


        self.canvas.move(self.image, self.xVel, self.yVel)