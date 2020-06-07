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
        self._cwd_ftp()
        self._cwd_local() 
        # self._ftp_files = self._get_ftp_file_names_dates()
        # self._local_files = self._get_local_file_names_dates()

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

    def _cwd_ftp(self):
        if self._FTP_FOLDER:
            try:
                self._ftp.cwd(self._FTP_FOLDER)
            except:
                print(f"can't change FTP dirrectory {self._FTP_FOLDER}")

    def _get_ftp_file_names_dates(self) -> dict:
        data = []
        self._ftp.dir(data.append)
        ftp_file_name_date = {} 
        now = datetime.datetime.now()

        for line in data:
            file_name = line.split()[-1]
            if now.month == 1 and now.day == 1:
                pass
                # delete_all_files_on_ftp()
            datestr =str(now.year)+' '.join(line.split()[5:8])
            orig_date = datetime.datetime.strptime(datestr, '%Y%b %d %H:%M')
            ftp_file_name_date[file_name] = orig_date
        # print(f"ls of folder[{self._FTP_FOLDER}]:\n{ftp_file_name_date}")
        return ftp_file_name_date
    
    def _cwd_local(self):
        if self._LOCAL_FOLDER:
            try:
                os.chdir(self._LOCAL_FOLDER)
            except:
                print(f"can't change local directory {self._LOCAL_FOLDER}")

    def _get_local_file_names_dates(self) -> dict:
        local_file_name_date = {} 
        for each_file in os.listdir():
            modi_time = os.path.getctime(each_file)
            modif_date = datetime.datetime.fromtimestamp(modi_time)
            local_file_name_date[each_file] = modif_date
        return local_file_name_date

    def _get_ftp_download_list(self):
        download_list=[]
        ftp_files = self._get_ftp_file_names_dates()
        local_files = self._get_local_file_names_dates()
        for each_ftp_file in ftp_files:
            if local_files.get(each_ftp_file, False):
                # print(self._local_files.get(each_ftp_file, False))
                # print(f"date ftp {self._ftp_files[each_ftp_file]}")
                # print(f"date local {self._local_files[each_ftp_file]}")
                # print(self._ftp_files[each_ftp_file]- self._local_files[each_ftp_file])
                if ftp_files.get(each_ftp_file) > local_files.get(each_ftp_file):
                    print(f"file on FTP {each_ftp_file} is newer than local")
                    download_list.append(each_ftp_file)
            else:
                # print(f"file {each_ftp_file} not exist")
                download_list.append(each_ftp_file)
        return download_list
    
    def update_local_files(self):
        update_list = self._get_ftp_download_list()
        for each in update_list:
            print(f"trying to download {each}...")
            try:
                with open(each, 'wb') as f:
                    self._ftp.retrbinary('RETR ' + each, f.write)
            except:
                print(f"can't download or write {each}")

get_ftp = OnlyNewFTPFilesGetter()


get_ftp.update_local_files()