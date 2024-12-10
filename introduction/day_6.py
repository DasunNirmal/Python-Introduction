# BASIC WAY TO READ A FILE OR WRITE A FILE

# file_01 = open("myfile.txt","r") 
# by default it is read mode but you can specify it as "r" mode as well
# if in in the read mode the specified file does not exist, it will throw an error

    # file_contents_1 = file_01.read()
    # file_contents_2 = file_01.readline()
    # file_contents_3 = file_01.readlines()

    # print("using read() :",file_contents_1) # Dasun Nirmal 21
    # print("using readline() :",file_contents_2) # Dasun
    # print("using readlines() :",file_contents_3) # ['Dasun\n', 'Nirmal\n', '21']

# file_01.close()

# with open("myfile.txt","r") as file_02:
    
    # file_contents_1 = file_02.read()
    # file_contents_2 = file_02.readline()
    # file_contents_3 = file_02.readlines()
    
    # print("using read() :",file_contents_1) # Dasun Nirmal 21
    # print("using readline() :",file_contents_2) # Dasun
    # print("using readlines() :",file_contents_3) # ['Dasun\n', 'Nirmal\n', '21']

    # Using with we don't need to close the file manually

with open("myfile_2.txt","w") as file_03:

    # using the write command when we try to write a new line the existing line will be erased and then the new line will wirte 

    # file_03.write("Hello World \nthis is our python class")
    my_list = list(("Hi\n","This is a new line created using\n","writelines"))
    my_list.append("\nWe are IJSE")
    file_03.writelines(my_list)
    