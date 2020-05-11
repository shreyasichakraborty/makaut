# Text-based user interfaces (TUI), alternately terminal user interfaces, reflects dependence upon the properties of 
# computer terminals and not just text.
# It is a retronym parallel to the concept of graphical user interfaces (GUI). 
# Like GUIs, they may use the entire screen area and accept mouse and other inputs. 

# tui_meny.py is a Redhat Linux integrated Python project. It provides a range of options to the user to perfom task on 
# the linux terminal without having prior knowledge about linux commands.


import os
import getpass
os.system("tput setaf 2")
print("Launching TUI")
print("Enter your password: ")
password=getpass.getpass()

if(password!="1234"):
    print("Login Failed")
    exit()


os.system("tput setaf 1")
print("\t\t\t  WELCOME TO TUI\t\t\t")
os.system("tput setaf 7")
print("\t\t\t------------------")
location=int(input("Press 1.Local 2.Remote : "))
if location==1:
    print("Entering local device")
    while True:
        print("""
        1.Print date
        2.Print cal
        3.Configure web
        4.Configure docker
        5.Configure ssh
        6.Configure yum
        7.Add user
        8.Delete user
        9.Create a file
        10.Create a folder
        11.Exit""")

        ch=int(input("Enter your choice: "))

        if(ch==1):
            os.system("date")

        elif ch==2:
            os.system("cal")

        elif ch==3:
            os.system("yum install httpd -y")
            os.system("systemctl start httpd")
            os.system("systemctl status httpd")

        elif ch==4:
            os.system("yum install docker-ce -y")
            os.system("systemctl start docker")
            os.system("systemctl status docker")


        elif ch==7:
            new_user=input("Enter the name of new user")
            os.system("sudo useradd {}".format(new_user))
        
        elif ch==8:
            del_user=input("Enter the name of the user to delete")
            os.system("sudo userdel {}".format(del_user))

        elif ch==9:
            filename=input("Enter the filename")
            os.system("sudo touch {}".format(filename))
           
        elif ch==10:
            foldername=input("Enter the filename")
            os.system("sudo mkdir {}".format(foldername))
            

        elif ch==11:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")

        input("Press enter to continue")
        os.system("clear")

elif location==2:
    ip=input("Enter the IP of the remote device: ")
    p=os.system("ping -c 2 {}".format(ip))
    if(p!=0):
        print("IP not reachable")
        exit()
    print("Entering remote device")
    os.system("ssh-keygen")
    os.system("ssh-copy-id root@{}".format(ip))
    while True:
        print("""
        1.Print date
        2.Print cal
        3.Configure web
        4.Configure docker
        5.Configure ssh
        6.Configure yum
        7.Add user
        8.Delete user
        9.Create a file
        10.Create a folder
        11.Exit""")

        ch=int(input("Enter your choice: "))

        if(ch==1):
            os.system("ssh root@{} date".format(ip))

        elif ch==2:
            os.system("ssh root@{} cal".format(ip))

        elif ch==3:
            os.system("ssh root@{} yum install httpd -y".format(ip))
            os.system("ssh root@{} systemctl start httpd".format(ip))
            os.system("ssh root@{} systemctl status httpd".format(ip))

        elif ch==4:
            os.system("ssh root@{} yum install docker-ce -y".format(ip))
            os.system("ssh root@{} systemctl start docker".format(ip))
            os.system("ssh root@{} systemctl status docker".format(ip))
        
        elif ch==7:
            new_user=input("Enter the name of new user: ")
            os.system("ssh {} useradd {}".format(ip,new_user))
        
        elif ch==8:
            del_user=input("Enter the name of the user to delete: ")
            os.system("ssh {} userdel {}".format(ip,del_user))

        elif ch==9:
            filename=input("Enter the filename")
            os.system("ssh root@{} touch {}".format(ip,filename))
           
        elif ch==10:
            foldername=input("Enter the filename")
            os.system("ssh root@{} mkdir {}".format(ip,foldername))
            
        elif ch==11:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")

        input("Press enter to continue")
        os.system("clear")


else:
    print("Invalid location")
    

        
    
