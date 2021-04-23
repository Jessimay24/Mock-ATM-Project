# create record
# update record
# read record
# delete
# CRUD

import os 

user_db_path = "data/user_record/"

def create(accountNumber, user_details):

    completion_state = False

    try:    
        f = open(user_db_path + str(accountNumber) + '.txt', 'x')
          
    except FileExistsError:
        print('User already exists')
        delete(accountNumber)
        
        #delete the already created file, and print out error, then return false
        
    else:
        f.write(str(user_details));
        completion_state = True

    finally:
        f.close();
        return completion_state 
        
    

    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true


def update(accountNumber):
    print('update user record')
    # find the user with account number
    # fetch the content of the file
    # update the content of the file
    # return true


def read(accountNumber):
    print('read user record')
    f = open(user_db_path + str(accountNumber) + '.txt', 'r')
    return f.readline()
    # find user with account number
    # fetch content of the file


def delete(accountNumber):

    is_delete_Successful = False
    
    if os.path.exists(user_db_path + str(accountNumber)+ ".txt"):
        try:
            os.remove(user_db_path + str(accountNumber)+ ".txt")
            is_delete_Successful = True
            
        except FileNotFoundError:
            print('User not found')

        finally:

           return is_delete_Successful
    
    # find user with account number
    # delete the user file

    
#def find(accountNumber):
  # print('find user')
    # find user in the data fold
delete(11111111111)


#print(read(2585774492))
print(read(4089169140))

