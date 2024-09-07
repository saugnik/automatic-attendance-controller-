from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Regonition System")

        #first img
        img=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\top picture.jpeg")
        img=img.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second img
        img1=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\background.jpeg")
        img1=img1.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third img
        img2=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\backgroud 2.webp")
        img2=img2.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg img
        img3=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\main background.jpeg")
        img3=img3.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35," bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=650)

        #left label frame
        Left_Frame=Left_Frame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_Frame.place(x=10,width=760,height=500)

        img_left=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\backgroud 2.webp")
        img_left=img_left.resize((720,130),Image.Resampling.NEAREST(0))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=5,y=0,width=550,height=130)

        #current course
        Current_course_Frame=Left_Frame(main_frame,bd=2,relief=RIDGE,text="Current course",font=("time new roman",12,"bold"))
        Current_course_Frame.place(x=5,y=135,width=720,height=150)

        #Year
        year_label=Label(Current_course_Frame,text="department",font=("time new roman",12,"bold",),bg="white"state="read only")
        year_label.grid(row=0,column=0,padx=10)
        year_combo-ttk.Combobox(Current_course_Frame,font=("time new roman",12,"bold"),width=17)
        year_combo["values"]=("select department","second year(A)","second year(B)","Third year","forth year")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=w)

        #Student info
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Info")
        class_student_frame.place(x=5,y=250,width=720,height=300)

        


        

        #Right label frame
        Right_Frame=Left_Frame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_Frame.place(x=740,width=660,height=500)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()