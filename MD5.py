from hashlib import md5
def main():
    s = 'admin'
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    print(new_md5.hexdigest())
    pass
if __name__ == '__main__':
    main()