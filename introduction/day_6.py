# BASIC WAY TO READ A FILE OR WRITE A FILE

# file_01 = open("myfile_1.txt","r") 
# by default it is read mode but you can specify it as "r" mode as well
# if in in the read mode the specified file does not exist, it will throw an error

    # file_contents_1 = file_01.read()
    # file_contents_2 = file_01.readline()
    # file_contents_3 = file_01.readlines()

    # print("using read() :",file_contents_1) # Dasun Nirmal 21
    # print("using readline() :",file_contents_2) # Dasun
    # print("using readlines() :",file_contents_3) # ['Dasun\n', 'Nirmal\n', '21']

# file_01.close()

# with open("myfile_1.txt","r") as file_02:
    
    # file_contents_1 = file_02.read()
    # file_contents_2 = file_02.readline()
    # file_contents_3 = file_02.readlines()
    
    # print("using read() :",file_contents_1) # Dasun Nirmal 21
    # print("using readline() :",file_contents_2) # Dasun
    # print("using readlines() :",file_contents_3) # ['Dasun\n', 'Nirmal\n', '21']

    # Using with we don't need to close the file manually

# with open("myfile_2.txt","w") as file_03:

#     # using the write command when we try to write a new line the existing line will be erased and then the new line will wirte 

#     # file_03.write("Hello World \nthis is our python class")
#     my_list = list(("Hi\n","This is a new line created using\n","writelines"))
#     my_list.append("\nWe are IJSE")
#     file_03.writelines(my_list)

# TASK
    
# implemetn a simple contact management System
# create a sys that store and manage contacts...file name contact.txt
# each contact should be inclued name, phone number,email

# add a new contact - append the contact to the file
# view all conatcts - read and disply all contacts
# exits the program


    
while True :
    print("\nEnter 1 to Add a Contact: ")
    print("Enter 2 to View Contacts: ")
    print("Enter 3 to exit: \n")

    option = input("Optin : ")
    if option == "1" :
        print("\n=========================================================\n")
        with open("contact.txt","a") as contacts :
            name = input("Enter Name : ")
            phone_number = input("Enter Your Phone Number : ")
            email = input("Enter Your Email : ")
            contacts.write(f"\n\nName: {name} \nPhone Number: {phone_number} \nEmail: {email}\n")
            print("=========================================================\n")
    else :
        print("wrong input try again")
        continue

    if option == "2" :
        print("=========================================================")
        with open("contact.txt","r") as readContacts:
            c = readContacts.read()
            print(c,"\n")
            print("=========================================================")
    else :
        print("wrong input try again!!")
        continue

    if option == "3" :
        exit()            