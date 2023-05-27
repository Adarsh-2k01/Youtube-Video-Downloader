from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from pytube import YouTube
class Error(Exception):
    pass
class validerror(Error):
    pass
a=Tk()
a.geometry('800x600+350+100')
a.minsize(800,600)
a.title("YOUTUBE VIDEO DOWNLOADER")
a.iconbitmap("E:\python works\downloader icon.ico")
F1=Frame(a,width=1900,height=1800)
F1.pack()
img=ImageTk.PhotoImage(Image.open("E:\python works\canvas bg.jpg"))
label=Label(F1,image=img)
label.pack()
L1=Label(a,text="ENTER THE VIDEO URL:",font=("Roboto", 30,"bold"),borderwidth=5,relief="solid",bg="#ADD8E6",fg="#191C27")
L1.place(x=550,y=150)
def temp_text(e):
    E1.delete(0,"end")
link=StringVar()
E1=Entry(a,textvariable=link,border=3,font=("signal",20,"bold"),borderwidth=5,relief="solid",fg="#964C1D",bg="#ADD8E6")
#E1.insert(0,'Paste  the URL Here...')
E1.place(x=620,y=300)
#E1.bind("<FocusIn>", temp_text)

m=Menu(a)
a.config(menu=m)
FileMenu=Menu(m)
m.add_cascade(label="File",menu=FileMenu)
EditMenu=Menu(m)
m.add_cascade(label="Edit",menu=EditMenu)
OptionMenu=Menu(m)
m.add_cascade(label="Option",menu=OptionMenu)
def cmdExit():
    m=messagebox.askquestion('Exit Application','Are you sure want to exit this application!')
    if m=='yes':
        a.destroy()
    else:
        a.mainloop()
FileMenu.add_command(label="Exit",command=cmdExit)
def cmdClear():
    E1.delete(0,"end")
EditMenu.add_command(label="Clear",command=cmdClear)
def cmdSelectAll():
   E1.select_range(0,"end")
EditMenu.add_command(label="Select All",command=cmdSelectAll)
def cmdAbout():
    b=Tk()
    b.geometry('300x400+350+100')
    b.minsize(300,400)
    b.maxsize(300,400)
    b.title("About")
    b.iconbitmap("E:\python works\downloader icon.ico")
    C1=Canvas(b,width=800,height=750,bg="lightblue",border=5)
    C1.create_text(550, 400, text= "This is free YouTube Downloader",fill="black",font=('Helvetica 10 bold'))
    C1.create_text(550, 470, text= "You can download required videos of your",fill="black",font=('Helvetica 10 bold'))
    C1.create_text(550, 485, text= "need",fill="black",font=('Helvetica 10 bold'))
    C1.create_text(550, 555, text= "Email:adarshjs2001@gmail.com",fill="black",font=('Helvetica 10 bold'))
    C1.create_text(550, 625, text= "Thanks for downloading this program",fill="black",font=('Helvetica 10 bold'))
    C1.create_text(550, 645, text= "(｡◕‿◕｡)",fill="black",font=('Helvetica 10 bold'))
    C1.place(anchor='center')
    def close_button():
        b.destroy()
    B1=Button(b,text="Close",width=42,bg="#ADD8E6",activebackground="#DCAE96",relief=RIDGE,cursor="hand2",command=close_button)
    B1.place(x=0,y=375)
    b.mainloop()
OptionMenu.add_command(label="About",command=cmdAbout)

def go_button():
    d=link.get()
    try:
        if d=="":
            raise validerror
        else:
            c=Tk()
            c.geometry('800x500+350+100')
            c.title("YOUTUBE VIDEO DOWNLOADER")
            c.iconbitmap("E:\python works\downloader icon.ico")
            c.config(bg="#ADD8E6")
##            ca=Canvas(c)
##            img1=ImageTk.PhotoImage(Image.open("frame 2.jpg","r"))
##            ca.create_image(1,1,anchor=NE,image=img1)
            F2=Frame(c,width=1000,height=800)
            F2.place(x=160,y=10)
            L2=Label(c,text="*Choose a serial number!!",font=('Helvetica 12 bold'),bg="#ADD8E6",fg="#FF0000")
            L2.place(x=660,y=280)
##            label1=Label(F2,image=img1)
##            label1.pack()
##            style=ttk.Style()
##            style.configure("mystyle.Treeview",font=("signal",20,"bold"),rowheight=10)
##            style.configure("mystyle.Treeview.Heading",font=("signal",20,"bold"))
            col=("Serial. no.","Resolution")
            tree=ttk.Treeview(F2,columns=col,show="headings")
            for i in col:
                tree.heading(i,text=i)
                if i=="Resolution":
                    tree.column(i,width=1000)
                tree.grid(row=1,column=0,columnspan=2)
                tree.pack(fill=X)
##            for line in range(0):
##                F2.insert(END,line)
            yt=YouTube(d)
            videos=yt.streams.filter(file_extension='mp4',progressive=True)
            for i in videos:
                aaa=videos.index(i)+1
                tree.insert("","end",values=(aaa,i))
            E2=Entry(c,textvariable=IntVar,border=3,font=("signal",20,"bold"),borderwidth=5,relief="solid",fg="#964C1D",bg="#ADD8E6")
            E2.place(x=600,y=350)
            def download():
                g=int(E2.get())-1
                videos[int(g)].download()
            B3=Button(c,text="DOWNLOAD",width=10,height=2,bg="#ADD8E6",activebackground="#d5c1aa",relief=RAISED,cursor="hand2",command=download)
            B3.place(x=720,y=440)
            c.mainloop()
        
    except validerror:
        msg=messagebox.showerror("ERROR","Not a valid URL")
##E1.bind("<FocusIn>", temp_text)
##E1.insert(0,'Paste  the URL Here...')    
B2=Button(a,text="GO",width=10,height=2,bg="#ADD8E6",highlightbackground="black",highlightthickness=4,bd=4,activebackground="#964C1D",relief=RAISED,cursor="hand2",command=go_button)
B2.place(x=732,y=390)
a.bind('<Return>',lambda event:go_button())
a.focus()
a.mainloop()


