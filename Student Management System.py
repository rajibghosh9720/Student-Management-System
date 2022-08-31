from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
import sqlite3
try:
    db=sqlite3.connect('Student Management System.db')
    cr=db.cursor()
    cr.execute("create table Student(Name, Registration, Roll, Gender, DOB, Contact, Email, Address)")
    db.commit()
except:
    print("Table is ready !!!")
    

class student:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Management System')
        self.root.geometry('1520x800+0+0')
        self.root.configure(background='#D3D3D3')
        
        
        title=Label(self.root, text="Student Management System",bd=10, font=('Colonna MT',50, 'bold'),bg='#40E0D0',fg='#2F4F4F')
        title.pack(side=TOP,fill=BOTH)
        
        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE,bg='#8FBC8F')
        Manage_Frame.place(x=10,y=100,width=1510,height=700)
#=====================================================================
        
        Registerbtn=Button(text='Register New Student',bg='#87CEFA',fg='Black',font=('Rockwell Condensed', 20, 'bold'),command=lambda :RegisterNewStudent())
        Registerbtn.place(x=200,y=400,width=500,height=50)
        
        Displaybtn=Button(text='Display Student Information',bg='#87CEFA',fg='Black',font=('Rockwell Condensed', 20, 'bold'),command=lambda :DisplayStudentInformation())
        Displaybtn.place(x=800,y=400,width=500,height=50)
        
#=====================================================================
        En=Label(text='Student Information Form',font=('Forte', 40, 'underline'),fg='#2F4F4F',bg='#8FBC8F')
        En.place(x=470,y=200)
#=====================================================================
def RegisterNewStudent():
    root.destroy()
    w=Tk()
    
    x=StringVar()
    y=StringVar()
    z=StringVar()
    m=StringVar()
    n=StringVar()
    o=StringVar()
    p=StringVar()
    
    
    w.title("Register New Student")
    w.geometry('1520x800+0+0')
    w.configure(background='#87CEEB')
#=====================================================================    
                
    def insert():
        cr.execute("insert into Student(Name, Registration, Roll, Gender, DOB , Contact, Email, Address) values(?,?,?,?,?,?,?,?)",(text_name.get(),text_registration.get(),text_roll.get(),combo_gender.get(),text_dob.get(),text_Contact.get(),text_email.get(),text_Address.get('1.0',END)))
        db.commit()
        messagebox.showinfo("Success", "Student Data Saved Successfully.....")
        
        
    def update():
        cr.execute("update Student set Registration=?, Roll=?, Gender=?, DOB=?, Contact=?, Email=?, Address=? where Name=?",(text_registration.get(),text_roll.get(),combo_gender.get(),text_dob.get(),text_Contact.get(),text_email.get(),text_Address.get('1.0',END),text_name.get()))
        db.commit()
        messagebox.showinfo("Success", "Student Update Successfully.....")
        
        
    def delete():
        cr.execute("delete from Student where Name=?",(text_name.get(),))
        db.commit()
        messagebox.showinfo("Success", "Student Delete Successfully.....")
        
    def Reset():
        x.set("")
        y.set("")
        z.set("")
        m.set("")
        n.set("")
        o.set("")
        p.set("")
        text_Address.delete('1.0',END)
        messagebox.showinfo("Success", "Reset Successfully.....")
    
#=====================================================================
    
    L1= tk.Label(w, text="Register New Student", font=('Colonna MT', 50, 'bold'),relief=GROOVE,bg="#00CED1",fg="#2F4F4F", width=80)
    L1.pack()
#=====================================================================
    Manage_Frame=Frame(w, bd=4, relief=RIDGE,bg='#66CDAA')
    Manage_Frame.place(x=10,y=100,width=1520,height=700)
#=====================================================================
    
    m_title=Label(Manage_Frame, text='Manage Students',bg='#66CDAA',fg='#2F4F4F',font=('Edwardian Script ITC', 50, 'bold','underline'))
    m_title.place(x=550,y=20)
       
    lbl_name=Label(Manage_Frame, text='Name',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_name.place(x=3,y=150)
       
    text_name=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=5, relief=GROOVE, textvar=x)
    text_name.place(x=100,y=150,width=350,height=45)
       
    lbl_registration=Label(Manage_Frame, text='Registration No.',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_registration.place(x=470,y=150)
       
    text_registration=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=5, relief=GROOVE ,textvar=y)
    text_registration.place(x=680,y=150,width=350,height=45)
       
    lbl_roll=Label(Manage_Frame, text='Roll No. ',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_roll.place(x=1040,y=150)
       
    text_roll=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=5, relief=GROOVE ,textvar=z)
    text_roll.place(x=1150,y=150,width=350,height=45)
    
    lbl_Gender=Label(Manage_Frame, text='Gender ',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_Gender.place(x=3,y=250)
       
    combo_gender=ttk.Combobox(Manage_Frame, font=('times new roman', 20, 'bold'),state='readonly',textvar=m)
    combo_gender['values']=('Male','Femal','Others')
    combo_gender.place(x=100,y=250,width=350,height=45)
    
    lbl_dob=Label(Manage_Frame, text='D.O.B ',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_dob.place(x=470,y=250)
       
    text_dob=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=5, relief=GROOVE,textvar=n)
    text_dob.place(x=680,y=250,width=350,height=45)
       
    lbl_Contact=Label(Manage_Frame, text='Contact ',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_Contact.place(x=1040,y=250)
       
    text_Contact=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=5, relief=GROOVE,textvar=o)
    text_Contact.place(x=1150,y=250,width=350,height=45)
       
    lbl_email=Label(Manage_Frame, text='Email ',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_email.place(x=3,y=350)
       
    text_email=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=5, relief=GROOVE,textvar=p)
    text_email.place(x=100,y=350,width=350,height=45)
    
       
    lbl_Address=Label(Manage_Frame, text='Address ',bg='#66CDAA',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_Address.place(x=480,y=350)
       
    text_Address=Text(Manage_Frame,width=30, height=4, font=('',15),relief=GROOVE)
    text_Address.place(x=680,y=350,width=350,height=100)
    
#============================BUTTON==================================
    btn_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE,bg='#29AB87')
    btn_Frame.place(x=15,y=500,width=1480,height=80)
#=====================================================================
    Addbtn=Button(btn_Frame,text='Submit',font=('Lucida Calligraphy', 8, 'bold'),bg='#ADD8E6',width=30,height=2,command=insert)
    Addbtn.place(x=5,y=15)
       
    updatebtn=Button(btn_Frame,text='Update',font=('Lucida Calligraphy', 8, 'bold'),bg='#ADD8E6',width=30,height=2,command=update)
    updatebtn.place(x=395,y=15)
       
    deletebtn=Button(btn_Frame,text='Delete',font=('Lucida Calligraphy', 8, 'bold'),bg='#ADD8E6',width=30,height=2,command=delete)
    deletebtn.place(x=800,y=15)
       
    Resetbtn=Button(btn_Frame,text='Reset',font=('Lucida Calligraphy',8, 'bold'),bg='#ADD8E6',width=30,height=2,command=Reset)
    Resetbtn.place(x=1185,y=15)
    
#=====================================================================
    
    backbtn=Button(Manage_Frame,text='Display Student Information',font=('times new roman',10, 'bold'),bg='#2E8B57',fg='white',width=30,height=2,command=lambda :DisplayStudentInformation())
    backbtn.place(x=15,y=620)
    
    exitbtn=Button(Manage_Frame,text='Exit Page',font=('times new roman',10, 'bold'),bg='#2E8B57',fg='white',width=30,height=2,command=w.destroy)
    exitbtn.place(x=1273,y=620)    
    
#=====================================================================
def DisplayStudentInformation():
    m=Tk()
    
    e=StringVar()
    f=StringVar()
    
    
    
    m.title("Display Student Information")
    m.geometry('1520x800+0+0')
    m.configure(background='#01796F')
#===================================================================== 
    
    def get_cursor():
        cursor_row=Student_table.focus()
        contents=Student_table.item(cursor_row)
        row=contents['values']
        
    
#    print(row)
        x.set(row[0])
        y.set(row[1])
        z.set(row[2])
        m.set(row[3])
        n.set(row[4])
        o.set(row[5])
        p.set(row[6])
        text_Address.delete('1.0',END)
        text_Address.insert(END,row[7])
    
    def search_data():
        cr.execute("select * from Student where "+str(combo_search.get())+" LIKE '%"+str(text_Search.get())+"%'")
        rows=cr.fetchall()
        if len(rows)!=0:
            Student_table.delete(*Student_table.get_children())
            for row in rows:
                Student_table.insert('', END, values= row)
                db.commit() 
                
                
    def fetch_data():
        cr.execute("select * from Student")
        data=cr.fetchall()
        if len(data)!=0:
            Student_table.delete(*Student_table.get_children())
            for i in data:
                Student_table.insert('', END, values= i)
                db.commit()   
#=====================================================================   
    L1= tk.Label(m, text="Display Student Information",relief=GROOVE,bg="#00CED1",fg="#556B2F", width=80)
    L1.config(font=("Colonna MT", 50, 'bold','underline'))
    L1.pack()
#=====================================================================
    Display_Frame=Frame(m, bd=4, relief=RIDGE,bg='#5F9EA0')
    Display_Frame.place(x=15,y=90,width=1500,height=650)
#=====================================================================
    exitbtn=Button(m,text='Exit Page',font=('times new roman',10, 'bold'),bg='#2E8B57',fg='white',width=30,height=2,command=m.destroy)
    exitbtn.place(x=1295,y=750)
    
#=====================================================================
      
    lbl_search=Label(Display_Frame, text='Search By',bg='#5F9EA0',fg='white',font=('times new roman', 20, 'bold'))
    lbl_search.grid(row=0, column=0, pady=10,padx=20, sticky="w")
       
       
    combo_search=ttk.Combobox(Display_Frame, width=10, font=('times new roman',14, 'bold'),state='readonly', textvar=e)
    combo_search['values']=('Name','Registration','Roll','Contact')
    combo_search.grid(row=0, column=1, pady=10,padx=20, sticky="w")
       
       
    text_Search=Entry(Display_Frame,width=20, font=('times new roman', 14, 'bold'),bd=5, relief=GROOVE, textvar=f)
    text_Search.grid(row=0, column=2, pady=10,padx=20, sticky="w")
       
    searchbtn=Button(Display_Frame,text='Search', font=('times new roman', 10, 'bold'),width=10,pady=10,bg='#1C2951',fg='white',command=lambda :search_data())
    searchbtn.grid(row=0,column=3,padx=10,pady=10)
       
    showallbtn=Button(Display_Frame,text='Show All', font=('times new roman', 10, 'bold'),width=10,pady=10,bg='#1C2951',fg='white',command=lambda :fetch_data())
    showallbtn.grid(row=0,column=4,padx=10,pady=10)    
    
    Table_Frame=Frame(Display_Frame, bd=4, relief=RIDGE,bg='#01796F')
    Table_Frame.place(x=5,y=70,width=1480,height=550)
    
    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
       
    Student_table=ttk.Treeview(Table_Frame, columns=("name","registration","roll","gender","dob","contact","email", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
       
    scroll_x.config(command =Student_table.xview)
    scroll_y.config(command =Student_table.yview)
    
    Student_table.heading("name", text="Name")
    Student_table.heading("registration", text="Registration No.")
    Student_table.heading("roll", text="Roll No.")
    Student_table.heading("gender", text="Gender")
    Student_table.heading("dob", text="D.O.B")
    Student_table.heading("contact", text="Contact")
    Student_table.heading("email", text="Email")
    Student_table.heading("Address", text="Address")
       
    Student_table['show']='headings'
    
    Student_table.column('name',width=100)
    Student_table.column('registration',width=100)
    Student_table.column('roll',width=100)
    Student_table.column('gender',width=100)
    Student_table.column('dob',width=100)
    Student_table.column('contact',width=100)
    Student_table.column('email',width=150)
    Student_table.column('Address',width=460)
    Student_table.pack(fill=BOTH,expand=1)
    
     
        
root=Tk()
ob=student(root)
root.mainloop()
