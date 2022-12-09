from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil
class Sorting_app:
    def __init__(self,root):
        self.root=root
        self.root.title("Sorting App  | Developed by gopal")
        self.root.geometry("1350x7000+0+0")
        self.root.config(bg="black")
        self.logo_icon=PhotoImage(file="img/Folder-icon (1).png")
        title=Label(self.root,text="Files Sorting", font=("impact",40),image=self.logo_icon,compound="left",bg="#023548",fg="white").place(x=0,y=0,relwidth=1,height=100)

        #====================section 1=================
        self.var_foldername=StringVar()

        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",15,"bold"),bg="black",fg="white").place(x=50,y=120)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=250,y=120,height=35,width=600)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",font=("times new roman",15,"bold"),cursor="hand2",activebackground="#262626",activeforeground="white",bg="#262626",fg="white").place(x=900,y=120)
        hr=Label(self.root,bg="lightgrey").place(x=15,y=180,height=2,width=1300)

        # ====================section 2=================
        #====================Extentions++++++++++++++
        self.image_extentions=["Image Extentions" ,".jpg", ".png"]
        self.video_extentions = ["Video Extentions", ".mp4", ".mkv"]
        self.audio_extentions = ["Audio Extentions", ".mp3", ".wav"]
        self.document_extentions = ["Documents Extentions", ".doc", ".xlsx",".xls", ".zip", ".pdf", ".rar"]

        self.folders = {
                'videos': self.video_extentions,
                'audios': self.audio_extentions,
                'images': self.image_extentions,
                'documents': self.document_extentions,
        }

        lbl_support_ext = Label(self.root, text="Varios Supported extensions",bg="black",fg="white",font=("times new roman", 15, "bold")).place(x=50,y=200)
        self.image_box=ttk.Combobox(self.root,values=self.image_extentions,justify=CENTER,font=("times new roman",15),state='readonly')
        self.image_box.place(x=60,y=250)
        self.image_box.current(0)

        self.video_box = ttk.Combobox(self.root, values=self.video_extentions, justify=CENTER,font=("times new roman", 15), state='readonly')
        self.video_box.place(x=310, y=250)
        self.video_box.current(0)

        self.audio_box = ttk.Combobox(self.root, values=self.audio_extentions, justify=CENTER,font=("times new roman", 15), state='readonly')
        self.audio_box.place(x=560, y=250)
        self.audio_box.current(0)

        self.document_box = ttk.Combobox(self.root, values=self.document_extentions, justify=CENTER,font=("times new roman", 15), state='readonly')
        self.document_box.place(x=810, y=250)
        self.document_box.current(0)


        #===========================section3++++++++++++++++++++
        #===========================All Image Icons+++++++++++++++++++++

        self.image_icon = PhotoImage(file="img/photos-icon-8.png")
        self.video_icon = PhotoImage(file="img/Videos-icon.png")
        self.audio_icon = PhotoImage(file="img/Audio-File-icon.png")
        self.document_icon = PhotoImage(file="img/Folder-Documents-icon.png")
        self.other_icon = PhotoImage(file="img/question-mark-icon-png-clipart-best-GHJOjX-clipart.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="black")
        Frame1.place(x=50,y=300,width=1270,height=300)
        self.lbl_total_files = Label(Frame1, text="Total Files:",bg="black",fg="white",font=("times new roman", 15, "bold"))
        self.lbl_total_files.place(x=10, y=10)

        self.lbl_total_image=Label(Frame1, bd=3, relief=RAISED,image=self.image_icon,bg="#087587")
        self.lbl_total_image_no = Label(Frame1,font=("times new roman", 15, "bold"),bg="black",fg="white")
        self.lbl_total_image_no.place(x=20,y=260)
        self.lbl_total_image.place(x=10,y=50,width=230,height=200)

        self.lbl_total_video = Label(Frame1, bd=3, relief=RAISED, image=self.video_icon, bg="#087587")
        self.lbl_total_video.place(x=260, y=50, width=230, height=200)
        self.lbl_total_video_no = Label(Frame1,font=("times new roman", 15, "bold"),bg="black",fg="white")
        self.lbl_total_video_no.place(x=290, y=260)

        self.lbl_total_audio = Label(Frame1, bd=3, relief=RAISED, image=self.audio_icon, bg="#087587")
        self.lbl_total_audio.place(x=520, y=50, width=230, height=200)
        self.lbl_total_audio_no = Label(Frame1, font=("times new roman", 15, "bold"),bg="black",fg="white")
        self.lbl_total_audio_no.place(x=550, y=260)

        self.lbl_total_document = Label(Frame1, bd=3, relief=RAISED, image=self.document_icon,bg="#087587")
        self.lbl_total_document.place(x=780, y=50, width=230, height=200)
        self.lbl_total_document_no = Label(Frame1, font=("times new roman", 15, "bold"),bg="black",fg="white")
        self.lbl_total_document_no.place(x=810, y=260)

        self.lbl_total_other = Label(Frame1, bd=3, relief=RAISED, image=self.other_icon, bg="#087587")
        self.lbl_total_other.place(x=1040, y=50, width=220, height=200)
        self.lbl_total_other_no = Label(Frame1, font=("times new roman", 15, "bold"),bg="black",fg="white")
        self.lbl_total_other_no.place(x=1070, y=260)

        #=================== section 4================
        lbl_status = Label(self.root, text="STATUS",font=("times new roman", 15, "bold"),bg="black",fg="white").place(x=50, y=620)
        self.lbl_st_total = Label(self.root, text=" ", font=("times new roman", 15, "bold"),fg="green")
        self.lbl_st_total.place(x=250, y=620)

        self.lbl_st_moved = Label(self.root, text=" ", font=("times new roman", 15, "bold"),fg="blue")
        self.lbl_st_moved.place(x=500, y=620)

        self.lbl_st_left = Label(self.root, text=" ", font=("times new roman", 15, "bold"),fg="orange")
        self.lbl_st_left.place(x=750, y=620)


        #====================buttons=====================
        self.btn_clear_button = Button(self.root,command=self.clear, text="CLEAR", font=("times new roman", 15, "bold"), cursor="hand2",activebackground="green", activeforeground="white", bg="#262626", fg="white")
        self.btn_clear_button.place(x=920, y=610,width=120,height=50)

        self.btn_start_button = Button(self.root,state=DISABLED,command=self.start_function, text="START",font=("times new roman", 15, "bold"),cursor="hand2", activebackground="green", activeforeground="white", bg="#262626",fg="white")
        self.btn_start_button.place(x=1100, y=610, width=120, height=50)

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        combine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    #print(folder_name)
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1

                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios+=1

                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos+=1

                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents+=1
         #=============other files==================
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                ext = "." + i.split(".")[-1]
                if ext.lower() not in combine_list:
                    others+=1

        self.lbl_total_image_no.config( text="Total Images: "+str(images))
        self.lbl_total_audio_no.config( text="Total Audios: "+str(audios))
        self.lbl_total_video_no.config( text="Total Videos: "+str(videos))
        self.lbl_total_document_no.config( text="Total Documents: "+str(documents))
        self.lbl_total_other_no.config( text="Total Others: "+str(others))
        self.lbl_total_files.config( text="Total files:"+str(self.count))

    def browse_function(self):
        op=filedialog.askdirectory(title="Select folder for sorting")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directry = self.var_foldername.get()
            self.other_name ="others"
            self.rename_folder()

            self.all_files = os.listdir(self.directry)
            length = len(self.all_files)
            count = 1
            self.Total_count()
            self.btn_start_button.config(state=NORMAL)
            # print(self.all_files)

    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear_button.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry, i)) == True:
                    c += 1
                    self.create_move(i.split(".")[-1], i)
                    self.lbl_st_total.config( text="TOTAL : "+str(self.count),bg="black",fg="white")
                    self.lbl_st_moved.config(text="MOVED : " + str(c),bg="black",fg="white")
                    self.lbl_st_left.config(text="LEFT : " + str(self.count-c),bg="black",fg="white")

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()

            messagebox.showinfo("Success","ALl files has moved successfully")
            self.btn_start_button.config(state=DISABLED)
            self.btn_clear_button.config(state=NORMAL)
        else:
            messagebox.showerror("Error","please select folder")

    def clear(self):
        self.btn_start_button.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text=" ")
        self.lbl_st_moved.config(text=" ")
        self.lbl_st_left.config(text=" ")
        self.lbl_total_image_no.config(text=" ")
        self.lbl_total_audio_no.config(text="")
        self.lbl_total_video_no.config(text="")
        self.lbl_total_document_no.config(text="")
        self.lbl_total_other_no.config(text=" ")
        self.lbl_total_files.config(text="Total Files:")

    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry, folder)) == True:
                os.rename(os.path.join(self.directry, folder), os.path.join(self.directry, folder.lower()))

    def create_move(self,ext, file_name):
        find = False
        for folder_name in self.folders:
            if "." + ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry, folder_name))
                shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, folder_name))
                find = True
                break
        if find != True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry, self.other_name))
            shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, self.other_name))

root=Tk()
obj=Sorting_app(root)
root.mainloop()
