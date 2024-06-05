from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

class FileEncryptor:
    def __init__(self, password: str):
        self.password = password.encode()
        self.backend = default_backend()
        self.salt = os.urandom(16)

    def derive_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=self.backend
        )
        return kdf.derive(self.password)

    def encrypt_file(self, input_file: str, output_file: str):
        key = self.derive_key()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()

        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            f_out.write(self.salt)
            f_out.write(iv)
            while chunk := f_in.read(1024):
                f_out.write(encryptor.update(chunk))
            f_out.write(encryptor.finalize())

    def decrypt_file(self, input_file: str, output_file: str):
        with open(input_file, 'rb') as f_in:
            self.salt = f_in.read(16)
            key = self.derive_key()
            iv = f_in.read(16)
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=self.backend)
            decryptor = cipher.decryptor()

            with open(output_file, 'wb') as f_out:
                while chunk := f_in.read(1024):
                    f_out.write(decryptor.update(chunk))
                f_out.write(decryptor.finalize())
