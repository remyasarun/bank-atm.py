from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import mysql.connector

window = Tk()
window.title("ATM BANK")
window.geometry("600x500")



# =======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
AADHAR = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
DEPOSIT = StringVar()
WITHDRAWAL = StringVar()
BALANCE = StringVar()
balance = StringVar()
NET_BALANCE = StringVar()




# =======================================METHODS=======================================


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        window.destroy()
        exit()
def Database():
    global conn, cursor

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase")

    cursor = conn.cursor()

def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(window)
    LoginFrame.pack(side=TOP, pady=60)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)


def RegisterForm():
    global RegisterFrame,lbl_result2
    RegisterFrame = Frame(window)
    RegisterFrame.pack(side=TOP, pady=10)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 15), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 15), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 15), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 15), bd=18)
    lbl_lastname.grid(row=4)
    lbl_aadhar = Label(RegisterFrame, text="Aadhar number:", font=('arial', 15), bd=30)
    lbl_aadhar.grid(row=5)
    lbl_age = Label(RegisterFrame, text="Age:", font=('arial', 15), bd=18)
    lbl_age.grid(row=6)
    lbl_address = Label(RegisterFrame, text="address:", font=('arial', 15), bd=18)
    lbl_address.grid(row=7)
    lbl_deposit = Label(RegisterFrame, text="Deposit amount:", font=('arial', 15), bd=18)
    lbl_deposit.grid(row=8)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 10))
    lbl_result2.grid(row=9, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 15), textvariable=USERNAME, width=10)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 15), textvariable=PASSWORD, width=10, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 15), textvariable=FIRSTNAME, width=10)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 15), textvariable=LASTNAME, width=10)
    lastname.grid(row=4, column=1)
    aadhar = Entry(RegisterFrame, font=('arial', 15), textvariable=AADHAR, width=10)
    aadhar.grid(row=5, column=1)
    age = Entry(RegisterFrame, font=('arial', 15), textvariable=AGE, width=10)
    age.grid(row=6, column=1)
    address = Entry(RegisterFrame, font=('arial', 15), textvariable=ADDRESS, width=10)
    address.grid(row=7, column=1)
    deposit = Entry(RegisterFrame, font=('arial', 15), textvariable=DEPOSIT, width=10)
    deposit.grid(row=8, column=1)

    btn_login = Button(RegisterFrame, text="Register", font=('arial', 15), width=10, command=Register)
    btn_login.grid(row=11, columnspan=2, pady=5)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)

def toggletoselect(event=None):
    LoginFrame.destroy()
    selectionform()

def selectionform():
    global SelectionFrame
    SelectionFrame = Frame(window)
    SelectionFrame.pack(side=TOP, pady=40)
    lbl_select=Label(SelectionFrame, text="select one option", font=('arial', 15), bd=18)
    lbl_select.grid(row=1, column=1)
    btn_deposit = Button(SelectionFrame, text="Deposit", font=('arial', 15), width=10, command=Deposit1)
    btn_deposit.grid(row=3, column=1, pady=5)
    btn_withdrawal = Button(SelectionFrame, text="Withdrawal", font=('arial', 15), width=10,command=withdraw1)
    btn_withdrawal.grid(row=4, column=1, pady=5)
    btn_balance1 = Button(SelectionFrame, text="Balance", font=('arial', 15), width=10, command=avail_Balance3)
    btn_balance1.grid(row=5, column=1, pady=5)
    btn_exit = Button(SelectionFrame, text="Exit", font=('arial', 15), width=10, command=exit)
    btn_exit.grid(row=6, column=1, pady=5)


def toggletodeposit(event=None):
    SelectionFrame.destroy()
    depositform()

def depositform():
    global DepositFrame,deposit_amount, balance, lbl_deposit11,e_deposit
    DepositFrame = Frame(window)
    DepositFrame.pack(side=TOP, pady=40)
    lbl_deposit1 = Label(DepositFrame, text="enter the amount",  font=('arial', 15), bd=18)
    lbl_deposit1.grid(row=1)
    e_deposit = Entry(DepositFrame, textvariable=DEPOSIT)
    e_deposit.grid(row=2)
    lbl_deposit11 = Label(DepositFrame, text="", font=('arial', 18))
    lbl_deposit11.grid(row=3)
    btn_deposit11 = Button(DepositFrame, text="Deposit", font=('arial', 15), width=10, command=Deposit)
    btn_deposit11.grid(row=4, pady=5)
    btn_balance1 = Button(DepositFrame, text="Balance", font=('arial', 15), width=10, command=avail_Balance)
    btn_balance1.grid(row=5, pady=5)
    btn_exit11 = Button(DepositFrame, text="Exit", font=('arial', 15), width=10, command=exit)
    btn_exit11.grid(row=6, pady=5)
    lbl_d2 = Label(DepositFrame, text="Back", fg="Blue", font=('arial', 12))
    lbl_d2.grid(row=0, sticky=W)
    lbl_d2.bind('<Button-1>', ToggleToBack1)

def Balanceform():
    global BalanceFrame,lbl_balance1
    BalanceFrame = Frame(window)
    BalanceFrame.pack(side=TOP, pady=10)
    lbl_balance1=Label(BalanceFrame,text=" Available Balance is", fg="black")
    lbl_balance1.grid(row=1, column=1,sticky="W")
    lbl_balance2=Label(BalanceFrame,textvariable=NET_BALANCE, fg="black")
    lbl_balance2.grid(row=1, column=2, sticky="W")
    NET_BALANCE.set(current_balance())
    btn_deposit33 = Button(BalanceFrame, text="Deposit", font=('arial', 15), width=10, command=toggletobal_to_deposit)
    btn_deposit33.grid(row=4, column=1, pady=5)
    btn_withdraw33 = Button(BalanceFrame, text="Withdraw", font=('arial', 15), width=10, command=toggletobal_to_withdraw)
    btn_withdraw33.grid(row=5, column=1, pady=5)
    btn_exit33 = Button(BalanceFrame, text="Exit", font=('arial', 15), width=10, command=exit)
    btn_exit33.grid(row=6,column=1, pady=5)

def ToggleToBalance1():
    DepositFrame.destroy()
    Balanceform()
def ToggleToBalance2():
    WithdrawalFrame.destroy() 
    Balanceform()
def ToggleToBalance3():
    SelectionFrame.destroy()
    Balanceform()
def toggletobal_to_deposit():
    BalanceFrame.destroy()
    depositform()

def toggletobal_to_withdraw():
    BalanceFrame.destroy()
    Withdrawalform()
def avail_Balance():
    ToggleToBalance1()
def avail_Balance2():
    ToggleToBalance2()
def avail_Balance3():
    ToggleToBalance3()

def ToggleTowithdraw():
    SelectionFrame.destroy()
    Withdrawalform()

def Withdrawalform():
    global WithdrawalFrame, lbl_withdrawal11, e_withdrawal
    WithdrawalFrame = Frame(window)
    WithdrawalFrame.pack(side=TOP, pady=40)
    lbl_withdrawal1 = Label(WithdrawalFrame, text="enter the amount", font=('arial', 15), bd=18)
    lbl_withdrawal1.grid(row=1)
    e_withdrawal = Entry(WithdrawalFrame, textvariable=WITHDRAWAL)
    e_withdrawal.grid(row=2)
    lbl_withdrawal11 = Label(WithdrawalFrame, text="", font=('arial', 18))
    lbl_withdrawal11.grid(row=3)
    btn_withdrawal11 = Button(WithdrawalFrame, text="Withdraw", font=('arial', 15), width=10, command=Withdrawal)
    btn_withdrawal11.grid(row=4, pady=5)
    btn_balance12 = Button(WithdrawalFrame, text="Balance", font=('arial', 15), width=10, command=avail_Balance2)
    btn_balance12.grid(row=6, pady=5)
    btn_exit12 = Button(WithdrawalFrame, text="Exit", font=('arial', 15), width=10, command=exit)
    btn_exit12.grid(row=7, pady=5)
    lbl_w2 = Label(WithdrawalFrame, text="Back", fg="Blue" , font=('arial', 12))
    lbl_w2.grid(row=0, sticky=W)
    lbl_w2.bind('<Button-1>', ToggleToBack2)


def ToggleToBack1(event=None):
    DepositFrame.destroy()
    selectionform()

def ToggleToBack2(event=None):
    WithdrawalFrame.destroy()
    selectionform()

def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

def exit():
   window.destroy()


def Register():
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "" or AADHAR.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or DEPOSIT.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM bank_atm WHERE username = %s", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO bank_atm(username, password, firstname, lastname, aadhar, age, address, deposit) VALUES(%s, %s, %s, %s, %s, %s,%s, %s )",
                           (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get()), str(AADHAR.get()), str(AGE.get()), str(ADDRESS.get()), str(DEPOSIT.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            AADHAR.set("")
            AGE.set("")
            ADDRESS.set("")
            DEPOSIT.set("")
            WITHDRAWAL.set("")
            BALANCE.set("")

            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()


def  Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM bank_atm WHERE username = %s and password = %s",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            toggletoselect()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")

def Deposit1():
    toggletodeposit()

def Deposit():
    Database()
    global balance, deposit_amt, balance1
    balance1 = current_balance()
    deposit_amt = int(DEPOSIT.get())
    balance = int(deposit_amt) + balance1
    cursor.execute("update bank_atm set deposit=%s,balance=%s where username=%s", (int(DEPOSIT.get()), balance, str(USERNAME.get())))
    conn.commit()
    lbl_deposit11.config(text="Successfully Deposited!", fg="black")
    e_deposit.delete(0, END)
    cursor.close()
    conn.close()

def  withdraw1():
    ToggleTowithdraw()

def current_balance():
    Database()
    global original_balance
    cursor.execute("SELECT balance from bank_atm where username=%s", (USERNAME.get(),))
    res = cursor.fetchone()
    for original_balance in res:
        print(original_balance)
    return original_balance

def Withdrawal():
    Database()
    global pre_balance, e_withdrawal, balance

    pre_balance = current_balance()
    amt = int(WITHDRAWAL.get())
    if balance >= amt:
        balance = pre_balance - amt
        cursor.execute("update bank_atm set withdrawel=%s, balance=%s where username=%s",
                       (str(WITHDRAWAL.get()), balance, str(USERNAME.get())))
        conn.commit()

        lbl_withdrawal11.config(text="withdrawal is successful!", fg="black")
    else:
        balance = pre_balance + 0
        cursor.execute("update bank_atm set withdrawel=%s, balance=%s where username=%s",
                       (str(WITHDRAWAL.get()), balance, str(USERNAME.get())))
        lbl_withdrawal11.config(text="Insufficient balance ", fg="black")
    e_withdrawal.delete(0, END)
    cursor.close()
    conn.close()
    return balance


LoginForm()

# ========================================MENUBAR WIDGETS==================================
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="file", menu=filemenu)
window.config(menu=menubar)

# ========================================INITIALIZATION===================================

window.mainloop()