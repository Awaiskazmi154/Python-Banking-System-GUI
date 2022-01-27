
# CustomerAccount Class inheriting TK class
class CustomerAccount():
    
    # class initialization
    def __init__(self, fname, lname, address, account_no, balance):
       
        # method to inherit functionality
        super().__init__()
     
        # class variables
        self.fname = fname # first name
        self.lname = lname # last name
        self.address = address # address 
        self.account_no = account_no # account number
        self.balance = float(balance) # balance
        self.account_type = "" # account type
        self.account_name = "" # account name
        self.interest_rate = "" # interest rate
        self.overdraft_limit = "" # overdraft limit
    
    # function for updating first name of the customer    
    def update_first_name(self, fname):
        
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
                    if (word != self.fname):
                    
                        # write the line as it is
                        newfile.write(line)
                    
                    # if the word is the first name of customer to be updated
                    else:
                    
                        # write the line for the customer new data (updated first name)
                        newfile.write("\n"+fname+","+self.lname+","+self.address[0]+","+self.address[1]+","+self.address[2]+","+self.address[3]+","+str(self.account_no)+","+str(self.balance)+","+self.account_type+","+self.account_name+","+str(self.interest_rate)+","+str(self.overdraft_limit))
                
                # incrementing the word number count corrresponding to next iteration of the loop over the same line
                count+=1
        
        # closing the file object after writing the data into it      
        newfile.close()
        
        # setting customer obects first name to updated first name
        self.fname = fname
    
    # method to update last name of the customer     
    def update_last_name(self, lname):
        
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
                    if (word != self.fname):
                    
                        # write the line as it is
                        newfile.write(line)
                    
                    # if the word is the first name of customer to be updated
                    else:
                    
                        # write the line for the customer new data (updated last name)
                        newfile.write("\n"+self.fname+","+lname+","+self.address[0]+","+self.address[1]+","+self.address[2]+","+self.address[3]+","+str(self.account_no)+","+str(self.balance)+","+self.account_type+","+self.account_name+","+str(self.interest_rate)+","+str(self.overdraft_limit))
                
                # incrementing the word number count corrresponding to next iteration of the loop over the same line    
                count+=1
        
        # closing the file object after writing the data into it        
        newfile.close()
        
        # setting customer obects last name to updated last name
        self.lname = lname
    
    # function for getting first name of the customer            
    def get_first_name(self):
        return self.fname
    
    # function to get last name of the customer
    def get_last_name(self):
        return self.lname
    
    # function to update address of the customer    
    def update_address(self, addr):
        
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
                    if (word != self.fname):
                    
                        # write the line as it is
                        newfile.write(line)
                    
                    # if the word is the first name of customer to be updated
                    else:
                    
                        # write the line for the customer new data (updated address)
                        newfile.write("\n"+self.fname+","+self.lname+","+addr[0]+","+addr[1]+","+addr[2]+","+addr[3]+","+str(self.account_no)+","+str(self.balance)+","+self.account_type+","+self.account_name+","+str(self.interest_rate)+","+str(self.overdraft_limit))
                
                # incrementing the word number count corrresponding to next iteration of the loop over the same line    
                count+=1
        
        # closing the file object after writing the data into it         
        newfile.close()
        
        # setting customer obects address to updated address
        self.address = addr
    
    # function to get address of the customer 
    def get_address(self):
        return self.address
    
    # function to deposit amount in the customer account 
    def deposit(self, amount):
        
        # increasing the customer balance according to the deposited amount 
        self.balance+=amount
       
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
                    if (word != self.fname):
                    
                        # write the line as it is
                        newfile.write(line)
                    
                    # if the word is the first name of customer to be updated
                    else:
                    
                        # write the line for the customer new data (new balance after deposit)
                        newfile.write("\n"+self.fname+","+self.lname+","+self.address[0]+","+self.address[1]+","+self.address[2]+","+self.address[3]+","+str(self.account_no)+","+str(self.balance)+","+self.account_type+","+self.account_name+","+str(self.interest_rate)+","+str(self.overdraft_limit))
                 
                # incrementing the word number count corrresponding to next iteration of the loop over the same line   
                count+=1
        
        # closing the file object after writing the data into it       
        newfile.close()
    
    
        
        