from Cryptodome.Cipher import DES
import binascii
def main():
    key = b'abcdefgh'
    des = DES.new(key,DES.MODE_ECB)
    encrypto_res = b'1627381823y1278hfc7178237671863'

    encryt_text = binascii.a2b_hex(encrypto_res) #将十六进制的字节串转换为二进制的，与上面的函数差别在a2b
    decrypt_res = des.decrypt(encryt_text)
    print(decrypt_res)
    pass
if __name__ == '__main__':
    main()