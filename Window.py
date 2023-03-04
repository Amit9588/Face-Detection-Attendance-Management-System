import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Helpdesk
import os
import cv2
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recogniton System")
#first Image
        img=Image.open(r"collegeimage\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#Second
        img1 = Image.open(r"collegeimage\college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
#Third Image
        img2 = Image.open(r"collegeimage\college_images\images.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        #Bg ImGGE
        img3 = Image.open(r"collegeimage\college_images\bg1.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bG_image= Label(self.root, image=self.photoimg3)
        bG_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bG_image,text="FACE RECOGNITION ATTENDANCE SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-100,y=0,width=1530,height=45)

        # --------------- Time----------------------
        def time():
            string = strftime("%H:%M:%S:%p")
            lb1.config(text=string)
            lb1.after(1000,time)
        lb1=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lb1.place(x=100,y=0,width=110,height=50)
        time()
#student Button
        img4 = Image.open(r"collegeimage\college_images\student_at_PC_1600px.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bG_image,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=100,y=60,width=220,height=220)

        b1_1 = Button(bG_image, text="Student Details",command=self.student_details, cursor='hand2',font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=100, y=260, width=220, height=40)

        # detection Button
        img5 = Image.open(r"collegeimage\college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bG_image, image=self.photoimg5, cursor='hand2',command=self.face_data)
        b1.place(x=400, y=60, width=220, height=220)

        b1_1 = Button(bG_image, text="Face Detector", cursor='hand2',command=self.face_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=400, y=260, width=220, height=40)

        # Attendence Button
        img6 = Image.open(r"collegeimage\college_images\smart-attendance.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bG_image, image=self.photoimg6, cursor='hand2',command=self.attendance_data)
        b1.place(x=700, y=60, width=220, height=220)

        b1_1 = Button(bG_image, text="Attendence", cursor='hand2',command=self.attendance_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=700, y=260, width=220, height=40)

        # HelpDesk Button
        img7 = Image.open(r"collegeimage\college_images\Help desk.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bG_image, image=self.photoimg7, cursor='hand2',command=self.help_data)
        b1.place(x=1000, y=60, width=220, height=220)

        b1_1 = Button(bG_image, text="Help Desk", cursor='hand2',command=self.help_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=1000, y=260, width=220, height=40)

        # Train Button
        img8 = Image.open(r"collegeimage\college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bG_image, image=self.photoimg8, cursor='hand2',command=self.train_data)
        b1.place(x=100, y=315, width=220, height=220)

        b1_1 = Button(bG_image, text="Train Data", cursor='hand2',command=self.train_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=100, y=515, width=220, height=40)

        # Photos Button
        img9 = Image.open(r"collegeimage\college_images\photos.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bG_image, image=self.photoimg9, cursor='hand2',command=self.open_img)
        b1.place(x=400, y=315, width=220, height=220)

        b1_1 = Button(bG_image, text="Photos", cursor='hand2',command=self.open_img, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=400, y=515, width=220, height=40)

        # Developer Button
        img10 = Image.open(r"collegeimage\college_images\developer.jpg")
        img10 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bG_image, image=self.photoimg10, cursor='hand2',command=self.Developer_data)
        b1.place(x=700, y=315, width=220, height=220)

        b1_1 = Button(bG_image, text="Developer", cursor='hand2',command=self.Developer_data, font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=700, y=515, width=220, height=40)

        # EXIT Button
        img11 = Image.open(r"collegeimage\college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bG_image, image=self.photoimg11, cursor='hand2')
        b1.place(x=1000, y=315, width=220, height=220)

        b1_1 = Button(bG_image, text="Exit", cursor='hand2', font=("times new roman", 15, "bold"),
                      bg="dark blue", fg="white")
        b1_1.place(x=1000, y=515, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recogniton","Are you sure to exit the project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


################################# Function Button ##############

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Developer_data(self):

        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):

        self.new_window = Toplevel(self.root)
        self.app =Helpdesk(self.new_window)

if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)

    root.mainloop()