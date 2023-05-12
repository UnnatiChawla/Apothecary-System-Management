from logging import root
from tkinter import*
from PIL import Image,ImageTk
from click import command
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class ApothecaryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Apothecary Management System")
        self.root.geometry("1530x800+0+0")
        app_icon=PhotoImage(file="E:\Pharmancy Management System\Apothecary\logo1.png")
        self.root.iconphoto(TRUE,app_icon)
        
        #addmed variable
        self.addmed_var=StringVar()
        self.refmed_var=StringVar()
        
        #main text variable
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()
        
        
        
        
        lbltitle=Label(self.root,text="APOTHECARY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='black',fg="teal",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill='x')
        
        
        img1=Image.open("E:\Pharmancy Management System\Apothecary\logo1.png")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=15,y=16)
        
        #dataframe
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20, bg="black")
        DataFrame.place(x=20,y=120,width=1500,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",bg="black",fg="teal",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",bg="black",fg="teal",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=520,height=350)
        
        #button frame
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20,bg="black")
        ButtonFrame.place(x=0,y=520,width=1530,height=70)
        
        #main button
        
        btnAddData=Button(ButtonFrame,command=self.addmeddata,text="Add Medicine",font=("arial",12,"bold"),bg="beige",fg="black")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateData=Button(ButtonFrame,command=self.Update_Data,text="UPDATE",font=("arial",13,"bold"),width=14,bg="beige",fg="black")
        btnUpdateData.grid(row=0,column=1)
        
        btnDeleteData=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",13,"bold"),width=14,bg="beige",fg="black")
        btnDeleteData.grid(row=0,column=2)
        
        btnRestData=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",13,"bold"),width=14,bg="beige",fg="black")
        btnRestData.grid(row=0,column=3)
        
        btnExitData=Button(ButtonFrame,text="EXIT",font=("arial",13,"bold"),width=14,bg="beige",fg="black", command=self.close_application)
        btnExitData.grid(row=0,column=4)
        
        #search
        lblSearch=Label(ButtonFrame,font=("arial",12,"bold"),text="Search By",padx=3,bg="beige",fg="black")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        
        #variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",13,"bold","italic"),state="readonly")
        search_combo["values"]=("Ref_no","MedName","Lot_no")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        
        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=5,relief=RIDGE,width=12,font=("arial",12,"bold"),bg="white",fg="black")
        txtSearch.grid(row=0,column=7)
        
        searchBtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=15,bg="beige",fg="black")
        searchBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("arial",13,"bold"),width=16,bg="beige",fg="black")
        showAll.grid(row=0,column=9)
        
        #label and entry
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2, pady=6,fg="white",bg="black")
        lblrefno.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()
        
        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",13,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        
        comName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name :",padx=2, fg="white", bg="black")
        comName.grid(row=1,column=0,sticky=W)
        comName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        comName.grid(row=1,column=1)
        
        comtypeofMed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine",padx=2,pady=6,fg="white",bg="black")
        comtypeofMed.grid(row=2,column=0,sticky=W)
        
        comtypeofMed=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27,font=("arial",12,"bold"),state="readonly")
        comtypeofMed["values"]=("Tablet","Liquid","capsules","Topical Medicines","Drops","Inhales","Injection")
        comtypeofMed.current(0)
        comtypeofMed.grid(row=2,column=1)
        
        #add medicine
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6,fg="white",bg="black")
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()
        
        lblMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27,font=("arial",12,"bold"),state="readonly")
        lblMedicineName["values"]=med
        lblMedicineName.current(0)
        lblMedicineName.grid(row=3,column=1)
        
        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No.:",padx=2,pady=6,fg="white",bg="black")
        lblLotNo.grid(row=4,column=0,sticky=W)
        lblLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblLotNo.grid(row=4,column=1)
        
        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6,fg="white",bg="black")
        lblIssueDate.grid(row=5,column=0,sticky=W)
        lblIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblIssueDate.grid(row=5,column=1)
        
        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6,fg="white",bg="black")
        lblExpDate.grid(row=6,column=0,sticky=W)
        lblExpDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblExpDate.grid(row=6,column=1)
        
        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6,fg="white",bg="black")
        lblUses.grid(row=7,column=0,sticky=W)
        lblUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblUses.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6,fg="white",bg="black")
        lblSideEffect.grid(row=8,column=0,sticky=W)
        lblSideEffect=Entry(DataFrameLeft,textvariable=self.sideeffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblSideEffect.grid(row=8,column=1)
        
        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec & Warning",padx=15,pady=6,fg="white",bg="black")
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        lblPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblPrecWarning.grid(row=0,column=3)
        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6,fg="white",bg="black")
        lblDosage.grid(row=1,column=2,sticky=W)
        lblDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblDosage.grid(row=1,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price:",padx=15,pady=6,fg="white",bg="black")
        lblPrice.grid(row=2,column=2,sticky=W)
        lblPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblPrice.grid(row=2,column=3)
        
        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6,fg="white",bg="black")
        lblProductQt.grid(row=3,column=2,sticky=W)
        lblProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        lblProductQt.grid(row=3,column=3)
        
        #Images
        lblhome=Label(DataFrameLeft,font=("arial",15,"bold"),text="Health is Wealth+",bg="black",fg="red",padx=1,pady=5)
        lblhome.place(x=570,y=280)
        img2=Image.open("E:\Pharmancy Management System\Apothecary\img1.jpg")
        img2=img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=500,y=300)
        
        img3=Image.open("E:\Pharmancy Management System\Apothecary\img.jpg")
        img3=img3.resize((150,135),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=790,y=300)
        
        img4=Image.open("E:\Pharmancy Management System\Apothecary\img2.jpg")
        img4=img4.resize((150,135),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=650,y=300)
        
        #dataframeright
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Adding Medicine Department",fg="black",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=520,height=350)
        
        img5=Image.open("E:\Pharmancy Management System\Apothecary\img3.jpg")
        img5=img5.resize((250,135),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=975,y=160)
        
        img6=Image.open("E:\Pharmancy Management System\Apothecary\img5.jpg")
        img6=img6.resize((250,135),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1220,y=160)
        
        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No.:")
        lblrefno.place(x=0,y=135)
        lblrefno=Entry(DataFrameRight,textvariable=self.refmed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        lblrefno.place(x=135,y=135)
        
        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",pady=6)
        lblmedName.place(x=0,y=155)
        lblmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        lblmedName.place(x=135,y=156)
        
        #sideframe
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=187,width=290,height=130)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medicine"),xscrollcommand=sc_x.set , yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medicine",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medicine",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        
        
        #medicine add button
        down_frame=Frame(DataFrameRight,bd=5,relief=RIDGE,bg="teal")
        down_frame.place(x=315,y=150,width=143,height=150)
        
        btnAddMed=Button(down_frame,text="ADD",font=("arial",12,"bold"),bg="beige",fg="black",width=12,pady=2, command=self.AddMed)
        btnAddMed.grid(row=0,column=0)
        
        btnUpdateMed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",12,"bold"),bg="beige",fg="black",width=12,pady=2)
        btnUpdateMed.grid(row=1,column=0)
        
        btnDeleteMed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),bg="beige",fg="red",width=12,pady=2)
        btnDeleteMed.grid(row=2,column=0)
        
        btnClearMed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),bg="beige",fg="black",width=12,pady=2)
        btnClearMed.grid(row=3,column=0)
        
        #frame details
        Framedetails=Frame(self.root,bd=15,relief=RIDGE,bg="beige")
        Framedetails.place(x=0,y=580,width=1530,height=200)
        
        #maintable & scrollbar
        TableFrame=Frame(self.root,bd=15,relief=RIDGE,bg="beige")
        TableFrame.place(x=12,y=591,width=1506,height=180)
        
        scroll_x=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(TableFrame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.apothecary_table=ttk.Treeview(TableFrame,column=("ref","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffects","warning","dosage","price","productQT"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.apothecary_table.xview)
        scroll_y.config(command=self.apothecary_table.yview)
        
        self.apothecary_table["show"]="headings"
        self.apothecary_table.heading("ref",text="Reference No.")
        self.apothecary_table.heading("companyname",text="Company Name")
        self.apothecary_table.heading("type",text="Type of Medicine")
        self.apothecary_table.heading("tabletname",text="Tablet Name")
        self.apothecary_table.heading("lotno",text="LOT NO.")
        self.apothecary_table.heading("issuedate",text="Issue Date")
        self.apothecary_table.heading("expdate",text="Exp Date")
        self.apothecary_table.heading("uses",text="Uses")
        self.apothecary_table.heading("sideeffects",text="Side Effects")
        self.apothecary_table.heading("warning",text="Warning")
        self.apothecary_table.heading("dosage",text="Dosage")
        self.apothecary_table.heading("price",text="Price")
        self.apothecary_table.heading("productQT",text="Product QT")
        
        self.apothecary_table.pack(fill=BOTH,expand=1)
        self.apothecary_table.column("ref",width=100)
        self.apothecary_table.column("companyname",width=100)
        self.apothecary_table.column("type",width=100)
        self.apothecary_table.column("tabletname",width=100)
        self.apothecary_table.column("lotno",width=100)
        self.apothecary_table.column("issuedate",width=100)
        self.apothecary_table.column("expdate",width=100)
        self.apothecary_table.column("uses",width=100)
        self.apothecary_table.column("sideeffects",width=100)
        self.apothecary_table.column("warning",width=100)
        self.apothecary_table.column("dosage",width=100)
        self.apothecary_table.column("price",width=100)
        self.apothecary_table.column("productQT",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.apothecary_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        #add medicine functionality declaration
        
    def AddMed(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(self.refmed_var.get(),self.addmed_var.get()))       
            
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Medicine Added")
        except:
           messagebox.showwarning("Invalid Data","Data entered is invalid.\nPlease check.")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()  
    #getcursor
    def Medget_cursor(self,ev=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        r=list(content["values"])
        
        #r=content["values"]
        self.refmed_var.set(r[0])
        self.addmed_var.set(r[1]) 
        
    def UpdateMed(self):
        if self.refmed_var.get()==" " or self.addmed_var.get()==" ":
            messagebox.showerror("Error","All fields are required!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(self.addmed_var.get(), self.refmed_var.get(),))         
        
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            
            
            messagebox.showinfo("Success","Medicine has been updated!")
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        
        sql="delete from pharma where Ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_dataMed()
        conn.close()
    
    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")    
    
    #main_table data
    
    def addmeddata(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required!")
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into meddata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.ref_var.get(),
                                                                    self.cmpName_var.get(),
                                                                    self.typeMed_var.get(),
                                                                    self.medName_var.get(),
                                                                    self.lot_var.get(),
                                                                    self.issuedate_var.get(),
                                                                    self.expdate_var.get(),
                                                                    self.uses_var.get(),
                                                                    self.sideeffect_var.get(),
                                                                    self.warning_var.get(),
                                                                    self.dosage_var.get(),
                                                                    self.price_var.get(),
                                                                    self.product_var.get(),
                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Data has been added!")   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from meddata")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.apothecary_table.delete(*self.apothecary_table.get_children())
            for i in row:
                self.apothecary_table.insert("",END,values=i)
            conn.commit()
        conn.close()         
    
    def get_cursor(self,ev=""): 
        cursor_row=self.apothecary_table.focus()
        content=self.apothecary_table.item(cursor_row)
        row=content["values"]
        
        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.product_var.set(row[12])     
    
    def Update_Data(self):
        if self.ref_var.get()==" " or self.lot_var.get()==" ":
            messagebox.showerror("Error","All fields are required!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("update meddata set CompName=%s,Type_Med=%s,MedName=%s,LotNo=%s,IssueDate=%s,ExpDate=%s,Uses=%s,SideEffects=%s,Warning=%s,Dosage=%s,Price=%s,Product=%s where Ref_no=%s",(
                                                                    
                                                                    self.cmpName_var.get(),
                                                                    self.typeMed_var.get(),
                                                                    self.medName_var.get(),
                                                                    self.lot_var.get(),
                                                                    self.issuedate_var.get(),
                                                                    self.expdate_var.get(),
                                                                    self.uses_var.get(),
                                                                    self.sideeffect_var.get(),
                                                                    self.warning_var.get(),
                                                                    self.dosage_var.get(),
                                                                    self.price_var.get(),
                                                                    self.product_var.get(),
                                                                    self.ref_var.get()
                                                                    ))         
        
            conn.commit()
            self.fetch_data()
            conn.close()            
            messagebox.showinfo("UPDATE","Record has been updated successfully!")
    
    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        
        sql="delete from meddata where Ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_data()
        conn.close() 
        messagebox.showinfo("Delete","Information has been deleted successfully!")
    
    def reset(self):
        #self.ref_var.set("")
        self.cmpName_var.set("")
        #self.typeMed_var.set("")
        #self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.product_var.set("")   
    
    def search_data(self,eve=""):
        conn=mysql.connector.connect(host="localhost",username="root",password="13112001",database="pharmacy")
        my_cursor=conn.cursor()
        search_query="SELECT * from meddata where " +str(self.search_var.get()) +" LIKE "+ "'%"+ str(self.searchTxt_var.get()) +"%"+"'"
        my_cursor.execute(search_query)

        rows=my_cursor.fetchall()
        print(rows)
        if len(rows)>0:
            self.apothecary_table.delete(*self.apothecary_table.get_children())
            for i in rows:
                self.apothecary_table.insert("",END,values=i)
            conn.commit()   
            conn.close()
        else:
            messagebox.showwarning("Data not exist!","Enter the valid data or record with this data do not exist.")
        
            
    def close_application(self):
        self.root.quit()
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=ApothecaryManagementSystem(root)
    root.mainloop()        
