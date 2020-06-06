from ftplib import FTP
import time
import pprint
import os
from settings import sets
import datetime

class OnlyNewFTPFilesGetter(object):
    def __init__(self, settings= sets):
        self._FTP_HOST = sets['FTP_HOST']
        self._FTP_PORT = sets['FTP_PORT']
        self._FTP_USER = sets['FTP_USER']
        self._FTP_PASSWD = sets['FTP_PASSWD']
        self._FTP_FOLDER = sets['FTP_FOLDER']
        self._ftp_connect()
        self._LOCAL_FOLDER = sets['LOCAL_FOLDER']

    def _ftp_connect(self):
        self._ftp = FTP()
        try:
            self._ftp.connect(self._FTP_HOST, self._FTP_PORT)
        except:
            print("can't connect to FTP")
        try:
            self._ftp.login(user = self._FTP_USER, passwd= self._FTP_PASSWD)
        except:
            print("can't login to FTP")

    def get_ftp_file_names_dates(self):
        if self._FTP_FOLDER:
            try:
                self._ftp.cwd(self._FTP_FOLDER)
            except:
                print(f"can't change FTP dirrectory {self._FTP_FOLDER}")
        data = []
        self._ftp.dir(data.append)
        ftp_file_name_date = []
        now = datetime.datetime.now()

        for line in data:
            file_name = line.split()[-1]
            if now.month == 1 and now.day == 1:
                pass
                # delete_all_files_on_ftp()
            datestr =str(now.year)+' '.join(line.split()[5:8])
            orig_date = datetime.datetime.strptime(datestr, '%Y%b %d %H:%M')

            ftp_file_name_date.append((file_name, orig_date))
        return ftp_file_name_date
    
    def get_local_file_names_dates(self):
        local_file_name_date = []
        if self._LOCAL_FOLDER:
            try:
                os.chdir(self._LOCAL_FOLDER)
            except:
                print(f"can't change local directory {self._LOCAL_FOLDER}")
        for each_file in os.listdir():
            modi_time = os.path.getctime(each_file)
            modif_date = datetime.datetime.fromtimestamp(modi_time)
            local_file_name_date.append((each_file, modif_date))
        return local_file_name_date

get_ftp = OnlyNewFTPFilesGetter()

print(get_ftp.get_ftp_file_names_dates())

print(get_ftp.get_local_file_names_dates())
