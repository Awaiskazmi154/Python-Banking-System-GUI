
# importing the tkinter module for GUI implementation
import tkinter as tk

# importing the PIL modules for Image
from PIL import Image, ImageTk

# importing customer_account class
from customer_account import CustomerAccount

# importing admin class
from admin import Admin

# initial customers accounts
customers_accounts_list = []

# initial admin accounts
admins_accounts_list = []

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = '#b9faf8'
        self.background='#7D26CD'
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self['background'] = self.defaultBackground

    def on_enter(self, e):
        self['background'] = self.background
        self['foreground']= 'white'
        self['cursor']= "hand2"

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground']= 'black'

class AppFrame(tk.Frame):
    def __init__(self, master, **kw):
        tk.Frame.__init__(self,master=master,**kw)
        self['background'] = '#e6fae6'


# Bank Class inheriting TK class
class BankSystem(tk.Tk):
    
    # class initialization
    def __init__(self):
        
        # method to inherit functionality
        super().__init__()
        
        # Frames for GUI
        self.frame1 = AppFrame(self) 
        self.frame2 = AppFrame(self) 
        self.frame3 = AppFrame(self)
        self.frame4 = AppFrame(self) 
        self.frame5 =  AppFrame(self)
        self.frame6 = AppFrame(self)
        self.frame7 =  AppFrame(self)
        self.frame8 =  AppFrame(self)
        self.frame9 =  AppFrame(self)
        self.frame10 = AppFrame(self) 
        self.frame11 = AppFrame(self)
        self.frame12 =  AppFrame(self)
        self.frame13 =  AppFrame(self)
        self.frame14 =  AppFrame(self)
        self.frame15 =  AppFrame(self)
        self.frame16 =  AppFrame(self)
        self.frame17 =  AppFrame(self)
        self.frame18 =  AppFrame(self)
        self.frame19 =  AppFrame(self)
        self.frame20 =  AppFrame(self)
        self.frame21 =  AppFrame(self)
        self.frame22 =  AppFrame(self)
        self.frame23 =  AppFrame(self)
        self.frame24 =  AppFrame(self)
        self.frame25 =  AppFrame(self)
        
        # initial customers accounts
        self.customers_accounts_list = []
        
        # initial admin accounts
        self.admins_accounts_list = []
        
        # loading the bank's accounts data
        self.load_bank_data()
    
    # function for loading the bank data   
    def load_bank_data(self):
        
        # loading bank customers_accounts
        self.load_customers()

        # create admin 1 (all admin rights)
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        

        # create admin 2
        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        
        # add admin objects to admims_list
        self.admins_accounts_list.append(admin_1)
        self.admins_accounts_list.append(admin_2)
    
    # function for loading the bank customers_accounts
    def load_customers(self):
       
        # reading customers accounts data file
        customer_acc_file = open('customer_accounts.txt', 'r')
        
        # reading lines from the file
        Lines = customer_acc_file.readlines()
        
        # looping all the lines
        for line in Lines:
            
            # number of words per line
            word_count = 0
            
            # loop for every word separated by comma , in the given line
            for word in line.split(','): 
                
                # for the 1st word (first name) in the line
                if word_count == 0:
                    fname = word
                
                # for the 2nd word (second name) in the line
                elif word_count == 1:
                    lname = word
                
                # for the 3rd - 7th words (address) in the line
                elif word_count == 2:
                    addr = []
                    addr.append(word)
                elif word_count == 3:
                    addr.append(word)
                elif word_count == 4:
                    addr.append(word)
                elif word_count == 5:
                    addr.append(word)
                elif word_count == 6:
                    address = addr
                    account_no = word
                
                # for the 8th word (account balance) in the line
                elif word_count == 7:
                    balance = word
                
                # for the 9th word (account type) in the line
                elif word_count == 8:
                    account_type = word
                
                # for the 10th word (account name) in the line
                elif word_count == 9:
                    account_name = word
                
                # for the 11th word (interest rate) in the line 
                elif word_count == 10:
                    interest_rate = word
                
                # for the 12th word (overdraft limit) in the line
                elif word_count == 11:
                    overdraft_limit = word
                
                # incrementing the word number count over the same line
                word_count += 1
            
            # creating a customer object from the collected line data
            customer = CustomerAccount(fname, lname, address, account_no, balance)
            
            # customer account_type provided in the file (if any)
            customer.account_type = account_type
            
            # customer account_name provided in the file (if any)
            customer.account_name = account_name
            
            # customer interest_rate provided in the file (if any)
            customer.interest_rate = interest_rate
            
            # customer overdraft_limit provided in the file (if any)
            customer.overdraft_limit = overdraft_limit
            
            # add customer object to customers_accounts_list
            self.customers_accounts_list.append(customer)
            
            # close the customers account file
            customer_acc_file.close()
    
    # function for running of main menu options  
    def run_main_options(self):
        
        # display labels for the new frame
        label1 = tk.Label(self.frame1, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        label2 = tk.Label(self.frame1, text="Welcome to the Python Bank System")
        label3 = tk.Label(self.frame1, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        label4 = tk.Label(self.frame1)
        label5 = tk.Label(self.frame1, text="Choose your option")
        label6 = tk.Label(self.frame1)
        
        # display label for the bank image
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.frame1, image=render)
        img.image = render
        
        
        # display buttons for the new frame
        button1 = HoverButton(self.frame1, text="1) Admin login" , command=lambda: self.main_menu('1'))
        button2 = HoverButton(self.frame1, text="2) Quit Python Bank System", command=lambda: self.main_menu('2'))
        
        # positioning frame contents appropriately using grid system
        label1.grid(row=1, column=1, columnspan=2,padx=20)
        label2.grid(row=2, column=1,columnspan=2,padx=20)
        label3.grid(row=3, column=1,columnspan=2,padx=20)
        
        button1.grid(row=4, column=1,padx=40,pady=10,sticky = 'W')
        button2.grid(row=5, column=1,padx=40,pady=10,sticky = 'W')
        
        label4.grid(row=6)
        label5.grid(row=7, column=1,padx=40,sticky = 'W')
        label6.grid(row=8)
        img.grid(row=9,column=1,columnspan=2,padx=20)
        
        # display frame on the screen
        self.frame1.pack()
    
    # function for the main menu of the bank application
    def main_menu(self, choice):
        
        # if user's choice is '1' for admin login
        if choice == '1':
           
            # remove previous frame from the display
            self.frame1.forget()
            
            # display labels for the new frame
            label1 = tk.Label(self.frame2, text="Please input admin username: ")
            label2 = tk.Label(self.frame2, text="Please input admin password: ")
            
            
            # display label for the bank image
            load = Image.open("logo.png")
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.frame2, image=render)
            img.image = render
            
            # display input fields of username and password for the new frame
            e1 = tk.Entry(self.frame2, bg='#f0f0fc', width=30)
            e2 = tk.Entry(self.frame2,bg='#f0f0fc',show="*", width=30)
            
            # display buttons for the new frame
            button = HoverButton(self.frame2, text="LogIn!", command= lambda: self.admin_login(e1.get(), e2.get()))
            back_button = HoverButton(self.frame2, text="Back", command= lambda: back_to_frame1(self.frame2))
            
            # positioning frame contents appropriately using grid system
            label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
            label2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
            e1.grid(row=1, column=3,padx=10)
            e2.grid(row=2, column=3,padx=10)
            back_button.grid(row=3,padx=25, column=1,sticky = 'W')
            button.grid(row=3, column=3,padx=15,pady=10,sticky = 'E')
            img.grid(row=5,column=1,columnspan=1,padx=20)
            
            # display the frame on the screen
            self.frame2.pack()
            
            # back button function to move to the previous frame
            def back_to_frame1(frame):
                frame.forget()
                self.frame1.pack()
        
        # if user's choice is '2' to Exit     
        elif choice == '2':
        
            # show the messages to user
            msg = "Thank-You for stopping by the bank!"
            tk.messagebox.showinfo( "Main Menu", msg)
            self.destroy()
            
        # if user enters any wrong choice 
        else:
        
            # show the messages to user
            msg = "Choose a correct option!"
            tk.messagebox.showinfo( "Main Menu", msg)
   
    # function for the admin login
    def admin_login(self, username, password):
        
        #STEP A.1
        # search the admin in the admins_accounts_list with entered username 
        found_admin = self.search_admins_by_name(username)
        
        # if the admin found 
        if found_admin != None:
            
            # if the found admin password matches the entered user's password
            if found_admin.get_password() == password:
                
                # show the messages to user
                msg = "\n Login successful"
                tk.messagebox.showinfo( "Admin Login", msg)
                
                # remove the current admin login frame
                self.frame2.forget()
                
                # display admin menu with options
                self.admin_menu(found_admin)
            
            # if the found admin password doesn't match the entered password
            else:
                
                # set found admin to None
                found_admin = None
                
                # show the messages to user
                msg = "\n Login failed! Incorrect Password"
                tk.messagebox.showinfo( "Admin Login", msg)
        
        # if the admin is not found in the list
        else:
           
            # set found admin to None
            found_admin = None
            
            # show the messages to user
            msg = "\n Login failed! "
            tk.messagebox.showinfo( "Admin Login", msg)
    
    # function to display admin options menu
    def admin_menu(self, admin_obj):
        
        # display labels for the new frame
        label1 = tk.Label(self.frame3, text="Welcome Admin %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
        label2 = tk.Label(self.frame3, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        label3 = tk.Label(self.frame3, text=" ")
        label4 = tk.Label(self.frame3, text="Choose your option")
        
        # display buttons for the new frame
        button3 = HoverButton(self.frame3, text="1) Transfer money",  command=lambda: self.run_admin_options('1', admin_obj))
        button4 = HoverButton(self.frame3, text="2) Customer account operations & profile settings" , command=lambda: self.run_admin_options('2', admin_obj))
        button5 = HoverButton(self.frame3, text="3) Delete customer", command=lambda: self.run_admin_options('3', admin_obj))
        button6 = HoverButton(self.frame3, text="4) Print all customers detail", command=lambda: self.run_admin_options('4', admin_obj))
        button7 = HoverButton(self.frame3, text="5) Update admin own information", command=lambda: self.run_admin_options('5', admin_obj))
        button8 = HoverButton(self.frame3, text="6) Create a new customer account", command=lambda: self.run_admin_options('6', admin_obj))
        button9 = HoverButton(self.frame3, text="7) Request a management report", command=lambda: self.run_admin_options('7', admin_obj))
        
        back_button = HoverButton(self.frame3,  bg='#b9faf8', text="Sign Out", command= lambda: back_to_frame2(self.frame3))
        
        # positioning the frame using grid system
        label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
        label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
        label3.grid(row=11, column=1)
        label4.grid(row=12, column=1,padx=40,pady=10,sticky = 'W')
        button3.grid(row=3, column=1,padx=40,pady=5,sticky = 'W')
        button4.grid(row=4, column=1,padx=40,pady=5,sticky = 'W')
        button5.grid(row=5, column=1,padx=40,pady=5,sticky = 'W')
        button6.grid(row=6, column=1,padx=40,pady=5,sticky = 'W')
        button7.grid(row=7, column=1,padx=40,pady=5,sticky = 'W')
        button8.grid(row=8, column=1,padx=40,pady=5,sticky = 'W')
        button9.grid(row=9, column=1,padx=40,pady=5,sticky = 'W')
        back_button.grid(row=15, column=2,padx=15,pady=10,sticky = 'E')
        
        # display the frame on screen
        self.frame3.pack()
        
        # back button to move to the previous frame
        def back_to_frame2(frame):
                frame.forget()
                self.frame2.pack()
    
    # function for searching admins by username in the admins_accounts_list       
    def search_admins_by_name(self, admin_username):
        
        #STEP A.2
        # initially setting found_admin
        found_admin = None
        
        # for every admin object in the admins_accounts_list
        for admin in self.admins_accounts_list:
            
            # admin username
            username = admin.get_username()
            
            # if username of admin matches with enetered name
            if username == admin_username:
                
                # found admin equals current admin object in the list
                found_admin = admin
                
                # break the loop
                break
        
        # if username of admin in the list gets doesn't match with enetered username
        if found_admin == None:
            
            # show the messages to user 
            msg = "The Admin %s does not exist! Try again...\n" %admin_username
            tk.messagebox.showinfo( "Admin", msg)
            
        # return the admin object 
        return found_admin 
    
    # function for searching the customers by last name in the customers_accounts_list     
    def search_customers_by_name(self, customer_lname):
        
        #STEP A.3
        # initially setting found_customer
        found_customer = None
        
        # for every customer account object in the customers_accounts_list
        for customer in self.customers_accounts_list:
            
            # customer last name
            customer_name = customer.get_last_name()
            
            # if last name of customer matches with enetered last name
            if customer_name == customer_lname:
                
                # found admin equals current admin object in the list
                found_customer = customer
                
                # break the loop
                break
        
        # if last name of customer doesn't match with enetered last name
        if found_customer == None:
           
            # show the messages to user
            msg = "The Customer %s does not exist! Try again...\n" %customer_lname
            tk.messagebox.showinfo( "Customer", msg)
             
        # return the customer object 
        return found_customer
        
    # function for transfering money between accounts
    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        
        #ToDo
        # method to search for sender's account in the customers_accounts_list
        sender_account = self.search_customers_by_name(sender_lname)
        
        # method to search for receivers's account in the customers_accounts_list
        receiver_account = self.search_customers_by_name(receiver_lname)
        
        # if sender and rceiver accounts exist
        if (sender_account != None) & (receiver_account != None):
            
            # if receiver's account number gets match with entered account number
            if receiver_account.account_no == receiver_account_no:
                
                # for valid transfer amount
                try:
                    
                    # if senders account balance is more than the transfer amount
                    if sender_account.balance >= float(amount):
                        
                        # removing accounts from the list for new updates
                        self.customers_accounts_list.remove(sender_account)
                        self.customers_accounts_list.remove(receiver_account)
                        
                        # deducting sender's balance and inrease same amount for receiver as a zero sum  
                        sender_account.balance -= float(amount)
                        receiver_account.balance += float(amount)
                        
                        # add new updated accounts to the list for consistency
                        self.customers_accounts_list.append(sender_account)
                        self.customers_accounts_list.append(receiver_account)
                        
                        # opening file having customers accounts data for reading
                        newfile =  open('customer_accounts.txt', "r")
                        
                        # reading lines from the file
                        lines = newfile.readlines()
                        
                        # closing file object
                        newfile.close()
                        
                        # opening file having customers accounts data for writing the new balances after transaction
                        newfile = open('customer_accounts.txt', "w")
                        
                        # loop for every line in the file
                        for line in lines:
                        
                            # word number count in the line
                            word_count = 0
                            
                            # loop for every word separated by , in the specified line
                            for word in line.split(','): 
                                
                                # if the word is second (i.e last name of customer)
                                if word_count == 1:
                            
                                    # if the word is niether last name of sender nor receiver
                                    if (word != sender_lname) &  (word != receiver_lname):
                                    
                                        # write the line as it is
                                        newfile.write(line)
                                   
                                    # if the word is last name of sender
                                    elif word == sender_lname:
                                    
                                        # write the line for the sender new data
                                        newfile.write("\n"+sender_account.fname+","+sender_account.lname+","+sender_account.address[0]+","+sender_account.address[1]+","+sender_account.address[2]+","+sender_account.address[3]+","+str(sender_account.account_no)+","+str(sender_account.balance)+","+sender_account.account_type+","+sender_account.account_name+","+str(sender_account.interest_rate)+","+str(sender_account.overdraft_limit))
                                    
                                    # if the word is last name of receiver
                                    elif word == receiver_lname:
                                    
                                        # write the line for the receiver new data
                                        newfile.write("\n"+receiver_account.fname+","+receiver_account.lname+","+receiver_account.address[0]+","+receiver_account.address[1]+","+receiver_account.address[2]+","+receiver_account.address[3]+","+str(receiver_account.account_no)+","+str(receiver_account.balance)+","+receiver_account.account_type+","+receiver_account.account_name+","+str(receiver_account.interest_rate)+","+str(receiver_account.overdraft_limit))
                                    
                                    # break the loop
                                    break
                                
                                # incrementing the word number count corrresponding to next iteration of the loop over the same line
                                word_count+=1
                        
                        # closing the file object after writing the data into it
                        newfile.close()
                        
                        # showing the messages to user
                        msg = "Money Successfully transfered!"
                        tk.messagebox.showinfo( "Money Transfer", msg)
                        
                    # if senders acoount balance is less than the transfer amount
                    else:
                        
                        # show the messages to user
                        msg = "Account balance is low than transfer amount\nMoney transfer Failed!!"
                        tk.messagebox.showinfo( "Money Transfer", msg)
                        
                # if user inputs invalid transfer amount
                except:
                    
                    # show the messages to user
                    msg = "Invalid Balance Amount"
                    tk.messagebox.showinfo( "Money Transfer", msg)
            
            # if receiver's account number doesn't match with entered account number
            else:
                
                # showing the messages to user
                msg = "Reciever account no. is incorrect\n Money transfer Failed!"
                tk.messagebox.showinfo( "Money Transfer", msg)    
                
        # if one or both the accounts does't exist in the list
        else:
            
            # show the messages to user
             msg = "Money transfer Failed!"
             tk.messagebox.showinfo( "Money Transfer", msg)
   
    # function for chosen option from admin options menu
    def run_admin_options(self, opt, admin_obj):                                
        
        # using a choice variable for entered option
        choice = opt
        
        # if choice entered is '1' for transfer money
        if choice == '1':
            
            # remove current frame from the display
            self.frame3.forget()
            
            # setting text labels for the new frame to display
            label1 = tk.Label(self.frame4, text="Please input sender surname: ")
            label2 = tk.Label(self.frame4, text="Please input the amount to be transferred: ")
            label3 = tk.Label(self.frame4, text="Please input receiver surname: ")
            label4 = tk.Label(self.frame4, text="Please input receiver account number: ")
            
            # setting buttons for the new frame to display
            button = HoverButton(self.frame4, text="Transfer!", command=lambda: self.transferMoney(e1.get(), e3.get(), e4.get(), e2.get()))
            back_button = HoverButton(self.frame4, text="Back", command= lambda: back_to_frame3(self.frame4))
            
            # setting input fields for the new frame to display
            e1 = tk.Entry(self.frame4,bg='#f0f0fc', width=50)
            e2 = tk.Entry(self.frame4, bg='#f0f0fc', width=50)
            e3 = tk.Entry(self.frame4, bg='#f0f0fc', width=50)
            e4 = tk.Entry(self.frame4, bg='#f0f0fc', width=50)
            
            # positioning frame contents appropriately using grid system
            label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
            label2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
            label3.grid(row=3, column=1,padx=20,pady=10,sticky = 'W')
            label4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')   
            e1.grid(row=1, column=3,padx=10)
            e2.grid(row=2, column=3,padx=10)
            e3.grid(row=3, column=3,padx=10)
            e4.grid(row=4, column=3,padx=10)          
            button.grid(row=5, column=3,padx=15,pady=10,sticky = 'E') 
            back_button.grid(row=5, column=1,padx=25,sticky = 'W')
            
            # packing the frame to display on screen
            self.frame4.pack()
            
            # back button function for previous frame
            def back_to_frame3(frame):
                frame.forget()
                self.frame3.pack()
            
        # if choice entered is '2' for customer account options
        elif choice == '2':
           
            # remove current frame from the display
            self.frame3.forget()
            
            # method to run customer options menu
            def run(customer_name):
               
                # setting custoomer_account variable to searched account from customers_accounts_list
                customer_account = self.search_customers_by_name(customer_name)
                
                # if customer account found
                if customer_account != None:
                
                    # method to withdraw amount from the customer account     
                    def withdraw(customer_account, amount):
                        
                        #ToDo
                        # setting the new balance after wihdrawl to 'new_balance' variable 
                        new_balance = customer_account.balance-amount
                        
                        # if the account overdraft limit is not empty
                        if customer_account.overdraft_limit != "":
                        
                            # if the overdraft limit is not exceeded
                            if (new_balance >= 0) | (abs(new_balance) < float(customer_account.overdraft_limit)):
                            
                                # setting the customer balance according to the withdrawl amount 
                                customer_account.balance-=amount
                                
                                # showing the required message on the message box to user
                                msg = "Amount Withdrawn \nNew Balance is "+ str(customer_account.balance)
                                tk.messagebox.showinfo( "Withdraw Amount", msg)
                                
                                # opening file having customers accounts data for reading
                                newfile =  open('customer_accounts.txt', "r")
                                
                                # reading lines from the file and storing to 'Lines'
                                lines = newfile.readlines()
                                
                                # closing file object
                                newfile.close()
                                
                                # opening file having customers accounts data for updation of new balances after transaction
                                newfile = open('customer_accounts.txt', "w")
                                
                                # loop for every line in the file
                                for line in lines:
                                
                                    # word number count in the line
                                    count = 0
                                    
                                    # loop for every word separated by , in the specified line
                                    for word in line.split(','): 
                                        
                                        # if the word is first (i.e first name of customer)
                                        if count == 0:
                                    
                                            # if the word is not the first name of customer to be updated
                                            if (word != customer_account.fname):
                                            
                                                # write the line as it is
                                                newfile.write(line)
                                            
                                            # if the word is the first name of customer to be updated   
                                            else:
                                            
                                                # write the line for the customer new data (new balance after withdrawl)
                                                newfile.write("\n"+customer_account.fname+","+customer_account.lname+","+customer_account.address[0]+","+customer_account.address[1]+","+customer_account.address[2]+","+customer_account.address[3]+","+str(customer_account.account_no)+","+str(customer_account.balance)+","+customer_account.account_type+","+customer_account.account_name+","+str(customer_account.interest_rate)+","+str(customer_account.overdraft_limit))
                                        
                                        # incrementing the word number count corrresponding to next iteration of the loop over the same line    
                                        count+=1
                                
                                # closing the file object after writing the data into it       
                                newfile.close()
                            
                            # if the overdraft limit exceeds (i.e. negative balance threshold reached)
                            else:
                            
                            # showing the required message on the message box to user
                               msg = "Overdraft limit exceeded! Withdrawl Failed"
                               tk.messagebox.showinfo( "Withraw Amount", msg) 
                        
                        # if the account overdraft limit is empty
                        else:
                        
                            # for default accounts overdraft limit is zero 
                            if (float(new_balance) >= 0):
                            
                                # setting the customer balance according to the withdrawl amount 
                                customer_account.balance-=amount
                                
                                # showing the required message on the message box to user
                                msg = "Amount Withdrawn \nNew Balance is "+ str(customer_account.balance)
                                tk.messagebox.showinfo( "Withdraw Amount", msg)
                                
                                # opening file having customers accounts data for reading
                                newfile =  open('customer_accounts.txt', "r")
                                
                                # reading lines from the file and storing to 'Lines'
                                lines = newfile.readlines()
                                
                                # closing file object
                                newfile.close()
                                
                                # opening file having customers accounts data for updation of new balances after transaction
                                newfile = open('customer_accounts.txt', "w")
                                
                                # loop for every line in the file
                                for line in lines:
                                
                                    # word number count in the line
                                    count = 0
                                    
                                    # loop for every word separated by , in the specified line
                                    for word in line.split(','): 
                                    
                                        # if the word is first (i.e first name of customer)
                                        if count == 0:
                                        
                                            # if the word is not the first name of customer to be updated
                                            if (word != customer_account.fname):
                                            
                                                # write the line as it is
                                                newfile.write(line)
                                            
                                            # if the word is the first name of customer to be updated
                                            else:
                                            
                                                # write the line for the customer new data (new balance after withdrawl)
                                                newfile.write("\n"+customer_account.fname+","+customer_account.lname+","+customer_account.address[0]+","+customer_account.address[1]+","+customer_account.address[2]+","+customer_account.address[3]+","+str(customer_account.account_no)+","+str(customer_account.balance)+","+customer_account.account_type+","+customer_account.account_name+","+str(customer_account.interest_rate)+","+str(customer_account.overdraft_limit))
                                     
                                        # incrementing the word number count corrresponding to next iteration of the loop over the same line    
                                        count+=1
                                
                                # closing the file object after writing the data into it         
                                newfile.close()
                            
                            # if the overdraft limit exceeds (i.e. negative balance threshold reached)
                            else:
                            
                                # showing the required message on the message box to user
                               msg = "Overdraft limit exceeded! Withdrawl Failed"
                               tk.messagebox.showinfo( "Withraw Amount", msg) 
                    
                    # function to print balance amount of the customer account
                    def print_balance(customer_account):
                        print("\n The account balance is %.2f" %customer_account.balance)
                        
                    # getter method for the balance amount of the customer account
                    def get_balance(customer_account):
                        return customer_account.balance
                    
                    # getter method for the account type of the customer account
                    def get_account_type(customer_account):
                        return customer_account.account_type
                    
                    # getter method for the account name of the customer account
                    def get_account_name(customer_account):
                        return customer_account.account_name
                    
                    # getter method for the interest rate of the customer account
                    def get_interest_rate(customer_account):
                        return customer_account.interest_rate
                    
                    # getter method for the overdraft limit of the customer account
                    def get_overdraft_limit(customer_account):
                        return customer_account.overdraft_limit
                    
                    # method for the running of menu options of the customer account 
                    def run_account_options(customer_account):
                        
                        # remove current frame from the display
                        self.frame5.forget()
                        
                        # setting text labels for the new frame to display
                        myLabel1 = tk.Label(self.frame21, text="Your Transaction Options Are:")
                        myLabel2 = tk.Label(self.frame21, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        button3 = HoverButton(self.frame21, text="1) Deposit money", command=lambda: account_menu(customer_account,'1'))
                        button4 = HoverButton(self.frame21, text="2) Withdraw money", command=lambda: account_menu(customer_account,'2'))
                        button5 = HoverButton(self.frame21, text="3) Check balance", command=lambda: account_menu(customer_account,'3'))
                        button6 = HoverButton(self.frame21, text="4) Update customer name", command=lambda: account_menu(customer_account,'4'))
                        button7 = HoverButton(self.frame21, text="5) Update customer address", command=lambda: account_menu(customer_account,'5'))
                        button8 = HoverButton(self.frame21, text="6) Show customer details", command=lambda: account_menu(customer_account, '6'))
                        myLabel10 = tk.Label(self.frame21)
                        myLabel11 = tk.Label(self.frame21, text="Choose your option")
                      
                        # setting button for the new frame to display
                        back_button = HoverButton(self.frame21, text="Back", command=lambda: account_menu(customer_account, '7'))
                        
                        # positioning frame contents appropriately using grid system
                        myLabel1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                        myLabel2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                        button3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                        button4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                        button5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                        button6.grid(row=6, column=1,padx=20,pady=5,sticky = 'W')
                        button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                        button8.grid(row=8, column=1,padx=20,pady=5,sticky = 'W')
                        myLabel10.grid(row=10, column=1)
                        myLabel11.grid(row=11, column=1,padx=20,pady=10,sticky = 'W')
                        back_button.grid(row=15, column=1,padx=20,pady=10,sticky = 'E')
                        
                        # packing the frame to display on screen
                        self.frame21.pack()    
                     
                    # function to show details of the customer account
                    def print_details(customer_account):
                        
                        # showing the customer details on the message box to user
                        msg = "First name: %s" %customer_account.fname +"\nLast name: %s" %customer_account.lname+"\nAccount No: %s" %customer_account.account_no+"\nAddress: %s" %customer_account.address[0]+"\n         %s" %customer_account.address[1]+"\n         %s" %customer_account.address[2]+"\n         %s" %customer_account.address[3]+"\n "
                        tk.messagebox.showinfo( "Customer Details", msg)
                        
                    # function for the selection of account menu options of the customer account
                    def account_menu(customer_account, opt):
                        
                        # setting option selected by user to the 'choice' variable
                        choice = opt
                        
                        # if choice entered is '1' to deposit money
                        if choice == '1':
                        
                            # remove current frame from the display
                            self.frame21.forget()
                            
                            # setting text label for the new frame to display
                            myLabel1 = tk.Label(self.frame22, text="Please enter amount to be deposited: ")
                            
                            # setting buttons for the new frame to display
                            button = HoverButton(self.frame22, text="Deposit!", command=lambda: try_deposit(customer_account, e.get()))
                            back_button = HoverButton(self.frame22, text="Back", command= lambda: back_to_frame1(self.frame22))
                            
                            # setting input field for the new frame to display
                            e = tk.Entry(self.frame22, bg='#f0f0fc', width=30)
                            
                            # positioning frame contents appropriately using grid system
                            myLabel1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')  
                            e.grid(row=1, column=3,padx=10)
                            button.grid(row=2, column=3, padx=15,pady=10,sticky = 'E')           
                            back_button.grid(row=2, column=1, padx=25,sticky = 'W')
                            
                            # packing the frame to display on screen
                            self.frame22.pack()
                            
                            # back button function for previous frame
                            def back_to_frame1(frame):
                               frame.forget()
                               self.frame21.pack()
                            
                            # function for entered deposit option
                            def try_deposit(customer_account, amount):
                            
                                # try the following code if the amount entered is valid
                                try:
                                
                                    # setting deposit amount to 'amount' to get a float value from string
                                    amount=float(amount)
                                    
                                    # calling the deposit money method
                                    customer_account.deposit(amount)
                                    
                                    # calling the print balance method
                                    print_balance(customer_account)
                                    
                                    # showing the required message on the message box to user
                                    msg = "Amount Deposited \nNew Balance is "+ str(customer_account.balance)
                                    tk.messagebox.showinfo( "Deposit Amount", msg)
                                
                                # if the amount entered is invalid
                                except:
                                
                                    # showing the required message on the message box to user
                                    msg = "Enter a valid amount!"
                                    tk.messagebox.showinfo( "Deposit Amount", msg)
                                    print ("\n Enter a valid amount!")
                                    
                         # if choice entered is '2' to withdraw money       
                        elif choice == '2':
                            
                            # remove current frame from the display
                            self.frame21.forget()
                            
                            # setting text label for the new frame to display
                            myLabel1 = tk.Label(self.frame23, text="Please enter amount to be withdrawn: ")
                            
                            # setting buttons for the new frame to display
                            button = HoverButton(self.frame23, text="Withdraw!", command=lambda: try_withdraw(e.get()))
                            back_button = HoverButton(self.frame23, text="Back", command= lambda: back_to_frame1(self.frame23))
                            
                            # setting input field for the new frame to display
                            e = tk.Entry(self.frame23, bg='#f0f0fc', width=30)
                            
                            # positioning frame contents appropriately using grid system
                            myLabel1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                            e.grid(row=1, column=3,padx=10)
                            button.grid(row=2, column=3, padx=15,pady=10,sticky = 'E')
                            back_button.grid(row=2, column=1, padx=25,sticky = 'W')
                            
                            # packing the frame to display on screen
                            self.frame23.pack()
                            
                            # back button function for previous frame
                            def back_to_frame1(frame):
                               frame.forget()
                               self.frame21.pack()
                            
                            # function for entered withdraw option
                            def try_withdraw(amount):
                            
                                # try the following code if the amount entered is valid
                                try:
                                
                                    # setting deposit amount to 'amount' to get a float value from string
                                    amount=float(amount)
                                    
                                    # calling the withdraw money method
                                    withdraw(customer_account, amount)
                                    
                                    # calling the print balance method
                                    print_balance(customer_account)
                                 
                                # if the amount entered is invalid   
                                except:
                                    
                                    # showing the required message on the message box to user
                                    msg = "Enter a valid amount!"
                                    tk.messagebox.showinfo( "Withdraw Amount", msg)
                        
                        # if choice entered is '3' to check available balance     
                        elif choice == '3':
                        
                            # showing the required message on the message box to user
                            msg = "Balance is "+ str(customer_account.balance)
                            tk.messagebox.showinfo( "Available balance", msg)
                            
                            # calling the print balance method
                            #STEP A.4.4
                            customer_account.print_balance()
                        
                        # if choice entered is '4' to update customer name     
                        elif choice == '4':
                        
                            # remove current frame from the display
                            self.frame21.forget()
                            
                            # setting text labels for the new frame to display
                            myLabel1 = tk.Label(self.frame24, text="Enter new customer first name: ")
                            myLabel2 = tk.Label(self.frame24, text="Enter new customer last name: ")
                            # setting buttons for the new frame to display
                            button = HoverButton(self.frame24, text="Update Name!", command=lambda: try_update(e1.get(), e2.get()))
                            back_button = HoverButton(self.frame24, text="Back", command= lambda: back_to_frame1(self.frame24))
                            
                            # setting input fiels for the new frame to display
                            e1 = tk.Entry(self.frame24, bg='#f0f0fc', width=50)
                            e2 = tk.Entry(self.frame24, bg='#f0f0fc', width=50)
                            
                            # positioning frame contents appropriately using grid system
                            myLabel1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                            myLabel2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
                            e1.grid(row=1, column=3,padx=10)
                            e2.grid(row=2, column=3,padx=10) 
                            button.grid(row=3, column=3, padx=15,pady=10,sticky = 'E')
                            back_button.grid(row=3, column=1, padx=25,sticky = 'W')            
                            
                            # packing the frame to display on screen
                            self.frame24.pack()
                            
                            # back button function for previous frame
                            def back_to_frame1(frame):
                               frame.forget()
                               self.frame21.pack()
                            
                            # function for entered update name option
                            def try_update(fname, sname):
                            
                                # calling method for the first name updation
                                customer_account.update_first_name(fname)
                                
                                # calling method for the last name updation
                                customer_account.update_last_name(sname)
                                
                                # showing the required message on the message box to user
                                msg = "Names updated successfully! "
                                tk.messagebox.showinfo( "Names update", msg)
                                
                        # if choice entered is '5' to update customer address    
                        elif choice == '5':
                            
                            # remove current frame from the display
                            self.frame21.forget()
                            
                            # setting text labels for the new frame to display
                            myLabel1 = tk.Label(self.frame25, text="Enter new house number: ")
                            myLabel2 = tk.Label(self.frame25, text="Enter new street name: ")
                            myLabel3 = tk.Label(self.frame25, text="Enter new city name: ")
                            myLabel4 = tk.Label(self.frame25, text="Enter new post code: ")
                            
                            # setting buttons for the new frame to display
                            button = HoverButton(self.frame25, text="Update Address!", command=lambda: try_update_address(e1.get(), e2.get(),e3.get(),e4.get()))
                            back_button = HoverButton(self.frame25, text="Back", command= lambda: back_to_frame1(self.frame25))
                            
                            # setting input fiels for the new frame to display
                            e1 = tk.Entry(self.frame25, bg='#f0f0fc', width=50)
                            e2 = tk.Entry(self.frame25, bg='#f0f0fc', width=50)
                            e3 = tk.Entry(self.frame25, bg='#f0f0fc', width=50)
                            e4 = tk.Entry(self.frame25, bg='#f0f0fc', width=50)
                            
                            # positioning frame contents appropriately using grid system
                            myLabel1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                            myLabel2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
                            myLabel3.grid(row=3, column=1,padx=20,pady=10,sticky = 'W')
                            myLabel4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')   
                            e1.grid(row=1, column=3,padx=10)
                            e2.grid(row=2, column=3,padx=10)
                            e3.grid(row=3, column=3,padx=10)
                            e4.grid(row=4, column=3,padx=10)            
                            button.grid(row=5, column=3, padx=15,pady=10,sticky = 'E')
                            back_button.grid(row=5, column=1, padx=25,sticky = 'W')
                            
                            # packing the frame to display on screen
                            self.frame25.pack()
                            
                            # back button function for previous frame
                            def back_to_frame1(frame):
                               frame.forget()
                               self.frame21.pack()
                            
                            # function for entered update address option
                            def try_update_address(house_num, street_name, city_name, post_code):
                            
                                #ToDo
                                # creating an empty addr list
                                addr = []
                                
                                # appending entered house_num to the addr list
                                addr.append(house_num)
                                
                                # appending entered street_name to the addr list
                                addr.append(street_name)
                                
                                # appending entered city_name to the addr list
                                addr.append(city_name)
                                
                                # appending entered post_code to the addr list
                                addr.append(post_code)
                                
                                # calling update_address method by passing addr list
                                customer_account.update_address(addr)
                                
                                # showing the required message on the message box to user
                                msg = "Address updated successfully! "
                                tk.messagebox.showinfo( "Adress update", msg)
                                
                        # if choice entered is '6' to see customer details         
                        elif choice == '6':
                           
                            # calling print_details method to see details
                            print_details(customer_account)
                        
                        # if choice entered is '7' to go back 
                        elif choice == '7':
                            
                            # display previous frame
                            self.frame5.pack()
                        
                            # remove current frame from the display
                            self.frame21.forget()
                    
                    # calling method to run customer options
                    run_account_options(customer_account)
                    
            # setting text label for the new frame to display
            label1 = tk.Label(self.frame5, text="Please input customer surname ")
          
            # setting input field for the new frame to display
            e = tk.Entry(self.frame5, bg='#f0f0fc', width=50)
            
            # setting buttons for the new frame to display
            button = HoverButton(self.frame5, text="Enter!", command=lambda: run(e.get()))
            back_button = HoverButton(self.frame5, text="Back", command= lambda: back_to_frame3(self.frame5))
            
            # positioning frame contents appropriately using grid system
            label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
            e.grid(row=1, column=3,padx=10)
            button.grid(row=2, column=3,padx=15,pady=10,sticky = 'E')
            back_button.grid(row=2, column=1, padx=25,sticky = 'W')
            
            # packing the frame to display on screen
            self.frame5.pack() 
            
            # back button function for previous frame
            def back_to_frame3(frame):
               frame.forget()
               self.frame3.pack()
            
        # if choice entered is '3' to delete a customer account
        elif choice == '3':
            
            # checking if admin has rights for the process
            if admin_obj.has_full_admin_right():
            
                #STEP A.5
                # calling delete method
                self.delete_customer()
            
            # if admin has no rights for the process
            else:
            
                # showing the required message on the message box to user
                msg = "The Admin " +admin_obj.lname+ " has no rights to delete an account! "
                tk.messagebox.showinfo( "Delete Customer", msg)
                
        # if choice entered is '4' to print all customer's details
        elif choice == '4':
            
            #STEP A.6
            # calling customers details method
            self.print_all_accounts_details() 
        
        # if choice entered is '5' to update admin own information
        elif choice == '5':
        
            # calling admin update information method
            self.update_admin_info(admin_obj)
        
        # if choice entered is '6' to create a new customer account   
        elif choice == '6':
        
            # calling create new customer method
            self.create_customer_account()
        
        # if choice entered is '7' to request for a management report     
        elif choice == '7':
        
            # calling request management report method
            self.request_management_report()
         
        # if choice entered is '8' to request for Sign out 
        elif choice == '8':
           
            # remove current frame from display
            self.frame3.forget()
            
            # display previous login screen
            self.frame2.pack()
        
        # if choice entered is incorrect
        else:
        
            # showing the required message on the message box to user
            msg = "Choose a correct option!"
            tk.messagebox.showinfo( "Admin Menu", msg)
            
    # function for request management report
    def request_management_report(self):
        
        # counting the number of all customers accounts from the size customers_accounts_list
        total_customers = len(self.customers_accounts_list)
        
        # sum of all the money of customers in the bank
        sum_of_money_all_customers = 0
        for customer in self.customers_accounts_list:
            sum_of_money_all_customers += customer.balance
        
        # sum of total payable yearly interest rate of customers in the bank
        total_payable_interest_rate = 0
        
        for customer in self.customers_accounts_list:
            if customer.interest_rate != "":
                total_payable_interest_rate += float(customer.balance) * float(customer.interest_rate) * 100
        
        # sum of all the overdrafts taken by the customers in the bank
        total_amount_of_overdrafts_taken = 0
        for customer in self.customers_accounts_list:
            if customer.balance < 0:
                total_amount_of_overdrafts_taken += abs(customer.balance)
           
        # show the messages to user
        msg = "a) Total number of customers in the system : " + str(total_customers)+"\nb) The sum of all money the customers : "+ str(sum_of_money_all_customers)+"\nc) The sum of amount of interest rate payable to all accounts for one year: "+str("{:.2f}".format(total_payable_interest_rate))+"\nd) Total amount of overdrafts currently taken by all customers: "+str(total_amount_of_overdrafts_taken)
        tk.messagebox.showinfo( "Management Report", msg) 
        
    
    # function for the deletion of the customers
    def delete_customer(self):
    
        # remove display of current frame
        self.frame3.forget()
        
        # display the label for the new frame
        label1 = tk.Label(self.frame6, text="input customer name you want to delete: ")
        
        # display input field for the new frame
        e = tk.Entry(self.frame6, bg='#f0f0fc', width=50)
        
        # display buttons for the new frame
        button = HoverButton(self.frame6, text="Enter!", command=lambda: try_delete(e.get()))
        back_button = HoverButton(self.frame6, text="Back", command= lambda: back_to_frame3(self.frame6))
        
        # positioning frame using grid system
        label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
        e.grid(row=1, column=3,padx=10) 
        button.grid(row=2, column=3, padx=15,pady=10,sticky = 'E')
        back_button.grid(row=2, column=1, padx=25,sticky = 'W')
        
        # display frame on screen
        self.frame6.pack()
        
        # back button function to move to the previous frame
        def back_to_frame3(frame):
               frame.forget()
               self.frame3.pack()
        
        # function for entered customer deletion 
        def try_delete(customer_name):
        
            # setting customer_account variable to entered customer
            customer_account = self.search_customers_by_name(customer_name)
            
            # if customer account found
            if customer_account != None:
            
                # remove customer account object from the list
                self.customers_accounts_list.remove(customer_account)
                
                # opening file having customers accounts data for reading
                newfile =  open('customer_accounts.txt', "r")
                
                # reading lines from the file and storing to 'Lines'
                lines = newfile.readlines()
                
                # closing file object
                newfile.close()
                
                # opening file having customers accounts data for updation of new balances after transaction
                newfile = open('customer_accounts.txt', "w")
                
                # loop for every line in the file
                for line in lines:
                
                    # word number count in the line
                    word_count = 0
                    
                    # loop for every word separated by , in the specified line    
                    for word in line.split(','): 
                        
                        # if the word is second word (i.e. the last name of customer)
                        if word_count == 1:
                    
                            # if the last name is not of the customer to be deleted
                            if word != customer_name:
                            
                                # write the line as it is
                                newfile.write(line)
                            
                            # break the loop for next line
                            break
                         
                        # incrementing the word number count corrresponding to next iteration of the loop over the same line
                        word_count+=1
                
                # closing the file object
                newfile.close()
                
                # showing the required message on the message box to user
                msg = "%s was deleted successfully!" %customer_name
                tk.messagebox.showinfo( "Delete Customer", msg)
                
    
    # function for the updation of admin own information (i.e. name and address)
    def update_admin_info(self, admin_obj):
        
        # remove current frame from the display
        self.frame3.forget()
    
        # setting label for the new frame to display 
        button1 = HoverButton(self.frame7, text="1) Update admin name", command=lambda: update_info('1'))
        button2 = HoverButton(self.frame7, text="2) Update admin address", command=lambda: update_info('2'))
        label3 = tk.Label(self.frame7, text=" ")
        label4 = tk.Label(self.frame7, text="Choose your option: ")
        
        # setting buttons for the new frame to display
        back_button = HoverButton(self.frame7, text="Back", command= lambda: back_to_frame3(self.frame7))
        
        
        # positioning frame contents appropriately using grid system
        button1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
        button2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
        label3.grid(row=3, column=1)
        label4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')
        back_button.grid(row=5, column=2,padx=15,pady=10,sticky = 'E')
        
        # packing the frame to display on screen
        self.frame7.pack()
        
        # back button function for previous frame
        def back_to_frame3(frame):
            frame.forget()
            self.frame3.pack()
        
        # update information function for enetered choice
        def update_info(option):
        
            # if choice entered is '1' to update admin name
            if option == '1':
            
                # remove current frame from the display
                self.frame7.forget()
                
                # setting label for the new frame to display
                label1 = tk.Label(self.frame8, text="Enter new admin first name: ")
                label2 = tk.Label(self.frame8, text="Enter new admin last name: ")
                
                # setting buttons for the new frame to display
                button = HoverButton(self.frame8, text="Update Name!", command=lambda: try_update(e1.get(), e2.get()))
                back_button = HoverButton(self.frame8, text="Back", command= lambda: back_to_frame7(self.frame8))
                
                # setting input fields for the new frame to display
                e1 = tk.Entry(self.frame8, width=50)
                e2 = tk.Entry(self.frame8, width=50)
                
                # positioning frame contents appropriately using grid system
                label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                label2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
                e1.grid(row=1, column=3,padx=10)
                e2.grid(row=2, column=3,padx=10)
                button.grid(row=3, column=3, padx=15,pady=10,sticky = 'E')
                back_button.grid(row=3, column=1,padx=25,sticky = 'W')
                
                # packing the frame to display on screen
                self.frame8.pack()
                
                # back button function for previous frame
                def back_to_frame7(frame):
                   frame.forget()
                   self.frame7.pack()
                
                # function to update for entered admin firstname and last name
                def try_update(fname, sname):
                
                    # calling method for the admin firstname update
                    admin_obj.update_first_name(fname)
                    
                    # calling method for the admin last name update
                    admin_obj.update_last_name(sname)
                    
                    # showing the required message on the message box to user
                    msg = "Names updated successfully! "
                    tk.messagebox.showinfo( "Names update", msg)
                    
            # if choice entered is '2' to update admin address   
            elif option == '2':
                
                # remove current frame from the display
                self.frame7.forget()
                
                # setting labels for the new frame to display
                label1 = tk.Label(self.frame9, text="Enter new house number: ")
                label2 = tk.Label(self.frame9, text="Enter new street name: ")
                label3 = tk.Label(self.frame9, text="Enter new city name: ")
                label4 = tk.Label(self.frame9, text="Enter new post code: ")
                
                # setting buttons for the new frame to display
                button = HoverButton(self.frame9, text="Update Address!", command=lambda: try_update_address(e1.get(), e2.get(),e3.get(),e4.get()))
                back_button = HoverButton(self.frame9, text="Back", command= lambda: back_to_frame7(self.frame9))
                
                # setting input fields for the new frame to display
                e1 = tk.Entry(self.frame9, bg='#f0f0fc', width=50)
                e2 = tk.Entry(self.frame9, bg='#f0f0fc', width=50)
                e3 = tk.Entry(self.frame9, bg='#f0f0fc', width=50)
                e4 = tk.Entry(self.frame9, bg='#f0f0fc', width=50)
                
                # positioning frame contents appropriately using grid system
                label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                label2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
                label3.grid(row=3, column=1,padx=20,pady=10,sticky = 'W')
                label4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')
                e1.grid(row=1, column=3,padx=10)
                e2.grid(row=2, column=3,padx=10)
                e3.grid(row=3, column=3,padx=10)
                e4.grid(row=4, column=3,padx=10)   
                button.grid(row=5, column=3, padx=15,pady=10,sticky = 'E')
                back_button.grid(row=5, column=1, padx=25,sticky = 'W')
                
                # packing the frame to display on screen
                self.frame9.pack()
                
                # back button function for previous frame
                def back_to_frame7(frame):
                   frame.forget()
                   self.frame7.pack()
                
                 # function to update for entered admin address
                def try_update_address(house_num, street_name, city_name, post_code):
                    #ToDo
                     # creating empty addr list
                    addr = []
                     # appending address information to list
                    addr.append(house_num)
                    addr.append(street_name)
                    addr.append(city_name)
                    addr.append(post_code)
                    
                    # calling method for the admin address update by passing addr list
                    admin_obj.update_address(addr)
                    
                    # showing the required message on the message box to user
                    msg = "Address updated successfully! "
                    tk.messagebox.showinfo( "Adress update", msg)
            
            # if choice entered is incorrect        
            else:
            
                # showing the required message on the message box to user
                msg = "Choose a correct option!"
                tk.messagebox.showinfo( "Update Admin Information", msg)
             
    # method for the creation of new customer account
    def create_customer_account(self):
        
        # remove current frame from the display
        self.frame3.forget()
        
        # setting labels for the new frame to display
        label1 = tk.Label(self.frame10, text="Enter customer first name: ")
        label2 = tk.Label(self.frame10, text="Enter customer last name: ")
        label3 = tk.Label(self.frame10, text="Enter house number: ")
        label4 = tk.Label(self.frame10, text="Enter street name: ")
        label5 = tk.Label(self.frame10, text="Enter city name: ")
        label6 = tk.Label(self.frame10, text="Enter post code: ")
        label7 = tk.Label(self.frame10, text="Enter balance: ")
        
        # setting buttons for the new frame to display
        button = HoverButton(self.frame10, text="Create new Customer!", command=lambda: try_new(e1.get(), e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get()))
        back_button = HoverButton(self.frame10, text="Back", command= lambda: back_to_frame3(self.frame10))
                
        # setting input fields for the new frame to display
        e1 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        e2 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        e3 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        e4 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        e5 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        e6 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        e7 = tk.Entry(self.frame10, bg='#f0f0fc', width=50)
        
        # positioning frame contents appropriately using grid system
        label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
        label2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
        label3.grid(row=3, column=1,padx=20,pady=10,sticky = 'W')
        label4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')
        label5.grid(row=5, column=1,padx=20,pady=10,sticky = 'W')
        label6.grid(row=6, column=1,padx=20,pady=10,sticky = 'W')
        label7.grid(row=7, column=1,padx=20,pady=10,sticky = 'W')    
        e1.grid(row=1, column=3,padx=10)
        e2.grid(row=2, column=3,padx=10)
        e3.grid(row=3, column=3,padx=10)
        e4.grid(row=4, column=3,padx=10)
        e5.grid(row=5, column=3,padx=10)
        e6.grid(row=6, column=3,padx=10)
        e7.grid(row=7, column=3,padx=10)    
        button.grid(row=8, column=3,padx=15,pady=10,sticky = 'E')
        back_button.grid(row=8, column=1,padx=25,sticky = 'W')
        
        # packing the frame to display on screen
        self.frame10.pack()
        
        # back button function for previous frame
        def back_to_frame3(frame):
           frame.forget()
           self.frame3.pack()        
        
        # function to create new customer according to entered inputs
        def try_new(fname, sname, house_num, street_name, city_name, post_code, balance):
        
            # if all the reuired fields are filled
            if (balance != "") & (fname !="") & (sname!="") & (house_num!="") & (street_name!="") & (city_name!="") & (post_code!=""):
            
                # try the following code if entered balance amount is valid
                try:
                
                    # if entered balance if greater than zero
                    if float(balance) >= 0 :
                    
                        # remove current frame from the display
                        self.frame10.forget()
                        
                        # setting account number for the new customer
                        account_no = 1234 + len(self.customers_accounts_list) 
                        
                        # creating empty addr list
                        addr = []
                        
                        # appending address information to list
                        addr.append(house_num)
                        addr.append(street_name)
                        addr.append(city_name)
                        addr.append(post_code)
                        
                        # creating an instance of CustomerAccount with the given input data
                        customer = CustomerAccount(fname, sname, addr, account_no, balance)
                        
                        # setting labels for the new frame to display
                        button1 = HoverButton(self.frame11, text="1) Enter account type", command=lambda: try_account('1'))
                        button2 = HoverButton(self.frame11, text="2) SKIP", command=lambda: try_account('2'))
                        label3 = tk.Label(self.frame11)
                        label4 = tk.Label(self.frame11, text="Choose your option")
                        
                        # setting buttons for the new frame to display
                        back_button = HoverButton(self.frame11, text="Back", command= lambda: back_to_frame10(self.frame11))
                        
                        # positioning frame contents appropriately using grid system
                        button1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                        button2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                        label3.grid(row=3, column=1)
                        label4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')
                        back_button.grid(row=5, column=2,padx=15,pady=10,sticky = 'E')
                        
                        # packing the frame to display on screen
                        self.frame11.pack()
                    
                    # if entered balance if less than zero    
                    else:
                    
                        # showing the required message on the message box to user
                        msg = "Invalid Balance Amount! Should be greater than or equal to zero"
                        tk.messagebox.showinfo( "New Customer Account", msg)
                
                # if entered balance amount is invalid
                except:
                
                    # showing the required message on the message box to user
                    msg = "Invalid Balance Amount"
                    tk.messagebox.showinfo( "New Customer Account", msg)
            
            # if one of the fields is surely empty
            else:
            
                # showing the required message on the message box to user
                msg = "One (or more) of the field(s) is empty"
                tk.messagebox.showinfo( "New Customer Account", msg)
            
            # back button function for previous frame
            def back_to_frame10(frame):
                   frame.forget()
                   self.frame10.pack()
            
            # function to update account type
            def try_account(option):
            
                # if choice entered is '1' to update account type  
                if option == '1':
                
                    # remove current frame from the display
                    self.frame11.forget()
                    
                    # setting labels for the new frame to display
                    label3 = tk.Label(self.frame12)
                    label4 = tk.Label(self.frame12, text="Choose your option")
                    
                    # setting buttons for the new frame to display                  
                    button1 = HoverButton(self.frame12, text="1) Saving Account", command=lambda: try_account_type(('1')))
                    button2 = HoverButton(self.frame12, text="2) Current Account", command=lambda: try_account_type(('2')))
                    back_button = HoverButton(self.frame12, text="Back", command= lambda: back_to_frame11(self.frame12))
                    
                    # positioning frame contents appropriately using grid system
                    button1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                    button2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                    label3.grid(row=3, column=1)
                    label4.grid(row=4, column=1,padx=20,pady=10,sticky = 'W')
                    back_button.grid(row=5, column=2,padx=15,pady=10,sticky = 'E')
                    
                    # packing the frame to display on screen
                    self.frame12.pack()
                    
                    # back button function for previous frame
                    def back_to_frame11(frame):
                           frame.forget()
                           self.frame11.pack()
                            
                    # function to update account type selection for 'saving' or 'current'
                    def try_account_type(type_option):
                    
                        # if choice entered is '1' to select 'saving' account type 
                        if type_option == '1':
                        
                            # setting customer account type to 'saving' 
                            customer.account_type = 'saving'
                            
                            # remove current frame from the display
                            self.frame12.forget()
                            
                            # setting labels for the new frame to display
                            label4 = tk.Label(self.frame13)
                            label5 = tk.Label(self.frame13, text="Choose your option")
                            
                            # setting buttons for the new frame to display
                            button1 = HoverButton(self.frame13, text="1) Traditional or Regular Savings Account", command=lambda: try_saving_type('1'))
                            button2 = HoverButton(self.frame13, text="2) High-Yield Savings Account", command=lambda: try_saving_type('2'))                     
                            button3 = HoverButton(self.frame13, text="3) Speciality Savings account",command=lambda: try_saving_type('3'))
                            back_button = HoverButton(self.frame13, text="Back", command= lambda: back_to_frame12(self.frame13))
                         
                            # positioning frame contents appropriately using grid system
                            button1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                            button2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                            button3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                            label4.grid(row=4, column=1)
                            label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                            back_button.grid(row=8, column=2,padx=15,pady=10,sticky = 'E')
                            
                            # packing the frame to display on screen
                            self.frame13.pack()
                            
                            # back button function for previous frame
                            def back_to_frame12(frame):
                                   frame.forget()
                                   self.frame12.pack()
                            
                            # function to set 'saving' account type selection from different 'saving' accounts
                            def try_saving_type(name_option):
                                
                                # function to set specific 'saving' account type        
                                def try_select_account(s_option):
                                
                                    # if choice selected is '1' to select the regular account 
                                    if s_option == '1':
                             
                                        # checking customer available balance for minimum account openning requirements
                                        if float(customer.balance) >= 500:
                                    
                                            # setting account name, interest rate and overdraft limit to customer account data
                                            customer.account_name = "regular savings account"
                                            customer.interest_rate = 0.1
                                            customer.overdraft_limit = 500
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account name selected successfully! :"+customer.account_name
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account is created successfully!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                            
                                            # remove current frame from the display
                                            self.frame14.forget()
                                            
                                            # calling back function to move back to admin menu
                                            back_to_frame3(self.frame14)
                                            
                                            # appending newly created customer object to the customers_accounts_list
                                            self.customers_accounts_list.append(customer)
                                            
                                            # openning file having customers data to append new customer data in the file
                                            f = open('customer_accounts.txt', "a")
                                            
                                            # writing new line in the file for new customer
                                            f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                                            
                                            # cloasing the file object
                                            f.close()
                                            
                                        # customer available balance is less than minimum account openning requirement
                                        else:
                                       
                                            # showing the required message on the message box to user
                                            msg = "Account creation amount (i.e 500) is higher than available balance:"+str(customer.balance)
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account type not set!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                        
                                    # if choice selected is '2' to select the high yield account          
                                    elif s_option == '2':
                                    
                                        # checking customer available balance for minimum account openning requirements
                                        if float(customer.balance) >= 300:
                                        
                                            # setting account name, interest rate and overdraft limit to customer account data
                                            customer.account_name = "high-yield savings account"
                                            customer.interest_rate = 0.2
                                            customer.overdraft_limit = 200
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account name selected successfully! :"+customer.account_name
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account is created successfully!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                           
                                            # remove current frame from the display
                                            self.frame15.forget()
                                            
                                            # calling back function to move back to admin menu
                                            back_to_frame3(self.frame15)
                                            
                                            # appending newly created customer object to the customers_accounts_list
                                            self.customers_accounts_list.append(customer)
                                            
                                            # openning file having customers data to append new customer data in the file
                                            f = open('customer_accounts.txt', "a")
                                            
                                            # writing new line in the file for new customer
                                            f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                                            
                                            # cloasing the file object
                                            f.close()
                                            
                                            # customer available balance is less than minimum account openning requirement
                                        else:
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account creation amount (i.e 300) is higher than available balance:"+str(customer.balance)
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account type not set!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                     
                                    # if choice selected is '3' to select the speciality account          
                                    elif s_option == '3':
                                        
                                        # checking customer available balance for minimum account openning requirements
                                        if float(customer.balance) >= 100:
                                        
                                            # setting account name, interest rate and overdraft limit to customer account data
                                            customer.account_name = "Speciality savings account"
                                            customer.interest_rate = 0.05
                                            customer.overdraft_limit = 400
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account name selected successfully! :"+customer.account_name
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account is created successfully!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                            
                                            # remove current frame from the display
                                            self.frame16.forget()
                                            
                                            # calling back function to move back to admin menu
                                            back_to_frame3(self.frame16)
                                            
                                            # appending newly created customer object to the customers_accounts_list
                                            self.customers_accounts_list.append(customer)
                                            
                                            # openning file having customers data to append new customer data in the file
                                            f = open('customer_accounts.txt', "a")
                                            
                                            # writing new line in the file for new customer
                                            f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                                            
                                            # closing the file object
                                            f.close()
                                        
                                        # customer available balance is less than minimum account openning requirement
                                        else:
                                        
                                            # showing the required message on the message box to user
                                            msg = "Account creation amount (i.e 100) is higher than available balance:"+str(customer.balance)
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account type not set!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                            
                                # back button function for previous frame
                                def back_to_frame13(frame):
                                       frame.forget()
                                       self.frame13.pack()
                                           
                                # if choice entered is '1' to select the account to see details
                                if name_option == '1':
                                
                                    # remove current frame from the display
                                    self.frame13.forget()
                                    
                                    # setting labels for the new frame to display
                                    label1 = tk.Label(self.frame14, text="Traditional or Regular Savings Account")
                                    label2 = tk.Label(self.frame14, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                     
                                    label3 = tk.Label(self.frame14, text="Yearly Interest Rate: 10%")
                                    label4 = tk.Label(self.frame14, text="OverDraft Limit: 500")
                                    label5 = tk.Label(self.frame14, text="Opening Minimum Balance: 500")
                                    label6 = tk.Label(self.frame14)
                                    label10 = tk.Label(self.frame14, text="Choose your option")
                                    
                                    # setting buttons for the new frame to display                                   
                                    button7 = HoverButton(self.frame14, text="1) Select Account", command=lambda: try_select_account('1'))
                                    back_button = HoverButton(self.frame14, text="Back", command= lambda: back_to_frame13(self.frame14))
                             
                                    # positioning frame contents appropriately using grid system
                                    label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                                    label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                                    label3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                                    label4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                                    label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                                    label6.grid(row=6, column=1)
                                    button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                                    label10.grid(row=10, column=1,padx=20,pady=5,sticky = 'W')
                                    back_button.grid(row=11, column=2,padx=15,pady=10,sticky = 'E')
                                    
                                    # packing the frame to display on screen
                                    self.frame14.pack()
                                
                                # if choice entered is '1' to select the account to see details
                                if name_option == '2':
                                
                                    # remove current frame from the display
                                    self.frame13.forget()
                                
                                    # setting labels for the new frame to display
                                    label1 = tk.Label(self.frame15, text="High-Yield Savings Account")
                                    label2 = tk.Label(self.frame15, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                     
                                    label3 = tk.Label(self.frame15, text="Yearly Interest Rate: 20%")
                                    label4 = tk.Label(self.frame15, text="OverDraft Limit: 200")
                                    label5 = tk.Label(self.frame15, text="Opening Minimum Balance: 300")
                                    label6 = tk.Label(self.frame15, text=" ")
                                    label10 = tk.Label(self.frame15, text="Choose your option: ")
                                    
                                    # setting buttons for the new frame to display
                                    button7 = HoverButton(self.frame15, text="1) Select Account", command=lambda: try_select_account('2'))
                                    back_button = HoverButton(self.frame15, text="Back", command= lambda: back_to_frame13(self.frame15))
                                    
                                    # positioning frame contents appropriately using grid system       
                                    label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                                    label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                                    label3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                                    label4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                                    label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                                    label6.grid(row=6, column=1)
                                    button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                                    label10.grid(row=10, column=1,padx=20,pady=5,sticky = 'W')
                                    back_button.grid(row=11, column=2,padx=15,pady=10,sticky = 'E')
                                    
                                    # packing the frame to display on screen
                                    self.frame15.pack()
                                    
                                    
                                # if choice entered is '3' to select the account to see details            
                                elif name_option == '3':
                                    
                                    # remove current frame from the display
                                    self.frame13.forget()
                                    
                                    # setting labels for the new frame to display
                                    label1 = tk.Label(self.frame16, text="Speciality savings account")
                                    label2 = tk.Label(self.frame16, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                     
                                    label3 = tk.Label(self.frame16, text="Yearly Interest Rate: 5%")
                                    label4 = tk.Label(self.frame16, text="OverDraft Limit: 400")
                                    label5 = tk.Label(self.frame16, text="Opening Minimum Balance: 100")
                                    label6 = tk.Label(self.frame16, text=" ")
                                    label10 = tk.Label(self.frame16, text="Choose your option")
                                    
                                    # setting buttons for the new frame to display
                                    button7 = HoverButton(self.frame16, text="1) Select Account", command=lambda: try_select_account('3'))
                                    back_button = HoverButton(self.frame16, text="Back", command= lambda: back_to_frame13(self.frame16))
                                    
                                    # positioning frame contents appropriately using grid system     
                                    label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                                    label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                                    label3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                                    label4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                                    label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                                    label6.grid(row=6, column=1)
                                    button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                                    label10.grid(row=10, column=1,padx=20,pady=5,sticky = 'W')
                                    back_button.grid(row=11, column=2,padx=15,pady=10,sticky = 'E')
                                    
                                    # packing the frame to display on screen
                                    self.frame16.pack()
                                    
                        # if choice entered is '2' to select 'current' account type 
                        elif type_option == '2':                            
                        
                            # setting customer account type to 'current' 
                            customer.account_type = 'current'
                            
                            # remove current frame from the display
                            self.frame12.forget()
                            
                            # setting labels for the new frame to display
                            label3 = tk.Label(self.frame17)
                            label4 = tk.Label(self.frame17, text="Choose your option: ")
                            
                            # setting buttons for the new frame to display
                            button1 = HoverButton(self.frame17, text="1) Premium Current Account", command=lambda: try_current_type('1'))
                            button2 = HoverButton(self.frame17, text="2) Standard Current Account", command=lambda: try_current_type('2'))
                            button3 = HoverButton(self.frame17, text="3) Packaged Current Account", command=lambda: try_current_type('3'))
                            
                            back_button = HoverButton(self.frame17, text="Back", command= lambda: back_to_frame12(self.frame17))
                            
                            # positioning frame contents appropriately using grid system 
                            button1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                            button2.grid(row=2, column=1,padx=20,pady=10,sticky = 'W')
                            button3.grid(row=3, column=1,padx=20,pady=10,sticky = 'W')
                            
                            label3.grid(row=4, column=1)
                            label4.grid(row=5, column=1,padx=20,pady=10,sticky = 'W')
                            back_button.grid(row=8, column=2,padx=15,pady=10,sticky = 'E')
                            
                            # packing the frame to display on screen
                            self.frame17.pack()
                            
                            # back button function for previous frame
                            def back_to_frame12(frame):
                                   frame.forget()
                                   self.frame12.pack()
                                    
                            # function to set 'saving' account type selection from different 'saving' accounts
                            def try_current_type(name_option):
                                
                                # function to set specific 'current' account type      
                                def try_select_account(s_option):
                                
                                    # if choice selected is '1' to select the premium account
                                    if s_option == '1':
                                    
                                        # checking customer available balance for minimum account openning requirements
                                        if float(customer.balance) >= 1000:
                                        
                                            # setting account name, interest rate and overdraft limit to customer account data
                                            customer.account_name = "premium current account"
                                            customer.interest_rate = 0
                                            customer.overdraft_limit = 2000
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account name selected successfully! :"+customer.account_name
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account is created successfully!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                            
                                            # remove current frame from the display
                                            self.frame18.forget()
                                            
                                            # calling back function to move back to admin menu
                                            back_to_frame3(self.frame18)
                                            
                                            # appending newly created customer object to the customers_accounts_list
                                            self.customers_accounts_list.append(customer)
                                            
                                            # openning file having customers data to append new customer data in the file
                                            f = open('customer_accounts.txt', "a")
                                            
                                            # writing new line in the file for new customer
                                            f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                                            
                                            # closing the file object
                                            f.close()
                                        
                                        # customer available balance is less than minimum account openning requirement
                                        else:
                                        
                                            # showing the required message on the message box to user
                                            msg = "Account creation amount (i.e 1000) is higher than available balance:"+str(customer.balance)
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account type not set!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                   
                                    # # if choice selected is '2' to select the standard account        
                                    elif s_option == '2':
                                        # checking customer available balance for minimum account openning requirements
                                        if float(customer.balance) >= 500:
                                        
                                            # setting account name, interest rate and overdraft limit to customer account data
                                            customer.account_name = "standard current account"
                                            customer.interest_rate = 0
                                            customer.overdraft_limit = 500
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account name selected successfully! :"+customer.account_name
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account is created successfully!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                            
                                            # remove current frame from the display
                                            self.frame19.forget()
                                            
                                            # calling back function to move back to admin menu
                                            back_to_frame3(self.frame19)
                                            
                                            # appending newly created customer object to the customers_accounts_list
                                            self.customers_accounts_list.append(customer)
                                            
                                            # openning file having customers data to append new customer data in the file
                                            f = open('customer_accounts.txt', "a")
                                            
                                            # writing new line in the file for new customer
                                            f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                                            
                                            # closing the file object
                                            f.close()
                                            
                                            # printing messsage
                                            print("\n%s account is created successfully!" %fname)
                                        
                                        # customer available balance is less than minimum account openning requirement
                                        else:
                                        
                                          # showing the required message on the message box to user
                                          msg = "Account creation amount (i.e 500) is higher than available balance:"+str(customer.balance)
                                          tk.messagebox.showinfo( "Account name", msg)
                                          msg = "%s account type not set!" %fname
                                          tk.messagebox.showinfo( "New Customer Account", msg) 
                                    
                                    # if choice selected is '3' to select the packaged account        
                                    elif s_option == '3':
                                        
                                        # checking customer available balance for minimum account openning requirements
                                        if float(customer.balance) >= 500:
                                        
                                            # setting account name, interest rate and overdraft limit to customer account data
                                            customer.account_name = "packaged current account"
                                            customer.interest_rate = 0
                                            customer.overdraft_limit = 500
                                            
                                            # showing the required message on the message box to user
                                            msg = "Account name selected successfully! :"+customer.account_name
                                            tk.messagebox.showinfo( "Account name", msg)
                                            msg = "%s account is created successfully!" %fname
                                            tk.messagebox.showinfo( "New Customer Account", msg)
                                            
                                            # remove current frame from the display
                                            self.frame20.forget()
                                            
                                            # calling back function to move back to admin menu
                                            back_to_frame3(self.frame20)
                                            
                                            # appending newly created customer object to the customers_accounts_list
                                            self.customers_accounts_list.append(customer)
                                            
                                            # openning file having customers data to append new customer data in the file
                                            f = open('customer_accounts.txt', "a")
                                            
                                            # writing new line in the file for new customer
                                            f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                                            
                                            # closing the file object
                                            f.close()
                                            
                                        # customer available balance is less than minimum account openning requirement
                                        else:
                                        
                                          # showing the required message on the message box to user
                                          msg = "Account creation amount (i.e 500) is higher than available balance:"+str(customer.balance)
                                          tk.messagebox.showinfo( "Account name", msg)
                                          msg = "%s account type not set!" %fname
                                          tk.messagebox.showinfo( "New Customer Account", msg)      
                                
                                # back button function for previous frame
                                def back_to_frame17(frame):
                                       frame.forget()
                                       self.frame17.pack()          
                                
                                # if choice entered is '1' to select the account to see details 
                                if name_option == '1':
                                
                                    # remove current frame from the display
                                    self.frame17.forget()
                                    
                                    # setting labels for the new frame to display
                                    label1 = tk.Label(self.frame18, text="Premium Current Account")
                                    label2 = tk.Label(self.frame18, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                     
                                    label3 = tk.Label(self.frame18, text="Interest Rate: 0%")
                                    label4 = tk.Label(self.frame18, text="OverDraft Limit: 2000")
                                    label5 = tk.Label(self.frame18, text="Opening Minimum Balance: 1000")
                                    label6 = tk.Label(self.frame18)
                                    label10 = tk.Label(self.frame18, text="Choose your option: ")
                                    
                                    # setting buttons for the new frame to display
                                    button7 = HoverButton(self.frame18, text="1) Select Account", command=lambda: try_select_account('1'))
                                    back_button = HoverButton(self.frame18, text="Back", command= lambda: back_to_frame17(self.frame18))
                                   
                                    # positioning frame contents appropriately using grid system       
                                    label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                                    label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                                    label3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                                    label4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                                    label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                                    label6.grid(row=6, column=1)
                                    button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                                    label10.grid(row=10, column=1,padx=20,pady=5,sticky = 'W')
                                    back_button.grid(row=11, column=2,padx=15,pady=10,sticky = 'E')
                                    
                                    # packing the frame to display on screen
                                    self.frame18.pack()
                                 
                                # if choice entered is '2' to select the account to see details
                                elif name_option == '2':
                                    
                                    # remove current frame from the display
                                    self.frame17.forget()
                                    
                                    # setting labels for the new frame to display
                                    label1 = tk.Label(self.frame19, text="Standard Current Account")
                                    label2 = tk.Label(self.frame19, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                     
                                    label3 = tk.Label(self.frame19, text="Interest Rate: 0%")
                                    label4 = tk.Label(self.frame19, text="OverDraft Limit: 500")
                                    label5 = tk.Label(self.frame19, text="Opening Minimum Balance: 500")
                                    label6 = tk.Label(self.frame19)
                                    label10 = tk.Label(self.frame19, text="Choose your option: ")
                                    
                                    # setting buttons for the new frame to display
                                    button7 = HoverButton(self.frame19, text="1) Select Account", command=lambda: try_select_account('2'))
                                    back_button = HoverButton(self.frame19, text="Back", command= lambda: back_to_frame17(self.frame19))
                                    
                                    # positioning frame contents appropriately using grid system         
                                    label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                                    label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                                    label3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                                    label4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                                    label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                                    label6.grid(row=6, column=1)
                                    button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                                    label10.grid(row=10, column=1,padx=20,pady=5,sticky = 'W')
                                    back_button.grid(row=11, column=2,padx=15,pady=10,sticky = 'E')
                                    
                                    # packing the frame to display on screen
                                    self.frame19.pack()
                              
                                # if choice entered is '3' to select the account to see details
                                elif name_option == '3':
                                    
                                    # remove current frame from the display
                                    self.frame17.forget()
                                    
                                    # setting labels for the new frame to display
                                    label1 = tk.Label(self.frame20, text="Packaged Current Account")
                                    label2 = tk.Label(self.frame20, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                     
                                    label3 = tk.Label(self.frame20, text="Interest Rate: 0%")
                                    label4 = tk.Label(self.frame20, text="OverDraft Limit: 800")
                                    label5 = tk.Label(self.frame20, text="Opening Minimum Balance: 600")
                                    label6 = tk.Label(self.frame20)
                                    label10 = tk.Label(self.frame20, text="Choose your option: ")
                                    
                                    # setting buttons for the new frame to display
                                    button7 = HoverButton(self.frame20, text="1) Select Account", command=lambda: try_select_account('3'))
                                    back_button = HoverButton(self.frame20, text="Back", command= lambda: back_to_frame17(self.frame20))
                                    
                                    # positioning frame contents appropriately using grid system         
                                    label1.grid(row=1, column=1,padx=20,pady=10,sticky = 'W')
                                    label2.grid(row=2, column=1,padx=20,pady=5,sticky = 'W')
                                    label3.grid(row=3, column=1,padx=20,pady=5,sticky = 'W')
                                    label4.grid(row=4, column=1,padx=20,pady=5,sticky = 'W')
                                    label5.grid(row=5, column=1,padx=20,pady=5,sticky = 'W')
                                    label6.grid(row=6, column=1)
                                    button7.grid(row=7, column=1,padx=20,pady=5,sticky = 'W')
                                    label10.grid(row=10, column=1,padx=20,pady=5,sticky = 'W')
                                    back_button.grid(row=11, column=2,padx=15,pady=10,sticky = 'E')
                                    
                                    # packing the frame to display on screen
                                    self.frame20.pack()
                                          
                # if choice entered is '2' to skip updating the account type  
                elif option == '2':
                
                    # append newly created customer to the accuonts list
                    self.customers_accounts_list.append(customer)
                    
                    # showing the required message on the message box to user
                    msg = "%s account is created successfully!" %fname
                    tk.messagebox.showinfo( "New Customer Account", msg)
                    back_to_frame3(self.frame11)
                    
                    # openning file having customers data to append new customer data in the file
                    f = open('customer_accounts.txt', "a")
                    
                    # writing new line in the file for new customer
                    f.write("\n"+fname+","+sname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(account_no)+","+str(balance)+","+customer.account_type+","+customer.account_name+","+str(customer.interest_rate)+","+str(customer.overdraft_limit))
                    
                    # closing the file object
                    f.close()
    
    # method to details of all the customers in the bank
    def print_all_accounts_details(self):
        
            # list related operation - move to main.py
            # count for customer number in the list
            i = 0
     
            # loop for every customer in the customers_accounts_list
            for customer_account in self.customers_accounts_list:
                i+=1
            
                # printing customer details on console
                print('\n %d. ' %i, end = ' ')
                
                # method for showing customers details on the message box
                # showing the customer details on the message box to user
                msg = "First name: %s" %customer_account.fname +"\nLast name: %s" %customer_account.lname+"\nAccount No: %s" %customer_account.account_no+"\nAddress: %s" %customer_account.address[0]+"\n         %s" %customer_account.address[1]+"\n         %s" %customer_account.address[2]+"\n         %s" %customer_account.address[3]+"\n "
                tk.messagebox.showinfo( "Customer Details", msg)
                print("------------------------")
              
# creating an instance of BankSystem Class
root = BankSystem()

# calling 'run_main_options' method to start appplication
root.run_main_options()

# setting application title
root.title("Python Banking System")

# set window size
root.geometry("600x500")

#set window color
root['background']='#856ff8'

# set window icon
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='logo.png'))

# mainloop for the GUI programming
root.mainloop()