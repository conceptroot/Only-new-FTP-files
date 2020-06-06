from ftplib import FTP
import time
import pprint
import os
from settings import *

ftp = FTP()
ftp.connect(FTP_HOST, FTP_PORT)
ftp.login(user = FTP_USER, passwd= FTP_PASSWD)
data = ftp.retrlines('LIST')

out = 'files/test.xlsx'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'EXT_op_kpi.XLSX', f.write)

data = []
ftp.dir(data.append)

def delete_all_files_on_ftp():
    pass
    print("Deleting all files in FTP")


import datetime


ftp_file_name_date = []
for line in data:
    # datestr = ' '.join(line.split()[3])
    file_name = line.split()[-1]
    now = datetime.datetime.now()
    if now.month == 1 and now.day == 1:
        delete_all_files_on_ftp()
    
    datestr =str(now.year)+' '.join(line.split()[5:8])
    orig_date = datetime.datetime.strptime(datestr, '%Y%b %d %H:%M')

    ftp_file_name_date.append((file_name, orig_date))

pprint.pprint(ftp_file_name_date)

print(os.listdir('files/'))
modi_time = os.path.getctime('files/test.xlsx')
print( time.ctime(modi_time))