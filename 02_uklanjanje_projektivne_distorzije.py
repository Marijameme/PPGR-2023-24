import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  
import cv2
import numpy as np
import modifikovaniDLT as mdf
import math

class Window:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Uklanjanje projektivne distorzije')
        self.load_button = tk.Button(root, text='Ucitaj sliku', command=self.load_picture)
        self.load_button.pack(padx=10 ,pady=10)
        self.canvas = tk.Canvas(root, width=1000, height=800)
        self.width = 1000
        self.height = 800
        self.canvas.pack()
        self.image = None
        self.points = []

        self.canvas.bind("<Button-1>", self.clik)

    def load_picture(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.image = cv2.imread(file_path)
            self.show_picture()
    def show_picture(self):
        print("slika se prikazuje")
        if self.image is not None:
            img_height, img_width, _ = self.image.shape
            if img_height > self.height or img_width > self.width:
                self._scale()
            self.photo = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.photo = Image.fromarray(self.photo)
            self.photo = ImageTk.PhotoImage(self.photo)
            
            self.canvas.config(width=self.image.shape[1], height=self.image.shape[0])
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
    def clik(self, event):
        if self.image is not None:
            x, y = event.x, event.y
            self.points.append([x, y, 1])
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='blue', outline="black", width=5)
                        
            print(f"Clicked at: ({x}, {y})") 
        if 4 == len(self.points):
            self._remove_distortion()
    
    def _scale(self):
        img_height, img_width, _ = self.image.shape
        alpha = min(self.height / img_height, self.width / img_width)
        new_width = int(img_width * alpha)
        new_height = int(img_height * alpha)
        self.image = cv2.resize(self.image, (new_width, new_height))

    def _calculate_coordinates(self):
        return [self.points[0],
                self.points[1], 
                [self.points[1][0]+200, self.points[1][1], self.points[1][2]],
                [self.points[0][0]+200, self.points[0][1], self.points[0][2]]]
    def _remove_distortion(self):
        print("uklanjamo distorziju")
        img = self._calculate_coordinates()
    
        # for x,y,z in img:
        #     print(x, y, z)
        #     self.canvas.create_oval(x, y, x, y, fill='blue', outline="blue", width=5)

        matrix = mdf.DLTwithNormalization(self.points, img)

        result = cv2.warpPerspective(self.image, matrix, (4080, 3060), flags=cv2.INTER_LINEAR)
        print('result shape: ', result.shape)

        self.photo = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        self.photo = Image.fromarray(self.photo)
        self.photo = ImageTk.PhotoImage(self.photo)
            
        self.canvas.config(width=self.image.shape[1], height=self.image.shape[0])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.points.clear()
        # print('Kraj')

if __name__ == "__main__":
    root = tk.Tk()
    # root.iconbitmap('C:/Users/Marijana/Desktop/Alati/ikonice/chrom')
    app = Window(root)
    root.mainloop()

