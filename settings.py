import yaml
with open('secret.yaml') as f:
    sets = yaml.safe_load(f)
   
FTP_HOST = sets['FTP_HOST']
FTP_PORT = sets['FTP_PORT'] 
FTP_USER = sets['FTP_USER']
FTP_PASSWD = sets['FTP_PASSWD']