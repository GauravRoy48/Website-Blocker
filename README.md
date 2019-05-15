# Website-Blocker
Python code to restrict access to user provided websites for given amount of time. 
For test purposes, the code should be run using command line instead of the GUI of Spyder IDE.

- User must find the hosts file in C:\Windows\System32\drivers\etc\ and edit the hosts file to have a new line after the last '127.0.0.1...' line. If not done, the code will keep adding new lines over days and increase the file size by 2 bytes everytime.
- User must enter list of websites in blocked_sites.txt.
- User must edit the main.pyw to change the 'start_hour', 'start_min', 'end_hour' and 'end_min' to accomodate their own blocking timings.
- User must edit the main.bat to correct the directory of the main.pyw file.
- User must run the main.bat file with admin privileges to run it successfully.

Spyder IDE used.
