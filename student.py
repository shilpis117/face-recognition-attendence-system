# ====================================================================================================================================================================

import tkinter
from tkinter import* 
from tkinter import ttk  # ttk has style tool for style
from tkinter.tix import IMAGETEXT
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # For MYSQL Connect to Our Project
import cv2  # Face Recognition Lib
# ====================================================================================================================================================================


# Create A Class
class Student_Detail:
    # Then We need Call Construction should define by Def
    def __init__(self, root): # root is root window
        self.root = root
        # Set Window Geometry of Window
        self.root.geometry("1530x790+0+0") # (width x height + X-axis + y-axis)
        self.root.title("Face Recognition System") # Window Tab name 
        
# ====================================================================================================================================================================
        
        # =========================== Variable =======================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_std_name = StringVar()
        
# ====================================================================================================================================================================
        
        # # Insert One Image From Folder 
        img = Image.open(r"Images_for_Window\student.jpg")
        
        # Size Set of Image
        img = img.resize((500, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg = ImageTk.PhotoImage(img)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg) # self root mean line 14 
        f_lbl.place(x=0,y=0, width=550, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis
        
# ====================================================================================================================================================================
        
        # Insert Two Image From Folder
        img2 = Image.open(r"Images_for_Window\student2.jpg")
        
        # Size Set of Image
        img2 = img2.resize((500, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg2) # self root mean line 14 
        f_lbl.place(x=500,y=0, width=520, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis
        
# ====================================================================================================================================================================
        
        # Insert Three Image From Folder
        img3 = Image.open(r"Images_for_Window\student3.jpg")
        
        # Size Set of Image
        img3 = img3.resize((500, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg3) # self root mean line 14 
        f_lbl.place(x=1000,y=0, width=520, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
        
# ====================================================================================================================================================================
        
        # Insert Image Background From Folder
        img4 = Image.open(r"Images_for_Window\Bg_image.jfif")
        
        # Size Set of Image
        img4 = img4.resize((1530,790), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        bg_img = Label(self.root,image=self.photoimg4) # self root mean line 14 
        bg_img.place(x=0,y=130, width=1530, height=790)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
        
# ====================================================================================================================================================================
        
        #Title of Label
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=0, width=1530, height=45) # Place ke Important isliye hota hai ki hum kahi par hi place kar sakte hai
        
# ====================================================================================================================================================================
        
        # Create A Frame In the Student Management System
        main_frame = Frame(bg_img, bd=2, bg="white") # bd is Border
        main_frame.place(x=10, y=50, width=1500, height=600)
        
# ====================================================================================================================================================================
        
        # Left Label Frame
        
        left_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)
        
# ====================================================================================================================================================================
        
        img_left = Image.open(r"Images_for_Window\attendance.jpg")
        
        # Size Set of Image
        img_left = img_left.resize((745, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(left_frame,image=self.photoimg_left) # self root mean line 14 
        f_lbl.place(x=5,y=0, width=745, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
        
        # Current Course Information
        current_course_frame=LabelFrame(left_frame,bd=2, bg="white", relief=RIDGE, text="Current Course Information",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=745, height=110)
# ====================================================================================================================================================================
        
        # Department LABEL
        dep_label = Label(current_course_frame, text='Department',font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0, column=0, padx=10)
        
        # Create multiple Combo Box
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),width=20,state="read only")
        dep_combo["values"]=("Select Department", "Computer","IT", "Mechnical", "Civil","Electrical")
        dep_combo.current(0) # Current main Position of Department Define karte hai
        dep_combo.grid(row=0, column=1,padx=2, pady=10, sticky=W) 
# ====================================================================================================================================================================
        
        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"),width=20,state="read only")
        course_combo["values"]=("Select Course", "CS","IT", "CE", "EE","EX","ME")
        course_combo.current(0) # Current main Position of Department Define karte hai
        course_combo.grid(row=0, column=3,padx=2, pady=10, sticky=W) 
# ====================================================================================================================================================================
        
        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman", 12, "bold"),width=20,state="read only")
        year_combo["values"]=("Select Year", "2020-21","2021-22", "2022-23", "2023-24")
        year_combo.current(0) # Current main Position of Department Define karte hai
        year_combo.grid(row=1, column=1,padx=2, pady=10, sticky=W) 
# ====================================================================================================================================================================
        
        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),width=20,state="read only")
        semester_combo["values"]=("Select Semester", "Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0) # Current main Position of Department Define karte hai
        semester_combo.grid(row=1, column=3,padx=2, pady=10, sticky=W) 
# ====================================================================================================================================================================
        
        # Class Student Information
        class_student_frame=LabelFrame(left_frame,bd=2, bg="white", relief=RIDGE, text="Class Student Information",font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=745, height=290)
# ====================================================================================================================================================================
        
        # Student_id
        student_id_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, sticky=W)
        
        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20,font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1,padx=10, sticky=W)
# ====================================================================================================================================================================
        
        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame,  textvariable=self.var_std_name, width=20,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3,padx=10,pady=5, sticky=W)
        
# ====================================================================================================================================================================
        
        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,font=("times new roman", 12, "bold"),width=20,state="read only")
        div_combo["values"]=("A", "B","C")
        div_combo.current(0) # Current main Position of Department Define karte hai
        div_combo.grid(row=1, column=1,padx=10, pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Roll Number
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,  width=20,font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3,padx=10,pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=20,state="read only")
        gender_combo["values"]=("Male", "Female","Other")
        gender_combo.current(0) # Current main Position of Department Define karte hai
        gender_combo.grid(row=2, column=1,padx=10, pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3,padx=10,pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Email                             
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20,font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1,padx=10,pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Phone No
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20,font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1,padx=10,pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20,font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3,padx=10,pady=5, sticky=W)
# ====================================================================================================================================================================
        
        # Radio Button
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)
# ====================================================================================================================================================================
        
        # Button Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x =5, y=200, width=720, height=34)
        
        # Create btn for save the Data into Database
        
        save_btn = Button(btn_frame, width="17",command=self.add_data, text="Save", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0,)
        
        update_btn = Button(btn_frame, width="17",command=self.update_data, text="Update", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1,)
        
        delete_btn = Button(btn_frame, width="17",command=self.delete_data, text="Delete", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2,)
        
        reset_btn = Button(btn_frame, width="17",command=self.reset_data, text="Reset", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3,)
        
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=234, width=720, height=30)
        
        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, width="35", text="Take photo Sample", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0,)
        
        Update_photo_btn = Button(btn_frame1, width="35", text="Update Photo Sample", font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Update_photo_btn.grid(row=1, column=1,)
# ====================================================================================================================================================================
        
        # Right Label Frame        
        Right_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=790, y=10, width=660, height=580)
# ====================================================================================================================================================================
        
        # Insert Image
        
        img_right = Image.open(r"Images_for_Window\student4.jpg")
        
        # Size Set of Image
        img_right = img_right.resize((745, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(Right_frame,image=self.photoimg_right) # self root mean line 14 
        f_lbl.place(x=5,y=0, width=745, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
# ====================================================================================================================================================================
        
        # ==========SEARCH SYSTEM============
        
        # Search Frame
        search_frame=LabelFrame(Right_frame,bd=2, bg="white", relief=RIDGE, text="Search System",font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=645, height=100)
# ====================================================================================================================================================================
        
        # Search Bar
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="Steelblue1",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        search_combo = ttk.Combobox(search_frame,font=("times new roman", 12, "bold"),width=15,state="read only")
        search_combo["values"]=("Select", "Roll_No","Phone_Number")
        search_combo.current(0) # Current main Position of Department Define karte hai
        search_combo.grid(row=0, column=1,padx=2, pady=10, sticky=W)
        
        search_entry = ttk.Entry(search_frame, width=12,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2,padx=10,pady=5, sticky=W)
        
        search_btn = Button(search_frame, width="11", text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=2)
# ====================================================================================================================================================================
        
        showAll_btn = Button(search_frame, width="11", text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4,padx=2)
# ====================================================================================================================================================================
        
        # ================= Table Frame ====================
        table_frame=Frame(Right_frame,bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=240, width=645, height=300)
# ====================================================================================================================================================================
        
        # ================= Scroll Bar ====================
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "phone","dob", "address","email", "teacher", "photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X) # pack main Side dena hota hai
        scroll_y.pack(side=RIGHT, fill=Y) # pack main Side dena hota hai
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100 )
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ====================================================================================================================================================================
        
        # ============== FUNCTION DECREATION FOR SAVE DATA===============
        
    def add_data(self):
        #Validation on Error When Data not Filled
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Field are Required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been Added Successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
# ====================================================================================================================================================================
    
    # ==============Fetch Data form Database Function Start ===================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        # Fetch data to a variable
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
# ====================================================================================================================================================================
        
    # ==============Fetch Data form Database Function END ===================
    
        
    # ================Get Cursor For Update data Function Start==============
    
    def get_cursor(self,event=""):
        # For Cursor Focus create a variable
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ================Get Cursor For Update data Function End==============
# ====================================================================================================================================================================
    
    # ================Update Function Start================================
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Field are Required", parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update", "Do you Want to Update this Student Details", parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update Student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Student details Successfully Update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    
    # ================Update Function End==================================
# ====================================================================================================================================================================
    
    # ================Delete Function Start================================
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id Must be Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do You Want To Delete This Student", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
                    my_cursor=conn.cursor()
                    # Query Create for Delete By Sql
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted Student Details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    
    # ================Delete Function End==================================
# ====================================================================================================================================================================
    
    # ================Reset Function Start================================
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    # ================Reset Function End==================================
# ====================================================================================================================================================================
    
    # Install opencv Lib For Add Sample of Photo
    
    # ================Generate Data Set Take Photo Sample START=================
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Field are Required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                
                # All Data Store in Variable
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Name=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # =====================Load Predefined Data on Face Frontals from OpenCV=========
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling Factor = 1.3
                    # Minimun Neighbor = 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450)) # Image Crop
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # File Path
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0,),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Sets Completed!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Error",f"Due To:{str(es)}",parent=self.root)
        
    # ================Generate Data Set Take Photo Sample END===================
# ====================================================================================================================================================================
    
        
if __name__ == "__main__":
    root=Tk()
    obj =Student_Detail(root)
    root.mainloop()
    
    