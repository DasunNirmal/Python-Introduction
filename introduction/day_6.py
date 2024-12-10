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


    
# while True :
#     print("\nEnter 1 to Add a Contact: ")
#     print("Enter 2 to View Contacts: ")
#     print("Enter 3 to exit: \n")

#     option = input("Optin : ")
#     if option == "1" :
#         print("\n=========================================================\n")
#         with open("contact.txt","a") as contacts :
#             name = input("Enter Name : ")
#             phone_number = input("Enter Your Phone Number : ")
#             email = input("Enter Your Email : ")
#             contacts.write(f"\n\nName: {name} \nPhone Number: {phone_number} \nEmail: {email}\n")
#             print("=========================================================\n")
#     else :
#         print("wrong input try again")
#         continue

#     if option == "2" :
#         print("=========================================================")
#         with open("contact.txt","r") as readContacts:
#             c = readContacts.read()
#             print(c,"\n")
#             print("=========================================================")
#     else :
#         print("wrong input try again!!")
#         continue

#     if option == "3" :
#         exit()            

# {jason eky should be string unlike python dictionary key where ut can be any immutable type}
# import json
# json_file_path = "example_1.json"
# with open("Python/introduction/example_1.json","r") as json_file:
#     json_data = json.load(json_file) # load uses to convert the json to a dict

# print(json_data,type(json_data))

# data = {
#     "Name": "Dasun",
#     "Age": "21",
#     "Address": "Ragama"
# }
# jason_file_path = "test.json"
# with open(jason_file_path,"w") as json_file:
#     jason_data = json.dumps(data,indent=4) # dump uses to convert the dict to a json
#     json_file.write(jason_data)

# print(f"Data has been written to {jason_file_path}")

# you are given a josn file name students.json which contents info about students and their marks
# your task is to 
# read the file and display the data in the following format
# display the names of all students who scored above 75
# add a new student to the file
# save the updated data back to the json file


# jason_file_path = "student.json"
# with open(jason_file_path,"r") as json_file:
#     jason_data = json.load(json_file)
    
#     for student in jason_data:
#         if student["grade"] > 75:
#             print("Student Who got over 75% marks : ",student["name"],"::",student["grade"])

# new_student = {
#     "name": "Nirmal",
#     "grade": 85
# }
# with open(jason_file_path,"w") as json_file:
#     jason_data.append(new_student)
#     json.dump(jason_data,json_file,indent=4)

# to store strcured we can use csv files

import csv
csv_file_path = "customers-1000.csv"
with open(csv_file_path,"r",newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)