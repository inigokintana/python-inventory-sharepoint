import os
import subprocess

def inputPing():
    ip = input("IP o nombre del ordenador a consultar: ")
    response = os.system("ping -n 1 " + ip)
    #and then check the response...
    if response == 0:
        print(f"{ip} is up!")
    else:
        print(f"{ip} is down!")
        print("**************************")
        print("**************************")
    
    return response,ip

def inputPing2():
    hostname = "10.20.16.30"
    output = subprocess.Popen(["ping.exe",hostname],stdout = subprocess.PIPE).communicate()[0]

    print(output)

    if ('unreachable' in output):
        print("Offline")
    
def checkUser(ip):
    # r is for raw string
    # we compose the path for the Users directory with the active profiles
    users= r"\\" + ip + r"\c$\Users\."
    
    # we change actual dir to remote environment
    os.chdir(users)
    
    # we listir . remote environment
    # we list only dirs -> isdir
    # array indexed by getmtype
    # reverse -> most actual is first - [0] we get the 1st one only
    print("Ultimo usuario activo en PC: " + sorted(filter(os.path.isdir, os.listdir('.')), key=os.path.getmtime, reverse = True)[0])
    print("**************************")
    print("**************************")
    
    #alternative
    #os.system(r"dir /o-d \\10.136.14.176\c$\Users\.")

if __name__ == "__main__":
    while True:
        response,ip = inputPing()
        if response == 0:
            checkUser(ip)
    