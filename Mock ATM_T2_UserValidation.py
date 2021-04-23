#Mock up ATM Project Improvements
#Login
#Register
#Bank Operations
#Generate Account Funtions
#Use functions

import datetime
import random
import validation
import database


datetime_object = datetime.datetime.now()
def accountCreator():
    return random.randrange(1111111111,9999999999)


def init():
    print(datetime_object)
    print('Welcome to Global Bank')
    print('Do you have an account with us? \n')
    accountStatus = int(input(' Select (1) yes, login (2) no, Register, (3) no, Exit  \n'))
    if(accountStatus == 1):
        login()
    elif(accountStatus == 2):
        register()
    else: print ('Exit')
        

def login():
    accountNumber = input('To login enter account number. \n')
    
    is_valid_account_number = validation.account_number_validation(accountNumber)

    if is_valid_account_number:
        password = input(' Enter password \n')
        print('How can we help you today?')
        operations()
    else:
        print("invalid account number")
        login()

        
def operations():
    print('1.Withdrawl')
    print('2.Cash Deposit')
    print('3.Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option: \n'))
    if(selectedOption == 1):
            print('you selected %s' %selectedOption)
            withdrawal = int(input('How much would you like to withdraw?'))
            if(withdrawal >= 10):
                print('Please take your $ %s' % withdrawal)
                transactionCompleted()
            elif(withdrawal < 10):
                print('Cannot withdraw less than $10')
                operations()
               
            else:
                print('Invalid Option')

    elif(selectedOption == 2):
            print('you selcted %s' %selectedOption)
            deposit = int(input('How much would you like to deposit?'))
            print('Current balance is $ %s' % deposit)
            print(' How else can we serve you?')
            operations()
            while(deposit < 0):
                print('return to main menu')
                operations()
            
    elif(selectedOption == 3):
            print('you selcted %s' %selectedOption)
            complaint = input('What issue would you like to report?')
            print("%s , We will review the issue shortly." %complaint)
            print('Thank you for contacting us. How else can we serve you?')
            operations()
            
    elif(selectedOption == 4):
            login()
    else:
        print('Invalid option selected, please try again')
        operations()

def register ():
    print('Welcome to registration')
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")
    generateAccountNumber = accountCreator()
    accountNumber=generateAccountNumber
    
    userAccountInfo = [accountNumber, first_name, last_name, email, password,0 ]

    is_user_created = database.create(accountNumber,[first_name, last_name, email, password,0 ])

    if is_user_created:
       
        print("Your account has been created")
        print('Your account number is: %s' % generateAccountNumber)
        print("Your account credentials are %s" % userAccountInfo)

        login()
         


init()



