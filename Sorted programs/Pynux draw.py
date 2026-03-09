import tkinter as tk
from tkinter import colorchooser

class PynuxDraw:
    def __init__(self, root):
        self.root = root
        self.root.title("Pynux Draw")
        self.root.geometry("900x650")
        self.root.configure(bg="#1e1e1e")

        self.brush_color = "white"
        self.brush_size = 5
        self.drawing = False

        
        self.toolbar = tk.Frame(self.root, bg="#2d2d2d", height=50)
        self.toolbar.pack(fill=tk.X, side=tk.TOP)

        
        colors = ["white", "black", "red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]
        for c in colors:
            tk.Button(self.toolbar, bg=c, width=2, height=1, command=lambda col=c: self.set_brush_color(col)).pack(side=tk.LEFT, padx=3, pady=5)

        
        tk.Button(self.toolbar, text="Custom Color", bg="#444", fg="white", command=self.choose_color).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Eraser", bg="#555", fg="white", command=self.set_eraser).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Clear", bg="#880000", fg="white", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Toggle Paper", bg="#006688", fg="white", command=self.toggle_paper).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Marker", bg="#333", fg="white", command=lambda: self.set_brush_type("marker")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.toolbar, text="Highlighter", bg="#333", fg="white", command=lambda: self.set_brush_type("highlighter")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.toolbar, text="Pencil", bg="#333", fg="white", command=lambda: self.set_brush_type("pencil")).pack(side=tk.LEFT, padx=5)

        
        self.canvas_bg = "white"
        self.canvas = tk.Canvas(self.root, bg=self.canvas_bg, cursor="tcross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

       
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def set_brush_color(self, color):
        self.brush_color = color

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.brush_color, width=self.brush_size,
                                    capstyle=tk.ROUND, smooth=True)
            self.last_x, self.last_y = event.x, event.y

    def set_brush_type(self, btype):
        self.brush_type = btype

    def set_eraser(self):
        
        self.brush_color = "#111"

    def clear_canvas(self):
        self.canvas.delete("all")

    def toggle_paper(self):
        self.canvas_bg = "black" if self.canvas_bg == "white" else "white"
        self.canvas.configure(bg=self.canvas_bg)
        if self.brush_color == self.canvas_bg:
            self.brush_color = "white" if self.canvas_bg == "black" else "black"

    def stop_draw(self, event):
        self.drawing = False


if __name__ == "__main__":
    root = tk.Tk()
    app = PynuxDraw(root)
    root.mainloop()
