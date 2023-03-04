import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Helpdesk:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root , text="Help Desk ", font=("times new roman", 35, "bold"),
                          bg="grey", fg="yellow")
        title_lbl.place(x=-0, y=0, width=1400, height=45)

        # first
        img = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg"
                         r"")
        img = img.resize((1430, 710), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=1430, height=670)

        dept_label = Label(f_lbl, text="Email : phenomenalregins3@gmail.com", font=("times new roman", 20, "bold"), bg="black",
                           fg="green")
        dept_label.grid(row=0, column=1, padx=0)



if __name__=="__main__":
    root = Tk()
    obj = Helpdesk(root)

    root.mainloop()