from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


# AES加密函数
def encrypt_data(data, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_data).decode('utf-8')


# AES解密函数
def decrypt_data(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted_data.decode('utf-8')
