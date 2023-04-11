# First Install tkinter by Using Pip 
# Instal Pillow by using Pip for Image

# ====================================================================================================================================================================

from time import strftime
from datetime import datetime
import tkinter
from tkinter import* 
from tkinter import ttk  # ttk has style tool for style
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

# ====================================================================================================================================================================


# Create A Class
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
# ====================================================================================================================================================================
 
        
# ===============EXIT Functions buttons==========================================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this Project",parent=self.root)
        if self.iExit>0:
                self.root.destroy()
        else:
                return
# ===============EXIT Function Button End =======================================
        
# ====================================================================================================================================================================


if __name__ == "__main__":
    root=Tk()
    obj =Face_Recognition_System(root)
    root.mainloop()
    
    