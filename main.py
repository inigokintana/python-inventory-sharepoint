import wmi
import os

if __name__ == "__main__":
    
    pc = os.environ['COMPUTERNAME']
    print('PC name '+ pc)
                
    conn = wmi.WMI ("10.136.14.241", user=r"tttt", password="xxxx")
 
    print('OS is: {0}'.format(conn.Win32_OperatingSystem()[0].Caption))
    #print('Disk freespace {0} - total {1}'.format(c.Win32_LogicalDisk()[0].Freespace,c.Win32_LogicalDisk()[0].Size))
    print('Total Memory: {0}'.format(conn.Win32_ComputerSystem()[0].TotalPhysicalMemory))
 
    wql = "SELECT IPAddress FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = 'True'"
    print('Local IP address: {0}'.format(' - '.join(conn.query(wql)[0].IPAddress)))
    
    # Get Local Users and Groups
    for group in conn.Win32_Group():
       print(group.Caption)
    #for user in group.associators(wmi_result_class="Win32_UserAccount"):
    #    print(" [+]", user.Caption)
    
