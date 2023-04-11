# ====================================================================================================================================================================

from tkinter import* 
from tkinter import ttk  # ttk has style tool for style
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # For MYSQL Connect to Our Project
import cv2  # Face Recognition Lib
import os
import numpy as np
import tkinter
from tkinter.tix import IMAGETEXT
from time import strftime
from datetime import datetime
from os.path import isfile,join
from os import listdir
import face_recognition
# ====================================================================================================================================================================

# ============================================= Create A Class START ===============================================================
class Face_Recognition:
    # Then We need Call Construction should define by Def
    def __init__(self,root): # root is root window
        self.root = root
        # Set Window Geometry of Window
        self.root.geometry("1530x790+0+0") # (width x height + X-axis + y-axis)
        self.root.title("Face Recognition System") # Window Tab name 
        
# =====================================================================================================================================================================

        #Title of Label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0, width=1530, height=45) # Place ke Important isliye hota hai ki hum kahi par hi place kar sakte hai
        
# ====================================================================================================================================================================
        
        # ========================================== First Image =============================================
        img_top = Image.open(r"Images_for_Window\face-recog.jpg")        
        img_top = img_top.resize((650,700), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg_top) # self root mean line 14 
        f_lbl.place(x=0,y=40, width=650, height=700)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
        
# ====================================================================================================================================================================
        
        # Second Image
        img_buttom = Image.open(r"Images_for_Window\face_loading.jpg")        
        img_buttom = img_buttom.resize((950, 700), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
        self.photoimg_top_bottom = ImageTk.PhotoImage(img_buttom)

        # Ab humko image ko set krna window pe lable ke help se, We create Label
        f_lbl = Label(self.root,image=self.photoimg_top_bottom) # self root mean line 14 
        f_lbl.place(x=650,y=40, width=950, height=700)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 

# ====================================================================================================================================================================

        # Button
        b1 = Button(f_lbl, text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman", 18, "bold"),bg="darkgreen",fg="white")
        b1.place(x=365, y=620, width=200, height=40)
        
# ============================Attendance=======================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            # Condition not repeat Attendance
            if((i not in name_list) and (r not in name_list) and (n not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:/%M:/%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
                
# ====================================================================================================================================================================

# ============================Face Recognition=======================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            # Covert Image Into Gray Sacle
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                # Mysql Data base se Id Lena hoga
                conn=mysql.connector.connect(host="localhost", username='root',password="Mysql12345", database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute('SELECT Name FROM student where Student_id='+str(id))
                n = my_cursor.fetchone()
                n= '+'.join(n)

                my_cursor.execute('SELECT Roll FROM student where Student_id='+str(id))
                r = my_cursor.fetchone()
                r= '+'.join(r)

                my_cursor.execute('SELECT Dep FROM student where Student_id='+str(id))
                d = my_cursor.fetchone()
                d= '+'.join(d)
                
                my_cursor.execute('SELECT Student_id FROM student where Student_id='+str(id))
                i = my_cursor.fetchone()
                i= '+'.join(i)


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,225,225),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,225,225),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,225,225),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,225,225),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(225,225,225),3)

                coord=[x,y,w,h]
            return coord


#         # Function for Regcognition Image 
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(225,225,225),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"classifier.xml")

        cap=cv2.VideoCapture(0)

        while True:
            ret,img=cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
            # Video capture ko release Karna hai
        cap.release()
        cv2.destroyAllWindows()
# # ====================================================================================================================================================================

# ============================================= Create A Class END =================================================================

if __name__ == "__main__":
    root=Tk()
    obj =Face_Recognition(root)
    root.mainloop()