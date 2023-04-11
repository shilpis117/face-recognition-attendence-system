from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title('ChatBot')
        self.root.geometry("750x620+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        main_frame= Frame(self.root,bd=4,bg='powder blue', width=610)
        main_frame.pack()
        
        img_chat = Image.open('Images_for_Window/chat.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_chat)
        
        Title_label = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT ME",font=("arial",30,"bold"),fg="green",bg="white")
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        # Button 
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()
        
        label_1=Label(btn_frame,text="Type Something", font=('times new roman',14, "bold"),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5, sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40, font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn_frame,text="Send>>",command=self.send, font=('arial ',15,'bold'),bg='green',width=8)
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clare=Button(btn_frame,text="Clear Data",command=self.clear, font=('arial ',15,'bold'),bg='red',fg='white',width=8)
        self.clare.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg, font=('times new roman',14, "bold"),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5, sticky=W)
        
        # ==========================================================================================================
        
        # ============== Function Declaration =============================================
        
# ======================================================================================
        
    # Enter Function
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('') 
# ======================================================================================
# ================= Clear Function ===================
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

# ======================================================================================

    
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        if (self.entry.get()==""):
            self.msg="Please Enter Some Text"
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')
        
        if (self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
            
        elif (self.entry.get()=="How Are You?"):
            self.text.insert(END,"\n\n"+"Bot: Fine And You")
        
        elif (self.entry.get()=="How Are You?"):
            self.text.insert(END,"\n\n"+"Bot: Fine And You")
        
        elif (self.entry.get()=="Fantastic"):
            self.text.insert(END,"\n\n"+"Bot: Nice To Hear")
        
        elif (self.entry.get()=="Who Created You?"):
            self.text.insert(END,"\n\n"+"Bot: Subhi and His Team Using Python")
            
        elif (self.entry.get()=="What Is Your Name?"):
            self.text.insert(END,"\n\n"+"Bot: My Name is Mr.Hacker")
        
        elif (self.entry.get()=="Can You Speck Marathi?"):
            self.text.insert(END,"\n\n"+"Bot: I'm still Learnig it.. ")

        elif (self.entry.get()=="What Is Machine Learning?"):
            self.text.insert(END,"\n\n"+"Bot: Machine Learning Is A Branch\n of Artificial Intellicial (AI) Focused\n on building application that learn\n form data and improve that accuracy\n over time without being programmed\n to do so. ")
            
        elif (self.entry.get()=="How Does Face Recognition Work?"):
            self.text.insert(END,"\n\n"+"Bot: Facial Recognition is a Way of\n Recognizing a Human Face Through\n technology. A Facial recognition\n system uses biometrics to map\n facial Feature from a photographer\n or video. It Compares the information with a database of knows faces to fine\n a match ")
            
        elif (self.entry.get()=="How Does Face Recognition Work Step by Step?"):
            self.text.insert(END,"\n\n"+"Bot: Step 1: Face detection. The Camera\n detects and locates the Image of a face,\neither alone or in a crowd. ...\nStep 2: Face Analysis. Next, an Image of\n the face is captured and analyzed. ...\nStep 3: ")

        elif (self.entry.get()=="How Many Countries use Facial Recognition?"):
            self.text.insert(END,"\n\n"+"Bot: In Use  98\n Approved, but not Implemented 12\n Considering facial recognition technology 13\n No Evidence of use 68")
    
        elif (self.entry.get()=="What is Python Programming?"):
            self.text.insert(END,"\n\n"+"Bot: Python is a General Purpose \n High Level Programming Language.\nYou can use Python for Developing\ndesktop GUI applications, Website\nand Web application. Also, Python,\nas ahigh")
        
        elif (self.entry.get()=="What is ChatBot?"):
            self.text.insert(END,"\n\n"+"Bot: A Chatbot is a Computer \nProgram that's Designed to \nsimulate human Conversation")

        elif (self.entry.get()=="Bye"):
            self.text.insert(END,"\n\n"+"Bot: Thank You For Chatting")
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I did'nt get it")
            
            
            
            
            
            
            
if __name__ == '__main__':
    root=Tk()
    obj = ChatBot(root)
    root.mainloop()