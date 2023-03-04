import cv2
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Face Recogniton System")

        title_lbl = Label(self.root, text="FACE RECOGNITON", font=("times new roman", 35, "bold"), bg="navy",
                          fg="yellow")
        title_lbl.place(x=0, y=0, width=1430, height=45)

        img_top = Image.open(
            r"collegeimage\college_images\face_detector1.jpg")
        img_top = img_top.resize((715, 630), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=715, height=630)

        img_bottom = Image.open(
            r"collegeimage\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((715, 630), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=715, y=45, width=715, height=630)

        # =======   Button===========
        b1_1 = Button(f_lbl, text="FACE RECOGNITON", cursor="hand2",command=self.face_recog,
                      font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=255, y=550, width=200, height=40)
        ####################### Attendance ++++++++++++++++++++
    def mark_attendance(self,i,r,n,d):
        with open("Amit.csv","r+",newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):

                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%m:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")



    def face_recog(self):
        def draw_bound(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Amit@9588",
                                               database="face_recognizerr")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)



                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("Select Student_id from student where Student_id=" +str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence>77:
                    cv2.putText(img, f"Id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]

            return coord
        def recognise(img,clf,faceCascade):
            coord = draw_bound(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img =video_cap.read()
            img = recognise(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition(root)

    root.mainloop()