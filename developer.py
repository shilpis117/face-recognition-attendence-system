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
class Developer:
    # Then We need Call Construction should define by Def
    def __init__(self, root): # root is root window
        self.root = root
        # Set Window Geometry of Window
        self.root.geometry("1530x790+0+0") # (width x height + X-axis + y-axis)
        self.root.title("Face Recognition System") # Window Tab name 
        
# ====================================================================================================================================================================

        # ======================================= Title of Label =======================================================================
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0, width=1530, height=45) # Place ke Important isliye hota hai ki hum kahi par hi place kar sakte hai

# ====================================================================================================================================================================
        
        img_top = Image.open(r"Images_for_Window\developer.jpg")        
        img_top = img_top.resize((1530, 740), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg_top) # self root mean line 14 
        f_lbl.place(x=0,y=40, width=1530, height=740)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 

# ====================================================================================================================================================================
        
        # =========================================== Create A Frame In the Developer ====================================================
        main_frame = Frame(f_lbl, bd=2, bg="white",relief=RAISED) # bd is Border
        main_frame.place(x=300, y=50, width=800, height=600)

# ====================================================================================================================================================================
        
        #img_top1 = Image.open(r"Images_for_Window\student.jpg")        
        #img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        #self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # Ab humko image ko set krna window pe lable ke help se, We create Label
        #f_lbl = Label(main_frame,image=self.photoimg_top1) # self root mean line 14 
        #f_lbl.place(x=300,y=0, width=200, height=200)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
       
# ====================================================================================================================================================================
        
        # ============================================ Developer Info =====================================================================
        dev_label = Label(main_frame, text='FACE RECOGNITION ATTENDANCE SYSTEM',font=("times new roman", 20, "bold"),bg="white",fg="red")
        dev_label.place(x=60,y=10)
        
        dev_label = Label(main_frame, text='This is a face recognition attendence system which incorporartes ',font=("times new roman", 20, "bold"),bg="white" ,fg="black")
        dev_label.place(x=0,y=40)

        dev_label = Label(main_frame, text='facial recognition technology to recognize and verify students ',font=("times new roman", 20, "bold"),bg="white",fg="black")
        dev_label.place(x=0,y=80)
        
        dev_label = Label(main_frame, text='facial features and to record attendence automatically.',font=("times new roman", 20, "bold"),bg="white" ,fg="black")
        dev_label.place(x=0,y=120)

        dev_label = Label(main_frame, text='DEVELOPER INCLUDES',font=("times new roman", 20, "bold"),bg="white",fg="green")
        dev_label.place(x=0,y=200)
        
        dev_label = Label(main_frame, text='1.Surbhi Shilpi (Full Stack Developer)\n2.Simran Vishwakarma (Frontend Developer)\n3.Sonali Gupta  (Backend Developer)\n4.Sneha Khodke  (Tester AND Integration)',font=("times new roman", 20, "bold"),bg="white" ,fg="blue")
        dev_label.place(x=0,y=260)

        #dev_label = Label(main_frame, text='Hello My Name Sneha Khodke',font=("times new roman", 20, "bold"),bg="white",fg="blue")
        
        #dev_label.place(x=0,y=5)
        
        #dev_label = Label(main_frame, text='I am  Tester',font=("times new roman", 20, "bold"),bg="white" ,fg="blue")
        #dev_label.place(x=0,y=40)
# ====================================================================================================================================================================


if __name__ == "__main__":
    root=Tk()
    obj =Developer(root)
    root.mainloop()