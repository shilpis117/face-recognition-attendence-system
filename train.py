import os
from tkinter import* 
from tkinter import ttk  # ttk has style tool for style
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # For MYSQL Connect to Our Project
import cv2  # Face Recognition Lib
from os import listdir
from os.path import isfile, join
import numpy as np


# Create A Class
class Train:
        # Then We need Call Construction should define by Def
        def __init__(self, root): # root is root window
                self.root = root
                # Set Window Geometry of Window
                self.root.geometry("1530x790+0+0") # (width x height + X-axis + y-axis)
                self.root.title("Face Recognition System") # Window Tab name 

        # ==========================================================================

                #Title of Label
                title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),bg="white",fg="red")
                title_lbl.place(x=0,y=0, width=1530, height=45) # Place ke Important isliye hota hai ki hum kahi par hi place kar sakte hai

        # ==========================================================================
                
                img_top = Image.open(r"Images_for_Window\Data_bg.jpg")        
                img_top = img_top.resize((1530, 300), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
                self.photoimg_top = ImageTk.PhotoImage(img_top)

                # Ab humko image ko set krna window pe lable ke help se, We create Label
                f_lbl = Label(self.root,image=self.photoimg_top) # self root mean line 14 
                f_lbl.place(x=0,y=40, width=1530, height=325)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 
                
        # ==========================================================================

                # Button
                b1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman", 30, "bold"),bg="red",fg="white")
                b1.place(x=0, y=350, width=1530, height=90)
                
        # ==========================================================================
                
                img_buttom = Image.open(r"Images_for_Window\multi_people.jpg")        
                img_buttom = img_buttom.resize((1530, 325), Image.ANTIALIAS) #((width, height, ANTIALIAS is use of High level image covert into low level Image))
                self.photoimg_top_bottom = ImageTk.PhotoImage(img_buttom)

                # Ab humko image ko set krna window pe lable ke help se, We create Label
                f_lbl = Label(self.root,image=self.photoimg_top_bottom) # self root mean line 14 
                f_lbl.place(x=0,y=440, width=1530, height=325)   # ab humko image place dena mean kaha par set krna hai. by using x-axis and Y-axis 


# ==========================================================================
        def train_classifier(self):
                data_dir=("data/")
                path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
                
                faces=[]
                ids=[]
                
                for image in path:
                        img=Image.open(image).convert('L') # Gray Scale Image
                        imageNp=np.array(img,'uint8')
                        id = int(os.path.split(image)[-1].split('.')[1])
                        
                        faces.append(imageNp)
                        ids.append(id)
                        cv2.imshow("Training",imageNp)
                        cv2.waitKey(1)==13
                # Ids ko Numpy main convert karna hai
                ids=np.array(ids)
                
# ==========================Train the classifier AND Save=============================
                
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Training datasets completed!!",parent=self.root)


if __name__ == "__main__":
        root=Tk()
        obj =Train(root)
        root.mainloop()