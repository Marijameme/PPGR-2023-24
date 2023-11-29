import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  
import cv2
import numpy as np
from osmo_teme import osmoteme

class Prozor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x700")
        self.root.title("Osmo teme")
        
        #ucitavanje
        dugme_ucitaj = tk.Button(root, text="Ucitaj sliku", font="Arial, 18" , command=self.ucitajSliku)
        dugme_ucitaj.pack(pady=10)
    
        #prikaz slike
        self.canvas = tk.Canvas(root, width=1000, height=800)
        self.canvas.pack()
        
        self.image = None
        self.points = []
        
        #dogadjaj
        self.canvas.bind("<Button-1>", self.klikNaSliku)
        
    def ucitajSliku(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.image = cv2.imread(file_path)
            self.prikaziSliku()
            
    def prikaziSliku(self):
        if self.image is not None:
            img_height, img_width, _ = self.image.shape
            max_height = 800
            max_width = 1000
            
        
            if img_height > max_height or img_width > max_width:
                scale_factor = min(max_height / img_height, max_width / img_width)
                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)
                self.image = cv2.resize(self.image, (new_width, new_height))
            
            self.photo = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.photo = Image.fromarray(self.photo)
            self.photo = ImageTk.PhotoImage(self.photo)
            
            self.canvas.config(width=self.image.shape[1], height=self.image.shape[0])
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            
    def klikNaSliku(self, event):
        if self.image is not None:
            x, y = event.x, event.y
            self.points.append((x, y))
            
            #crta tacku
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue', outline="black", width=5)
            
            #ispisuje koordinate
            coordinates = f"({x}, {y})"
            self.canvas.create_text(x+10, y-10, text=coordinates, fill='black', font=("Helvetica 10 bold"), anchor=tk.W)
            
            print(f"Clicked at: ({x}, {y})")

if __name__ == "__main__":
    root = tk.Tk()
    app = Prozor(root)
    root.mainloop()