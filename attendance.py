# ====================================================================================================================================================================

from multiprocessing import parent_process
import tkinter
from tkinter import* 
from tkinter import ttk  # ttk has style tool for style
from tkinter.tix import IMAGETEXT
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # For MYSQL Connect to Our Project
import cv2  # Face Recognition Lib
import os 
import csv
from tkinter import filedialog

# ====================================================================================================================================================================


# MyData
mydata=[]
# Create A Class
class Attendance:
    # Then We need Call Construction should define by Def
    def __init__(self, root): # root is root window
        self.root = root
        # Set Window Geometry of Window
        self.root.geometry("1530x790+0+0") # (width x height + X-axis + y-axis)
        self.root.title("Face Recognition System") # Window Tab name 

# ====================================================================================================================================================================

# ==================Varible Start====================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

# ==================Varible END======================================

# ====================================================================================================================================================================

# ============================================ Window Left Side Image Background Start ====================================================  
        img = Image.open(r"Images_for_Window\attendance_bg1.jfif")

        # Size Set of Image
        img = img.resize((800, 200), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg = ImageTk.PhotoImage(img)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg) # self root mean line 14 
        f_lbl.place(x=0,y=0, width=800, height=200)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis

# ============================================ Window Left Side Image Background End =======================================================  


# ====================================================================================================================================================================

# ============================================ Window Right Side Image Background Start =====================================================  

        # Insert Two Image From Folder
        img2 = Image.open(r"Images_for_Window\attendance_bg.jpg")

        # Size Set of Image
        img2 = img2.resize((800, 200), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2) # self root mean line 14 
        f_lbl.place(x=800,y=0, width=800, height=200)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis

# ============================================ Window Right Side Image Background End ======================================================== 

# ====================================================================================================================================================================

# ============================================ Windows Center Image Background Start ========================================================== 

        img4 = Image.open(r"Images_for_Window\Bg_image.jfif")

        # Size Set of Image
        img4 = img4.resize((1530,790), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Ab humko image ko set krna window pe lable ke help se, We create Label
        bg_img = Label(self.root,image=self.photoimg4) # self root mean line 14 
        bg_img.place(x=0,y=200, width=1530, height=790)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis
        
# ============================================ Window Center Image Background Start ============================================================

# ====================================================================================================================================================================

# =================================================== TITLE LABEL START ===================================================================

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=0, width=1530, height=45) # Place ke Important isliye hota hai ki hum kahi par hi place kar sakte hai

# =================================================== TITLE LABEL END ===========================================================================

# ====================================================================================================================================================================

# ==================================== Create A Frame In the Attendance Management System Start =================================================

        main_frame = Frame(bg_img, bd=2, bg="white") # bd is Border
        main_frame.place(x=10, y=50, width=1500, height=600)
        
# ==================================== Create A Frame In the Attendance Management System End ===================================================

# ====================================================================================================================================================================

# =========================================================== Left Side Label Frame Start =======================================================
        
        left_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)
        
        img_left = Image.open(r"Images_for_Window\attendance.jpg")
        # Size Set of Image
        img_left = img_left.resize((745, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(left_frame,image=self.photoimg_left) # self root mean line 14 
        f_lbl.place(x=5,y=0, width=745, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
        
        left_inside_frame = Frame(left_frame, bd=2,relief=RIDGE, bg="white") # bd is Border
        left_inside_frame.place(x=0, y=180 , width=740, height=400 )
        
# =========================================================== Left Side Label Frame End =========================================================
# ====================================================================================================================================================================

# ======================================= LABLE AND ENTRY START ================================================================================

# ======================================= ATTENDANCE ID START ==================================================================================

        # 
        attendance_id_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13,"bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)
        
        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20,font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1,padx=10,pady=5, sticky=W)
        
# ========================================= ATTENDANCE ID END ==================================================================================
# ====================================================================================================================================================================

# ======================================= NAME START ==================================================================================

        rollLabel = Label(left_inside_frame, text="Roll:", font="comicsansns 11 bold", bg="white")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)
        
        atten_roll = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)
# ======================================= NAME END ===================================================================================
# ====================================================================================================================================================================

# ======================================= DATE START ==================================================================================

        nameLabel=Label(left_inside_frame,text="Name", bg="white",  font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_date, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1,pady=8)
        
# ======================================= DATE END ==================================================================================
# ====================================================================================================================================================================

# ======================================= DEPARTMENT START ==================================================================================
        
        depLabel=Label(left_inside_frame, text="Department", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)
        
        atten_dep = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep, width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)
        
# ======================================= DEPARTMENT END ====================================================================================
# ====================================================================================================================================================================

# ======================================= TIME START ========================================================================================
        
        timeLabel=Label(left_inside_frame, text="Time", bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)
        
        atten_time = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1,pady=8)
        
# ======================================= TIME END ==========================================================================================
# ====================================================================================================================================================================

# ======================================= DATE START ========================================================================================
        
        dateLabel=Label(left_inside_frame, text="Date", bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)
        
        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=10)
# ======================================= DATE END =========================================================================================
# ====================================================================================================================================================================

# ======================================= ATTENDANCE START ========================================================================================
        
        attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance, font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
# ======================================= ATTENDANCE END =========================================================================================
# ====================================================================================================================================================================

# ======================================= BUTTON FRAME START ========================================================================================
        
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x =5, y=270, width=720, height=34)
        
        # Create btn for save the Data into Database
        
        save_btn = Button(btn_frame, width="17", text="Import csv", command=self.importCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0,)
        
        update_btn = Button(btn_frame, width="17", text="Export csv",command=self.exportCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn = Button(btn_frame, width="17", text="Update", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, width="17", command=self.reset_date, text="Reset", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
# ======================================= BUTTON FRAME END =========================================================================================
# ====================================================================================================================================================================
        
# ======================================= RIGHT LABEL FRAME START ========================================================================================

        Right_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=790, y=10, width=660, height=580)
        
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=640, height=445)
        
# ======================================= RIGHT LABEL FRAME END =========================================================================================
# ====================================================================================================================================================================

# =================================== Scroll Bar Table Start ==============================================
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll", "name", "department", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
# =================================== Scroll Bar Table End ================================================

# =====================================================================================================================================================================

# ==================================== FATCH DATA FUNCTION START ============================================
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i) 
            
# ==================================== FATCH DATA FUNCTION END ==============================================
            
# =====================================================================================================================================================================
            
#=================================== Import CSV FUNCTION START ============================================== 
    def importCsv(self):
        mydata.clear()
        # global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.")),parent=self.root)# getcwd full get current Working Directory
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

#=================================== Import CSV FUNCTION END =============================================== 
# =====================================================================================================================================================================

#=================================================== Export CSV FUNCTION START ============================================================= 

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.")),parent=self.root)# getcwd full get current Working Directory
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","You data Exported to"+os.path.basename(fln)+"successfully",paraent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
#=================================================== Export CSV FUNCTION END =============================================================== 
# =====================================================================================================================================================================
    
#=================================================== GET CURSOR FUNCTION START =============================================================== 
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
#=================================================== GET CURSOR FUNCTION END =============================================================== 
# ====================================================================================================================================================================
    
#=================================================== RESET FUNCTION START =============================================================== 
    
    def reset_date(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
#=================================================== RESET FUNCTION END ================================================================= 
#====================================================================================================================================================================

        
        
if __name__ == "__main__":
    root=Tk()
    obj =Attendance(root)
    root.mainloop()