# Only-new-FTP-files
This script checks local files and only gets new files from FTP server.

## Usage
put secret.yaml file to root dir:

    FTP_HOST: 'xxx.xxx.xxx.xxx'
    FTP_PORT: 22 
    FTP_USER: 'ftp_user'
    FTP_PASSWD: 'ftp_pass'
    FTP_FOLDER: 'ftp_folder'  # or leave blank to use root dir
    LOCAL_FOLDER: 'local_folder' # or leave blank to use root dir

Create OnlyNewFTPFilesGetter class object.
And run update_local_files() method

    ftp = OnlyNewFTPFilesGetter()
    ftp.update_local_files()

## Folders
p.s. (be aware)

    script gets modification time in FTP folder. 
    script gets creation time in local folder. 
## TODO
1. Add logger
2. Add filter to _get_ftp_file_names_dates. To filter out directiories in output
3. Add last year files logic. Right now FTP don't give information about year of file creation. So it could cause problems, when january comes.