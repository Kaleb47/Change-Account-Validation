# first you open the file

try:

  file = open('accounts.txt', 'r')
#then you read the file
  with open('accounts.txt') as f:
    accounts = file.readlines()
#input any number you want
    numeric = input("Enter charge number: ")
#assuming that the name is 0, but we'll increment it
  name = 0
#define the data as i in the read file
  for i in range(len(accounts)):
    if numeric == i:
     name = 1 #assigning a variable
    break; #offers an exit from the loop
  if name == 1: #checking if it equals 1
    print("The charge account is in the list")
  else:
    print("the charge account does not exist")
except IOError:
        print('The file could not be found')
except:
        print('An error occurred')

