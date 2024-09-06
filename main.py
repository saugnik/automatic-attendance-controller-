from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
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


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35," bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student details
        img4=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\main background.jpeg")
        img4=img4.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(bg_img,text="Students details",cursor="hand2",font=("times of roman",15,"bold"),bg="white",fg="red")
        b2.place(x=200,y=200,width=220,height=40)


        #detect face button
        img5=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\attendace.jpg")
        img5=img5.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg5=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(bg_img,text="Students details",cursor="hand2",font=("times of roman",15,"bold"),bg="white",fg="red")
        b2.place(x=500,y=300,width=220,height=40)


        #detection
        img5=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\attendace.jpg")
        img5=img5.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg5=ImageTk.PhotoImage(img4)

        b3=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b3.place(x=200,y=100,width=220,height=220)

        b4=Button(bg_img,text="Detection",cursor="hand2",font=("times of roman",15,"bold"),bg="white",fg="red")
        b4.place(x=700,y=400,width=220,height=40)



        #train data
        img6=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\train data.jpeg")
        img6=img6.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg6=ImageTk.PhotoImage(img4)

        b5=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b5.place(x=200,y=500,width=220,height=220)

        b6=Button(bg_img,text="Detection",cursor="hand2",font=("times of roman",15,"bold"),bg="white",fg="red")
        b6.place(x=500,y=1300,width=220,height=40)


        #Exit
        img6=Image.open(r"C:\Users\Saugnik\Desktop\attendance controller\pictures for this project\exit button.png")
        img6=img6.resize((500,130),Image.Resampling.NEAREST(0))
        self.photoimg6=ImageTk.PhotoImage(img4)

        b5=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b5.place(x=700,y=500,width=220,height=220)

        b6=Button(bg_img,text="Detection",cursor="hand2",font=("times of roman",15,"bold"),bg="white",fg="red")
        b6.place(x=700,y=1400,width=220,height=40)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()