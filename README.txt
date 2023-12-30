                                                                      e4t3m4ll
        						                               PYTHON MALWARE PROJECT
The Python Malware Project for the Prestigious Winter Of Code 6.0. The Complete Software consists of four Python Scripts. 
1. Brain.py
2. Parasite.py
3. Receiver.py
4. Sender.py


Brain.py - As the name suggests, this python script is the master of code execution on the victim machine, the Parasite file is converted to a nonconsole executable which would 
           be delivered to the victim server as a payload. Parasite when executed on the victim server will start to establish connection with the Brain.py python execution   
           which works on our server. The connection is established using the socket module where Brain and Parasite are connected using the same port on Attcking server and then 
           provides us Information about the victim and allows us to execute commands on the victim file system. This is the basic Backdoor software.
           The Commands which can be executed on the victim file system-
           1. cd - which helps us navigate through the file system of victim. Syntax - Bash Syntax
           2. upload - This command helps us to upload a file to the victim server remotely. Syntax - upload filename (Or path/to/file)
           3. download - This command helps us to download a file from the victim server into our server. Syntax - download filename (Or path/to/filename)
           4. dir - This command lists the contents of the present working directory. Command - dir
           5. quit - To break the connection.

Parasite.py - As the name suggests, This file infiltrates the host, and creating a backdoor which receives and executes the commands from the server with the help of json and 
              and subprocess modules respectively. The connection is established by socket module. The script is converted to an executable by the 
              "pyinstaller Parasite.py --onefile --noconsole" command in windows terminal. which can then be infiltrated into the system by hiding the executable in an image or an email.

Sender.py - This is the script which is made into an executable using pyinstaller in windows terminal. This script sends out signals using the socket module to a listening 
            machine, which is our server, this script basically uses the watchdog module and defines functions in order to monitor changes made in the victim file system by 
            the owner of that server and it pings and redirects the message about the changes to a text file on the attcking server or the client server.

Receiver.py - This script is executed on the attacking server ( mind before the victim executes the Sender script ). The command listens to connections sent by the machine 
              executing the Sender python script and redirects the path of the pings to a text file in our home directory.
                                     



                                     All in all the four scripts combined make up all the features which were asked in the Problem Statement
                                     with appropriate monitoring and snatching privilages 
                                     Where on nour server we would have to open two consoles of terminal one executing the Brain.py and the other 
                                     executing the Receiver.py
                                     both of the scripts use different ports from our server which we ensured that were open. So there is essentially 
                                     no discrepancy in running both the scripts successfully.
                                     since we are using the backdoor malware we need not worry about firewall for the most part and the malware is practically
                                     non malicious when scanned by an anti-virus software.
                                     while the Parasite and the Sender scripts run on the victim server. 


              (In all the cases while pentesting with the Software it is better to run the scripts on the main/attcking server before executing them on the victim file system.
              also the scripts were written according to the Local IP address of my attacking virtual machine, So they have to be changed before establishing connections)


Possible Future Additions and Shortcomings in the project:

1. The termination of payload when it is disconnected from the attacking server:
               The executable running in the background of the client/victim shuts itself when the connection from the host/attcking server is closed with the quit command.
               Currently I could not find a better way to keep the script running, because of lack of complete understanding of the socket library and networking using python
2. The lack of potency of the malware;
               Currently the software when we use it, the persistence of the scripts running on the server would not work on system restart and can still be detected by a very 
               vigilant user of the victim server 
3. The dynamic changes onto downloaded files:
               The script could also be made so that it updated the already downloaded files on the attcking server, That it updates the changes made into the counterpart of that 
               file onto the client/victim server. so that we would not have to download a file yet again.
4. The availability of downloading only pre existing files:
               The download command in our script, seems to only download files which were already existing onto the client system and files created during the script couldn't b
               downloaded which seems a bit trickier and I couldn't find it in the time gap.    

                                                                   I have also provided the Injector.py script which would inject any binary file/executable into a JPG/JPEG image with 
                                                                   The help of python.     



                                The executable and image can also be combined using the Winrar 
                                software and the file can be used as an executable on it's own.  

