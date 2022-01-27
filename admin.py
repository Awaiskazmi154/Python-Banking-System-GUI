
# Admin Class for the admins
class Admin:
    
    # class initialization
    def __init__(self, fname, lname, address, user_name, password, full_rights):

        # class variables
        
        # admin first name
        self.fname = fname 
        
        # admin last name
        self.lname = lname 
        
        # admin address
        self.address = address 
        
        # admin username
        self.user_name = user_name 
        
        # admin password
        self.password = password 
        
        # full administrative rights
        self.full_admin_rights = full_rights 
    
    
    # getter function for the first name of the admin       
    def get_first_name(self):
        return self.fname
    
    # getter function for the last name of the admin 
    def get_last_name(self):
        return self.lname
    
    # getter function for the user name of the admin 
    def get_username(self):
        return self.user_name
    
    # getter function for the address of the admin
    def get_address(self):
        return self.address      
    
    # getter function for the password of the admin
    def get_password(self):
        return self.password
    
    # function to see whther admin has full rights or not
    def has_full_admin_right(self):   
        return self.full_admin_rights

    # function to update first name of the admin
    def update_first_name(self, fname):
        
        # setting admin obects first name to updated first name
        self.fname = fname
    
    # function to update last name of the admin
    def update_last_name(self, lname):
    
        # setting admin obects last name to updated last name
        self.lname = lname
    
    # function to update address of the admin
    def update_address(self, addr):
        self.address = addr
    
    # function to update password of the admin
    def update_password(self, password):
        # setting admin obect's password to updated password
        self.password = password
    
    # function to update username of the admin
    def set_username(self, uname):
        # setting admin obect's user name to updated user name
        self.user_name = uname
    
    # function to update administration rights of the admin
    def set_full_admin_right(self, admin_right): 
    
        # setting admin obect's rights to updated rights
        self.full_admin_rights = admin_right
    
    
