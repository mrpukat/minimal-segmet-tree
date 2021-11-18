import tkinter as tk
import random as ra
import heapq as hq
import math

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.cordinatess_list = []
        self.number_of_dots = 10
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Genirate points"
        self.hi_there["command"] = self.genirate
        self.hi_there.pack(side="top")

        self.nummer = tk.Label(self)
        self.nummer["text"] = "Numer of points"
        self.nummer.pack( side = "top")

        self.entery = tk.Entry(self)
        self.entery.pack(side = "top")

        self.start = tk.Button(self)
        self.start["text"] = "start"
        self.start["command"] = self.mts
        self.start.pack(side="top")

        self.my_cancas = tk.Canvas(self,width=400,height=400,background="white")
        self.my_cancas.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.res = tk.Label(self)
        self.res.pack( side = "bottom")

    def get_nummer(self):
        nr = self.entery.get()
        try:
            return int(nr)
        except ValueError:
            return self.number_of_dots

    def genirate(self):
        self.number_of_dots = self.get_nummer()
        self.cordinatess_list = []
        for i in range(self.number_of_dots):
            cord = (0,0)
            while True:
                cord = (ra.randrange(110)+10,ra.randrange(110)+10)
                if not cord in self.cordinatess_list:
                    break
            self.cordinatess_list += [cord]
        self.draw_points()

    def draw_points(self): #Need to clear the canvis
        self.my_cancas.delete("all")
        for dot in self.cordinatess_list:
            self.my_cancas.create_oval(dot[0]*3,dot[1]*3,dot[0]*3,dot[1]*3,width = 10, fill = "black")

    def prosses(self, nodeIndex):
        for index in range(len(self.cordinatess_list)):
            if not self.taken[index]:
                x = self.cordinatess_list[nodeIndex][0] - self.cordinatess_list[index][0]
                y = self.cordinatess_list[nodeIndex][1] - self.cordinatess_list[index][1]
                distance = math.sqrt(x*x + y*y)
                hq.heappush(self.pq,(distance,(nodeIndex,index)))

    def mts(self):
        self.taken = []
        self.pq = []
        cost = 0

        for i in range(self.number_of_dots):
            self.taken += [False]

        self.taken[0] = True
        self.prosses(0)

        while self.pq:
            distance, index = hq.heappop(self.pq)
            if not self.taken[index[1]]:
                cost += distance
                self.taken[index[1]] = True
                orgin = self.cordinatess_list[index[0]]
                newdot = self.cordinatess_list[index[1]]
                self.my_cancas.create_line(orgin[0]*3,orgin[1]*3,newdot[0]*3,newdot[1]*3,fill = 'black')
                self.prosses(index[1])

        self.res["text"] = str(cost)

root = tk.Tk()
app = Application(master=root)

app.master.title("Minimal Segment Tree")
app.master.minsize(600,400)

app.mainloop()