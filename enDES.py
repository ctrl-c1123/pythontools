from Cryptodome.Cipher import DES
import binascii #提供了进制和ASCII码的转换
def main():
    key = b'abcdefgh' #密码长度必须是8位
    des = DES.new(key,DES.MODE_ECB)
    text = "haha123 nihao"
    text = text+(8-(len(text)%8))*'='
    print(text) # haha123 nihao===
    encrypt_text = des.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text) #binascii.b2a_hex将二进制的字节串转为16进制
    pass
if __name__ == '__main__':
    main()