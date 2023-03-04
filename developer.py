import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root , text="DEVELOPER ", font=("times new roman", 35, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=-0, y=0, width=1400, height=45)

        # first
        img = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\dev.jpg"
                         r"")
        img = img.resize((1430, 710), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=1430, height=670)

        main_frame = Frame(f_lbl, bd=2, bg="white",relief=RIDGE)
        main_frame.place(x=855, y=0, width=500, height=400)

        img1 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\tony.jpg"
                         r"")
        img1 = img1.resize((160, 160), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=1200, y=45, width=160, height=160)

        #Developer
        dept_label = Label(main_frame, text="Hello My Name is Amit.", font=("times new roman", 20, "bold"), bg="white",fg="black")
        dept_label.grid(row=0, column=0, padx=0)

        dept_label1 = Label(main_frame, text="I am Student of Btech IT.", font=("times new roman", 20, "bold"), bg="white",
                           fg="black")
        dept_label1.grid(row=1, column=0, padx=0)

        dept_label2 = Label(main_frame, text="Student of Guru Jambeshwar", font=("times new roman", 19, "bold"),
                            bg="white",
                            fg="black")
        dept_label2.grid(row=2, column=0, padx=2)

        dept_label3 = Label(main_frame, text="University.", font=("times new roman", 19, "bold"),
                            bg="white",
                            fg="black")
        dept_label3.grid(row=3, column=0, padx=2)



        img3 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\BestFacialRecognition.jpg"
                          r"")
        img3 = img3.resize((530, 250), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=855, y=198, width=530, height=250)








if __name__=="__main__":
    root = Tk()
    obj = Developer(root)

    root.mainloop()