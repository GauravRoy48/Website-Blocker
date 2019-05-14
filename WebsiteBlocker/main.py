##################################################################################
# Creator     : Gaurav Roy
# Date        : 14 May 2019
# Description : The code contains code to read a file containing website names
#               and blocks them for a fixed duration. It does this by editing 
#               the C:\Windows\System32\drivers\etc\hosts file to redirect the 
#               intended websites to 127.0.0.1 and thus denying access.
##################################################################################

import pandas as pd
import time
from datetime import datetime as dt

hosts_file_loc = "C:\\Windows\\System32\\drivers\\etc\\hosts" # hosts file location
redirect_str = "127.0.0.1" # Redirect IP

# Variables holding the starting and ending times for blocking (24 hour format)
start_hour = 10 # Range: 0-23
start_min = 0 # Range: 0-59
end_hour = 16 # Range: 0-23
end_min = 0 # Range: 0-59

websites = list(pd.read_csv('blocked_sites.txt',header=None)[0])

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_hour,start_min) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour, end_min):
        with open(hosts_file_loc, 'r+') as file:
            content = file.read()
            for website in websites:
                if website not in content:
                    file.write(redirect_str+' '+website+'\n')
        
    else:
        with open(hosts_file_loc, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
                
    time.sleep(5)
