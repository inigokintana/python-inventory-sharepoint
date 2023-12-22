import wmi

if __name__ == "__main__":
    
    c = wmi.WMI ()
 
    print('OS is: {0}'.format(c.Win32_OperatingSystem()[0].Caption))
    #print('Disk freespace {0} - total {1}'.format(c.Win32_LogicalDisk()[0].Freespace,c.Win32_LogicalDisk()[0].Size))
    print('Total Memory: {0}'.format(c.Win32_ComputerSystem()[0].TotalPhysicalMemory))
 
    wql = "SELECT IPAddress FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = 'True'"
    print('Local IP address: {0}'.format(' - '.join(c.query(wql)[0].IPAddress)))