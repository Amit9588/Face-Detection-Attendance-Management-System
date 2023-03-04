import cv2
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recogniton System")

        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="black",fg="green")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        img_top = Image.open(
            r"collegeimage\college_images\facialrecognition.png")
        img_top = img_top.resize((1430, 420), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1430, height=325)

    # =======   Button===========
        b1_1= Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=360,width=1430,height=45)

        img_bottom = Image.open(
            r"collegeimage\college_images\face_det.png")
        img_bottom = img_bottom.resize((1430, 380), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width=1430, height=325)

    def train_classifier(self):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img=Image.open(image).convert("L") # Gray scale image
            imageNp= np.array(img,'uint8')
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append((imageNp))
            ids.append((id))
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)== 13

        ids = np.array(ids)

        # +++++++++++++++++++ Train the classifier and save ++++++++++++++++++++++++
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")







if __name__=="__main__":
    root = Tk()
    obj = Train(root)


