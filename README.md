# Only-new-FTP-files
This script checks local files and only gets new files from FTP server.

## Folders
1. LOCAL_FOLDER - local folder. Script gets date of creation of all files in this folder. And then compare it with files, that located on FTP server.
2. FTP_FOLDER - FTP folder

p.s. (be aware)

    script gets modification time in FTP folder. 
    script gets creation time in local folder. 
## TODO
1. Add logger
2. 