from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

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
        b1 = Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
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
        
if __name__ == '__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()
    