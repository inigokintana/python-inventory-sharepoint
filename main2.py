import os

if __name__ == "__main__":
    ip = input("IP del ordenador a consultar: ")
    
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
    
    #alternative
    #os.system(r"dir /o-d \\10.136.14.176\c$\Users\.")