from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System
from time import strftime
from datetime import datetime
from tkinter.tix import IMAGETEXT 
import tkinter 
from PIL import Image,ImageTk
from student import Student_Detail
import os # Import System Directory 
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from chatbot import ChatBot


# =================================================================================================

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"Images_for_Window\login_bg.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=10,relheight=1, relwidth=1)
        
        frame = Frame(self.root, bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1 = Image.open(r"Images_for_Window\admin_bg.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started", font=("times new roman", 20, "bold"),bg="black",fg="white")
        get_str.place(x=95,y=100)
        
        # Label
        username = Label(frame,text="UserName:",font=("times new roman", 15, "bold"),bg="black",fg="white")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password = Label(frame,text="Password:",font=("times new roman", 15, "bold"),bg="black",fg="white")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman", 15, "bold"),show='*')
        self.txtpass.place(x=40,y=250,width=270)
        
        # ================= Icon Images ==============
        
        img2 = Image.open(r"Images_for_Window\admin_icon.png")
        img2=img2.resize((30,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=30,height=25)
        
        img3 = Image.open(r"Images_for_Window\pass.png")
        img3=img3.resize((30,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=30,height=25)
        
        # Login Button
        
        loginbtn = Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3, relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        # Regristration
        registerbtn = Button(frame,text="New User Register", command=self.register_window, font=("times new roman",10,"bold"),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground="black")
        registerbtn.place(x=20,y=350,width=160)
        
        # Forget password
        forgetpassbtn = Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground="black")
        forgetpassbtn.place(x=15,y=380,width=160)
        
        # =========================== Register Window Function =======================
    def register_window(self):  
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
# ===============================================================================================
    # LOgin FUNCTION
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","All Field required",parent=self.root)
        elif self.txtuser.get()=="Ranjeet" and self.txtpass.get()=="1234":
                messagebox.showinfo("Success","Welcome to Face Recognition System,",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invailed UserName & Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()

# ===============================================================================================
# ================= RESET Password Function =======================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select The Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter The Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter The New Password" ,parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
            my_cursor=conn.cursor()
            qury=('select * from register where email=%s and securityQ=%s and securityA=%s')
            value = (self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please Enter The Correct Answer" ,parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success",'Your Password has been reset, Please Login With New Password',parent=self.root2)
                self.root2.destroy()
# ===============================================================================================
# ================= Forget Function =======================================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please Enter The Email To Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error","Please Enter Valid UserName",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                # Create Label
                l = Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q = Label(self.root2,text="Select Security Question", font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["value"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(  self.root2,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
                
                self.txt_security = ttk.Entry( self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(  self.root2,text="New Password", font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                
                self.txt_newpass = ttk.Entry( self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn = Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white" ,bg="green")
                btn.place(x=100, y=290)
                
                

# ===============================================================================================
# =========================== Register Form  ================================

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # ============ Variable ================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        # ================= Bg Image ===============
        self.bg=ImageTk.PhotoImage(file=r"Images_for_Window\registerbg.png")
        bg_lbl =Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        # ================= Left Image ===============
        self.bg1=ImageTk.PhotoImage(file=r"Images_for_Window\left_image.jpg")
        left_lbl =Label(self.root,image=self.bg1)
        left_lbl.place(x=70,y=200,width=470,height=450)
        
        # ================= Main Image ===============
        
        frame=Frame(self.root,bg="white")
        frame.place(x=540,y=200,width=800,height=450)
        
        # ================= Register Label ===============
        register_lbl =Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="darkgreen")
        register_lbl.place(x=20,y=20)
        
        # ================= Label and Entry ===============
        # Row 1
        fname=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=80)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=110,width=250)
        
        lname=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=80)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=110,width=250)
        
        #------------------Row2
        contact = Label(frame,text="Contact No", font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=150)
        
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=180,width=250)
        
        email=Label(frame,text="Email", font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=150)
        
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=180,width=250)
        
        #------------------Row3
        security_Q = Label(frame,text="Select Security Question", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=220)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=250,width=250)
        self.combo_security_Q.current(0)
        
        security_Q=Label(frame,text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=370,y=220)
        
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=250,width=250)
        
        #------------------Row4
        pswd = Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=290)
        
        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=320,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=290)
        
        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=320,width=250)
        
        # --------Check Button-----------
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditons",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=360)
        
        # ========== Button ===========
        img = Image.open(r"Images_for_Window\register_now.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage, command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=390,width=200)
        
        img1 = Image.open(r"Images_for_Window\login_now.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1 = Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=390,width=200)
        
        
        # ================= Function Declartion=================
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passsword & Confirm Password Must Be Same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exit,Please Try Another Email",parent=self.root) 
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get()
                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully",parent=self.root)
            
# ========================================================================================================
# =============== Return Login Button Function =================
def return_login(self):
    self.root.destroy()

# ========================================================================================================
# =============== Main Project=================
class Face_Recognition_System:
    # Then We need Call Construction should define by Def
    def __init__(self, root): # root is root window
        self.root = root
        # Set Window Geometry of Window
        self.root.geometry("1530x790+0+0") # (width x height + X-axis + y-axis)
        self.root.title("Face Recognition System") # Window Tab name 
        
# ====================================================================================================================================================================

        # # Insert One Image From Folder 
        img = Image.open(r"Images_for_Window\face_recognition.jpg")
        
        # Size Set of Image
        img = img.resize((500, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg = ImageTk.PhotoImage(img)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg) # self root mean line 14 
        f_lbl.place(x=0,y=0, width=550, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis
        
# ====================================================================================================================================================================
        
        # Insert Two Image From Folder
        img2 = Image.open(r"Images_for_Window\face1.png")
        
        # Size Set of Image
        img2 = img2.resize((500, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg2) # self root mean line 14 
        f_lbl.place(x=500,y=0, width=520, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis

# ====================================================================================================================================================================
        
        # Insert Three Image From Folder
        img3 = Image.open(r"Images_for_Window\face_recognition.jpg")
        
        # Size Set of Image
        img3 = img3.resize((500, 130), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg3) # self root mean line 14 
        f_lbl.place(x=1000,y=0, width=550, height=130)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
        
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
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=45) # Place ke Important isliye hota hai ki hum kahi par hi place kar sakte hai
# ====================================================================================================================================================================
        
        # ================= Time =================================
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text = string)
                lbl.after(1000, time)
        
        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110, height=50)
        time()
        
# ====================================================================================================================================================================
        # Create a Student Image Button
        # Student detail Insert Image Background From Folder
        img5 = Image.open(r"Images_for_Window\student.jpg")
        img5 = img5.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        # Student Details Section for Image position 
        b1 = Button(bg_img, image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        
        # Student Detail Section for Image Button position
        b1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=200, y=300, width=220, height=40)
        
# ====================================================================================================================================================================
        
        # Create a Detect Face Image Button
        img6 = Image.open(r"Images_for_Window\face_detect.jpg")
        img6 = img6.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)
        
            # This Section for Image Button position
        b1 = Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=500, y=300, width=220, height=40)
        
# ====================================================================================================================================================================
        
        # Create a Attendance Button
        img7 = Image.open(r"Images_for_Window\attendance.jfif")
        img7 = img7.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=220, height=220)
        
        # This Section for Image Button position
        b1 = Button(bg_img, text="Attendance",cursor="hand2",command=self.attendance_data,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=800, y=300, width=220, height=40)
        
# ====================================================================================================================================================================
        
        # Create a Help Button
        img8 = Image.open(r"Images_for_Window\help.jpg")
        img8 = img8.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.chatbot)
        b1.place(x=1100, y=100, width=220, height=220)
        
        # This Section for Image Button position
        b1 = Button(bg_img, text="ChatBot",cursor="hand2",command=self.chatbot,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=1100, y=300, width=220, height=40)
        
# ====================================================================================================================================================================
        
        # Create a Train Data Button
        img9 = Image.open(r"Images_for_Window\train.jpg")
        img9 = img9.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)
        
        # This Section for Image Button positioncommand=self.train_data
        b1 = Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=200, y=580, width=220, height=40)
        
# ====================================================================================================================================================================
        
        # Create a Photo Data Button
        img10 = Image.open(r"Images_for_Window\collection.jpg")
        img10 = img10.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.open_image)
        b1.place(x=500, y=380, width=220, height=220)
        
        # This Section for Image Button position
        b1 = Button(bg_img, text="Photos Data",cursor="hand2",command=self.open_image,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=500, y=580, width=220, height=40)
    
# ====================================================================================================================================================================
    
        
        # Create a Developer Button
        img11 = Image.open(r"Images_for_Window\developer.jpg")
        img11 = img11.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)
        
        # This Section for Image Button position
        b1 = Button(bg_img, text="Developer",cursor="hand2",command=self.developer_data,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=800, y=580, width=220, height=40)
        
# ====================================================================================================================================================================
        
        # Create a Exit Button
        img12 = Image.open(r"Images_for_Window\exit.jpg")
        img12 = img12.resize((220,220), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        # This Section for Image position 
        b1 = Button(bg_img, image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=380, width=220, height=220)
        
        # Exit Section for Image Button position
        b1 = Button(bg_img, text="Exit",cursor="hand2",command=self.iExit,font=("times newr roman", 15, "bold"),bg="darkblue",fg="white")
        b1.place(x=1100, y=580, width=220, height=40)
        
# ====================================================================================================================================================================

# =============Function Button Start =======================================
    def open_image(self):
        os.startfile("data")

# =============Function Button Start =======================================

# ====================================================================================================================================================================

# ===============Functions buttons Start====================================
    def student_details(self):
        self.root.new_window=Toplevel(self.root)
        self.app=Student_Detail(self.root.new_window)
        
# ===============Function Button End =======================================

# ====================================================================================================================================================================

# ===============Functions buttons==========================================
    def train_data(self):
        self.root.new_window=Toplevel(self.root)
        self.app=Train(self.root.new_window)

# ===============Function Button End =======================================

# ====================================================================================================================================================================

# ===============Functions buttons==========================================
    def face_data(self):
        self.root.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.root.new_window)

# ===============Function Button End =======================================

# ====================================================================================================================================================================

# ===============Functions buttons==========================================
    def attendance_data(self):
        self.root.new_window=Toplevel(self.root)
        self.app=Attendance(self.root.new_window)

# ===============Function Button End =======================================
# ====================================================================================================================================================================

# ===============Functions buttons==========================================
    def developer_data(self):
        self.root.new_window=Toplevel(self.root)
        self.app=Developer(self.root.new_window)

# ===============Function Button End =======================================
# ====================================================================================================================================================================
# ===============Chatbot Function buttons==========================================
    def chatbot(self):
        self.root.new_window=Toplevel(self.root)
        self.app=ChatBot(self.root.new_window)

# ===============Function Button End =======================================

# ===============EXIT Functions buttons==========================================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
# ===============EXIT Function Button End =======================================
            

if __name__ == "__main__":
    main()