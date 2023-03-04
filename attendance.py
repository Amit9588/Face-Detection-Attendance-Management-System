import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import csv
import os

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+0")
        self.root.title("Attendance Management System")

        self.var_atten_id=StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # first
        img = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\smart-attendance.jpg")
        img = img.resize((715, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=715, height=200)
        # Second
        img1 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\attendence.jpg")
        img1 = img1.resize((715, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=715, y=0, width=715, height=130)



        # Bg ImGGE
        img3 = Image.open(r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\BestFacialRecognition.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bG_image = Label(self.root, image=self.photoimg3)
        bG_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bG_image, text="ATTENDANCE MANAGEMENT SYSTEM ", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=-100, y=0, width=1530, height=45)

        main_frame = Frame(bG_image, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1350, height=550)

        # left label frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=0, width=660, height=520)

        img_left = Image.open(
            r"C:\Users\Genuine Junction\Downloads\collegeimage\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 110), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=4, y=0, width=650, height=110)

        left_inside_frame = Frame(bG_image, bd=2, bg="white",relief=RIDGE)
        left_inside_frame.place(x=20, y=185, width=650, height=340)

        # Labels and frames
        # id
        atten_id_label = Label(left_inside_frame, text="Attendance Id:", font=("times new roman", 12, "bold"),
                              bg="white")
        atten_id_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        atten_id_entry = ttk.Entry(left_inside_frame, width=19,textvariable=self.var_atten_id,
                                  font=("times new roman", 13, "bold"))
        atten_id_entry.grid(row=0, column=1, padx=8, pady=5, sticky=W)

        # Roll no

        atten_roll_no_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                              bg="white")
        atten_roll_no_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        atten_roll_no_entry = ttk.Entry(left_inside_frame, width=19,textvariable=self.var_atten_roll,
                                  font=("times new roman", 13, "bold"))
        atten_roll_no_entry.grid(row=0, column=3, padx=8, pady=5, sticky=W)

        # Name

        atten_name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"),
                              bg="white")
        atten_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        atten_name_entry = ttk.Entry(left_inside_frame, width=19,textvariable=self.var_atten_name,
                                  font=("times new roman", 13, "bold"))
        atten_name_entry.grid(row=1, column=1, padx=8, pady=5, sticky=W)

        # Department

        atten_dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"),
                              bg="white")
        atten_dep_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        atten_dep_entry = ttk.Entry(left_inside_frame, width=19,textvariable=self.var_atten_dep,
                                  font=("times new roman", 13, "bold"))
        atten_dep_entry.grid(row=1, column=3, padx=8, pady=5, sticky=W)

        # Time

        atten_time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"),
                              bg="white")
        atten_time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        atten_time_entry = ttk.Entry(left_inside_frame, width=19,textvariable=self.var_atten_time,
                                  font=("times new roman", 13, "bold"))
        atten_time_entry.grid(row=2, column=1, padx=8, pady=5, sticky=W)

        # Date

        atten_date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"),
                              bg="white")
        atten_date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        atten_date_entry = ttk.Entry(left_inside_frame, width=19,textvariable=self.var_atten_date,
                                  font=("times new roman", 13, "bold"))
        atten_date_entry.grid(row=2, column=3, padx=8, pady=5, sticky=W)

        # Attendance Status

        attend_status_label = Label(left_inside_frame, text="Attendance Status",font=("times new roman", 12, "bold"),
                              bg="white")
        attend_status_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.attend_status_entry = ttk.Combobox(left_inside_frame, width=17,textvariable=self.var_atten_attendance,
                                  font=("times new roman", 13, "bold"))
        self.attend_status_entry["values"]=("Status","Present","Absent")

        self.attend_status_entry.grid(row=3, column=1, padx=8, pady=3, sticky=W)


        # Button frames
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=450, width=655, height=30)

        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv, width=16, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0, )

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv
                            , width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=16,
                            font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",  width=14,command=self.reset_data,
                           font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=675, y=0, width=660, height=520)


        table_frame = Frame(right_frame, bd=2, bg="white",relief=RIDGE)
        table_frame.place(x=5, y=0, width=650, height=455)

        # ------------------- scroll bar table ---------------------
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id", width=120)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # ------------------- Fetch data ------------------

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln= filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("Csv File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetch_data(mydata)

    def exportCsv(self):

        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfile(initialdir=os.getcwd(), title="Open Csv",
                                         filetypes=(("Csv File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+" Successfully")
        except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")














if __name__=="__main__":

    root = Tk()
    obj = Attendance(root)

    root.mainloop()