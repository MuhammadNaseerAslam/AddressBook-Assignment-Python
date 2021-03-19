import os
def AdressBook():
    print("We are going to save a contact!")
    f_W=open("Address Book.txt", mode='a')
    FName=input("Please Enter your First Name:  ")
    LName=input("Please Enter your Last Name:  ")
    MobileNo=(input("Please Enter your Mobile Number :  "))
    City =input("Please Enter your City:  ")
    Email=input("Please Enter your Email:  ")
    Profession=input("Please Enter your Profession:  ")
    f_W.write(FName+","+LName+","+MobileNo+","+City+","+Email+","+Profession+'\n')
    print("OH yes Sucessfully Contact Saved!")
    f_W.close()
def SearchByFirstName():
    print("We are going to search record by First Name")
    f_r=open("Address Book.txt", mode='r')
    FName_S=input("Please input First name which you want to search:   ")
    s =' '
    count=0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[0]==FName_S):
              count=count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count==0:
        print("This First Name is not in our record Sorry!")
    f_r.close()
def SearchByLastName():
    print("We are going to search record by Last Name")
    f_r=open("Address Book.txt", mode='r')
    LName_S=input("Please input Last name which you want to search:   ")
    s =' '
    count = 0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[1]==LName_S):
              count = count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count == 0:
       print("This Last Name is not in our record Sorry!")
    f_r.close()
def SearchByMobile():
    print("We are going to search record by Mobile Number")
    f_r=open("Address Book.txt", mode='r')
    Mobile_S=input("Please input Last name which you want to search:   ")
    s =' '
    count = 0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[2]==Mobile_S):
              count = count + 1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count == 0:
       print("This Mobile Number is not in our record Sorry!")
    f_r.close()
def SearchByEmail():
    print("We are going to search record by Email")
    f_r=open("Address Book.txt", mode='r')
    Email_S=input("Please input Email which you want to search:   ")
    s =' '
    count =0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[4]==Email_S):
              count = count + 1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count == 0:
       print("This Email is not in our record Sorry!")
    f_r.close()
def SearchByCity():
    print("We are going to search record by City")
    f_r=open("Address Book.txt", mode='r')
    City_S=input("Please input City which you want to search:   ")
    s =' '
    count =0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[3]==City_S):
              count = count + 1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count == 0:
       print(City_S+"  city is not in our record Sorry!")
    f_r.close()
def SpecialSearchByFirstName():
    print("We are going to search record by First Name key")
    f_r=open("Address Book.txt", mode='r')
    FName_S=input("Please input First name key which you want to search:   ")
    s =' '
    count=0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[0].find(FName_S)!=-1):
              count=count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count==0:
        print("This First Name key is not in our record Sorry!")
    f_r.close()
def SpecialSearchByLastName():
    print("We are going to search record by Last Name key")
    f_r=open("Address Book.txt", mode='r')
    FName_S=input("Please input Last name key which you want to search:   ")
    s =' '
    count=0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[1].find(FName_S)!=-1):
              count=count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count==0:
        print("This Last Name key is not in our record Sorry!")
    f_r.close()
def SpecialSearchByMobileNumber():
    print("We are going to search record by Mobile Number key")
    f_r=open("Address Book.txt", mode='r')
    FName_S=input("Please input Mobile No key which you want to search:   ")
    s =' '
    count=0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[2].find(FName_S)!=-1):
              count=count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count==0:
        print("This Moile No key is not in our record Sorry!")
    f_r.close()
def SpecialSearchByCity():
    print("We are going to search record by City key")
    f_r=open("Address Book.txt", mode='r')
    FName_S=input("Please input City key which you want to search:   ")
    s =' '
    count=0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[3].find(FName_S)!=-1):
              count=count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count==0:
        print("This City key is not in our record Sorry!")
    f_r.close()
def SpecialSearchByEmail():
    print("We are going to search record by Email key")
    f_r=open("Address Book.txt", mode='r')
    FName_S=input("Please input Email key which you want to search:   ")
    s =' '
    count=0
    while (s):
        s=f_r.readline()
        L=s.split(",")
        if len(s)>0:
           if (L[4].find(FName_S)!=-1):
              count=count+1
              print("Here is your Record which You want to search")
              print("FName is: ", L[0])
              print("LName is: ", L[1])
              print("Mobile No is: ", L[2])
              print("City is: ", L[3])
              print("Email is: ", L[4])
              print("Profession is: ", L[5])
    if count==0:
        print("This Email key is not in our record Sorry!")
    f_r.close()
def DeleteContactByName():
    print("We are going to delete record by First Name")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    FName_SU = input("Please input First Name which you want to Delete:   ")
    Email_SU = input("Please input also Email which you want to Delete:   ")
    s = ' '
    count = 0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[0] != FName_SU and L[4]!=Email_SU):
                f_w.write(s)
             elif (L[0] == FName_SU and L[4]==Email_SU):
                  count = count + 1
    if count == 0:
       print("This data is not in our record which you want to delete Sorry!")
    else:
        print(FName_SU+"  Data is sucessfully deleted!")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
def DeleteContactByMobile():
    print("We are going to delete record by Mobile Number")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    Mobile_SU = input("Please input Mobile Number which you want to Delete:   ")
    Email_SU = input("Please input also Email which you want to Delete:   ")
    s = ' '
    count =0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[2] != Mobile_SU and L[4]!=Email_SU):
                f_w.write(s)
             elif (L[2] == Mobile_SU and L[4]==Email_SU):
                  count = count + 1
    if count == 0:
       print("This data is not in our record which you want to delete Sorry!")
    else:
        print(Mobile_SU +"  Data is sucessfully deleted!")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
def DeleteContactByCity():
    print("We are going to delete record by City")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    City_SU = input("Please input City which you want to Delete:   ")
    Email_SU = input("Please input also Email which you want to Delete:   ")
    s = ' '
    count = 0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[3] != City_SU and L[4]!=Email_SU):
                f_w.write(s)
             elif (L[3] == City_SU and L[4]==Email_SU):
                count = count + 1
    if count == 0:
       print(City_SU+" data is not in our record which you want to delete Sorry!")
    else:
        print(City_SU+"  Data is sucessfully deleted")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
def AllDeleteContactByName():
    print("We are going to delete record by First Name all similiar data")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    FName_SU = input("Please input First Name which you want to Delete:   ")
    s = ' '
    count =0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[0] != FName_SU):
                f_w.write(s)
             elif (L[0] == FName_SU):
                 count=count+1
    if count == 0:
       print("This data is not in our record which you want to delete Sorry!")
    else:
        print(FName_SU+"  all Data is sucessfully deleted")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
def AllDeleteContactByMobile():
    print("We are going to delete record by Mobile Number all similiar data")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    Mobile_SU = input("Please input Mobile Number which you want to Delete:   ")
    s = ' '
    count = 0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[2] != Mobile_SU):
                f_w.write(s)
             elif (L[2] == Mobile_SU):
                 count=count+1
    if count == 0:
       print("This data is not in our record which you want to delete Sorry!")
    else:
        print(Mobile_SU+" all Data is sucessfully Deleted!")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
def AllDeleteContactByCity():
    print("We are going to delete record by City all similiar data")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    City_SU = input("Please input City which you want to Delete:   ")
    s = ' '
    count =0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[3] != City_SU):
                f_w.write(s)

    if count == 0:
       print("This data is not in our record which you want to delete Sorry!")
    else:
        print(City_SU +" all Data is sucessfully Deleted!")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
def UpdateContact():
    print("We are going to dupdate record by First Name")
    f_r = open("Address Book.txt", mode='r')
    f_w = open("UpdateAddress Book.txt", mode='w')
    FName_SU = input("Please input name which you want to update:   ")
    s = ' '
    count =0
    while (s):
          s = f_r.readline()
          L = s.split(",")
          if len(s) > 0:
             if (L[0] == FName_SU):
                count = count + 1
                FName = input("Please Enter your First Name:  ")
                LName = input("Please Enter your Last Name:  ")
                Mb= input("Please Enter your Mobile Number :  ")
                City = input("Please Enter your City:  ")
                Email= input("Please Enter your Email:  ")
                Profession = input("Please Enter your Profession:  ")
                f_w.write(FName+"," +LName+"," +Mb+ "," + City + "," + Email + "," + Profession + '\n')
             else:
               f_w.write(s)
    if count == 0:
       print("This data is not in our record which you want to Update Sorry!")
    else:
        print(FName_SU+"  Data is sucessfully Updated!")
    f_r.close()
    f_w.close()
    os.remove("Address Book.txt")
    os.rename(r'E:\Semester 8\WEB\Labs\UpdateAddress Book.txt',"Address Book.txt")
AdressBook()
AdressBook()
AllDeleteContactByName()







