
import sys
import tkMessageBox
import sqlite3

import quest_usamah_abdur_rehman_123560_C
import os
q=quest_usamah_abdur_rehman_123560_C.question()






#exceptions for tkinter spelling
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


class Log_In:

  #this function close the window
    def closeWindow(self):
        msg=tkMessageBox.askyesno("Log In","Are you Sure you want to Quit?")
        if(msg):
            quit()

    #constructor function, Main Login window
    def __init__(self, top=None):
        self.dbNAme="database"

        #Creating Database
        conn = sqlite3.connect(self.dbNAme)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS question(id integer primary key autoincrement,qid INTEGER,qName TEXT,qDesc TEXT,qtext TEXT,qtype TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS answer (aid INTEGER PRIMARY KEY AUTOINCREMENT ,Qid INTEGER,c1 text,c2 text,c3 text,c4 text,correctAnswer integer,tfAnswer integer,singleAnswer text,answer text)")
        c.execute("CREATE TABLE IF NOT EXISTS entity (uid INTEGER PRIMARY KEY AUTOINCREMENT,uName TEXT,uPassword TEXT,role INTEGER)")


        self.top=top       #storing my window in another variable because late i have to destroy it in order to hide it

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family {DejaVu Sans} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("648x316+641+179")      #window size
        top.title("Log In")                   #window Title
        top.configure(background="#006b31")    #background colour
        self.std = IntVar()                     #These two variable are initialize to store the state of checkbuttons
        self.tchr = IntVar()

         #user name

        self.userName = Entry(top)
        self.userName.place(relx=0.32, rely=0.13, relheight=0.06, relwidth=0.27)
        self.userName.configure(background="white")
        self.userName.configure(font="TkFixedFont")
        self.userName.configure(width=176)

        #user password

        self.userPassword = Entry(top,show="*")
        self.userPassword.place(relx=0.32, rely=0.38, relheight=0.06
                , relwidth=0.29)
        self.userPassword.configure(background="white")
        self.userPassword.configure(font="TkFixedFont")
        self.userPassword.configure(width=186)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.11, rely=0.13, height=28, width=96)
        self.Label1.configure(activebackground="#00600e")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(background="#006b31")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#fbebff")
        self.Label1.configure(highlightcolor="#000021")
        self.Label1.configure(text='''User Name''')
        self.Label1.configure(width=96)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.12, rely=0.35, height=28, width=76)
        self.Label2.configure(background="#006b31")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#fbebff")
        self.Label2.configure(text='''Password''')
        self.Label2.configure(width=76)

        #Check buttons for student and teacher

        self.roleStd = Checkbutton(top, text="Student", onvalue=1, offvalue=0, variable=self.std,)
        self.roleTchr = Checkbutton(top, text="Teacher", onvalue=1, offvalue=0, variable=self.tchr)
        self.roleTchr.place(relx=0.45, rely=0.51, relheight=0.06, relwidth=0.11)
        self.roleStd.place(relx=0.31, rely=0.51, relheight=0.06, relwidth=0.11)

        # Log in button

        self.btnlogin = Button(top,command=self.CheckLogin)
        self.btnlogin.place(relx=0.32, rely=0.7, height=26, width=97)
        self.btnlogin.configure(activebackground="#d9d9d9")
        self.btnlogin.configure(text='''Login''')
        self.btnlogin.configure(width=97)

        # Signup button


        self.btnSignup = Button(top,command=self.Signup)
        self.btnSignup.place(relx=0.51, rely=0.7, height=26, width=97)
        self.btnSignup.configure(activebackground="#d9d9d9")
        self.btnSignup.configure(text='''SignUp''')
        self.btnSignup.configure(width=97)

        # Quit Button

        self.btnClose = Button(top, command=self.closeWindow)
        self.btnClose.place(relx=0.70, rely=0.7, height=26, width=97)
        self.btnClose.configure(activebackground="#d9d9d9")
        self.btnClose.configure(text='''Close''')
        self.btnClose.configure(width=97)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    #this function checks credentials when use logg in
    def CheckLogin(self):

        username=self.userName.get()    #get the value of username entry field
        upas=self.userPassword.get()    #get the value of password entry field
        whtRole=0
        if self.std.get():    # checking which check button is checked if student button is check then store the enitiy as srudent and vice versa
         whtRole=2
        elif self.tchr.get():
            whtRole=1


        with sqlite3.connect("database") as conn: #sqlite3 connection
            cursor = conn.cursor()
            resut=cursor.execute("select *from entity where uName=? and upassword=? and role=?",(username,upas,whtRole))
            found=cursor.fetchone()
            #print found[2]
            conn.commit()

        if found:                 #if user found in database
            self.top.destroy()

            if whtRole==1:          #if user is teacher

                q.title() #calling title function from quiz.py

            elif whtRole==2:     #if user is student
                print "student"
                q.showAns()

        else:    #if credentials are wrong it will prompt the error message

            tkMessageBox._show("Wrong Credentials","User Name or Password is Incorrect")
















# this is signup function , if the user is new he will signup

    #Sign up function
    def Signup(self):

        self.top.destroy()  #destroy the previous main screen/window

        self.topA=Tk()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans Mono} -size 11 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans} -size 10 -weight bold -slant " \
                 "italic -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Serif} -size 10 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"

        self.topA.geometry("483x296+567+137")
        self.topA.title("New Toplevel 1")
        self.topA.configure(background="#006b31")
        self.is_checkedtchr = IntVar()
        self.is_checkedstd = IntVar()

        self.Label1 = Label(self.topA)
        self.Label1.place(relx=0.06, rely=0.27, height=28, width=176)
        self.Label1.configure(background="#006b31")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''New Username:''')
        self.Label1.configure(width=176)

        self.menubar = Menu(self.topA, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.topA.configure(menu=self.menubar)

        self.Label2 = Label(self.topA)
        self.Label2.place(relx=0.06, rely=0.07, height=28, width=319)
        self.Label2.configure(background="#006b31")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Please Enter New Credentials''')
        self.Label2.configure(width=319)

        self.Label3 = Label(self.topA)
        self.Label3.place(relx=0.04, rely=0.41, height=28, width=176)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(background="#006b31")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''New Password:''')

#user name

        self.nameE = Entry(self.topA)
        self.nameE.place(relx=0.5, rely=0.27, relheight=0.07, relwidth=0.3)
        self.nameE.configure(background="white")
        self.nameE.configure(font="TkFixedFont")
#password
        self.pwordE = Entry(self.topA)
        self.pwordE.place(relx=0.5, rely=0.41, relheight=0.07, relwidth=0.3)
        self.pwordE.configure(background="white")
        self.pwordE.configure(font="TkFixedFont")
        self.pwordE.configure(selectbackground="#c4c4c4")
#checkbutton for student or teacher
        self.std = Checkbutton(self.topA, text="Student", onvalue=1, offvalue=0, variable=self.is_checkedstd)
        self.tchr = Checkbutton(self.topA, text="Teacher", onvalue=1, offvalue=0, variable=self.is_checkedtchr)
        self.std.place(relx=0.5, rely=0.54, relwidth=0.14, relheight=0.0, height=18)
        self.tchr.place(relx=0.68, rely=0.54, relwidth=0.14, relheight=0.0, height=18)
#signup button
        self.signupBtn = Button(self.topA,command=self.doneSignup)
        self.signupBtn.place(relx=0.58, rely=0.68, height=36, width=77)
        self.signupBtn.configure(activebackground="#d9d9d9")
        self.signupBtn.configure(background="#000000")
        self.signupBtn.configure(font=font12)
        self.signupBtn.configure(foreground="#ffffff")
        self.signupBtn.configure(text='''Signup''')
        self.signupBtn.configure(width=77)
#close button
        self.btnClose = Button(self.topA,command=self.closeWindow)
        self.btnClose.place(relx=0.79, rely=0.68, height=36, width=77)
        self.btnClose.configure(activebackground="#d9d9d9")
        self.btnClose.configure(background="#000006")
        self.btnClose.configure(font=font12)
        self.btnClose.configure(foreground="#ffffff")
        self.btnClose.configure(text='''Quit''')
        self.btnClose.configure(width=77)
        self.topA.mainloop()


 #this function take the data information and sign him up by saving his credentials

    #this function store sigup data
    def doneSignup(self):
        global role                #declaring it as globle to acess it latest value from any function
        if self.is_checkedtchr.get():
            role=1  #role1 means he is teacher
        if self.is_checkedstd.get():  #role2 means student
            role=2

        parameters=self.nameE.get(),self.pwordE.get(),role     #storing credentials in database
        querry="insert into entity(uName,uPassword,role) values(?,?,?)"
        self.run_querry(querry,parameters)
        self.topA.destroy()  # This will destroy the signup window. :)
        os.system("python login_usamah_abdur_rehman_123560_C.py") #calling again the log in file

    # this function runs my querry for database
    def run_querry(self,querry,parameters):
        with sqlite3.connect(self.dbNAme) as conn:
            cursor=conn.cursor()
            result=cursor.execute(querry,parameters)
            conn.commit()
        return result


if __name__ == '__main__':
    global val, w, root
    root = Tk()
    top = Log_In (root)
    # login_support.init(root, top)
    root.mainloop()



