import wmi
import os
from getpass import getpass

if __name__ == "__main__":
    ip = input("IP del ordenador a consultar: ")
    usertext = input("tu usuario de EJ: ")
    pwdtext = getpass("password: ")
    
    conn = wmi.WMI (ip, user=usertext, password=pwdtext)
    #conn = wmi.WMI ("10.136.14.241", user=r"xxx", password="xxx")
    #conn = wmi.WMI ()
    
    for system in conn.Win32_ComputerSystem():
        print(system)
        print('PC name '+ system.Name)
        print('PC Manufacturer '+ system.Manufacturer)
        print('PC Model '+ system.Model)
 

    print('OS is: {0}'.format(conn.Win32_OperatingSystem()[0].Caption))
    #print('Disk freespace {0} - total {1}'.format(c.Win32_LogicalDisk()[0].Freespace,c.Win32_LogicalDisk()[0].Size))
    print('Total Memory: {0}'.format(conn.Win32_ComputerSystem()[0].TotalPhysicalMemory))
 
    wql = "SELECT IPAddress FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = 'True'"
    print('Local IP address: {0}'.format(' - '.join(conn.query(wql)[0].IPAddress)))

    #os.listdir(r"//" + ip + "/c$/Usuarios/.") - no funciona
    #os.listdir(r"\\10.136.14.176\c$\Users\.")
    #list(filter(os.path.isdir, os.listdir(r"\\10.136.14.176\c$\Users\.")))
    #dir /o-d \\10.136.14.176\c$\Users\.
    
    os.chdir(r"\\10.136.14.176\c$\Users\.")
    sorted(filter(os.path.isdir, os.listdir('.')), key=os.path.getmtime, reverse = True)[0]
    
    #alternative
    os.system(r"dir /o-d \\10.136.14.176\c$\Users\.")
    
    # Get Local Users and Groups
    #for group in conn.Win32_Group():
    #   print(group.Caption)
    #for user in group.associators(wmi_result_class="Win32_UserAccount"):
    #    print(" [+]", user.Caption)
    
