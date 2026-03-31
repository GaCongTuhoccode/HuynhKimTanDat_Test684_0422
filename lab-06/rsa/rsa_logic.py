import sys
from PyQt5 import QtWidgets
from rsa_cipher import Ui_RSA_Cipher 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

class RSA_App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RSA_Cipher()
        self.ui.setupUi(self)
        self.private_key = None
        self.public_key = None

       
        self.ui.btn_generate_keys.clicked.connect(self.generate_keys)
        self.ui.btn_encrypt.clicked.connect(self.encrypt_message)
        self.ui.btn_decrypt.clicked.connect(self.decrypt_message)

    def generate_keys(self):
       
        key = RSA.generate(2048)
        self.private_key = key
        self.public_key = key.publickey()
        pub_pem = self.public_key.export_key().decode()
        
        self.ui.txt_information.setPlainText(f"Keys Generated!\n\nPublic Key snippet:\n{pub_pem[:100]}...")

    def encrypt_message(self):
        if not self.public_key:
            self.ui.txt_information.setPlainText("Lỗi: Hãy nhấn 'Generate Keys' trước!")
            return
        
        message = self.ui.txt_plain_text.toPlainText().encode()
        cipher_rsa = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher_rsa.encrypt(message)
        
        self.ui.txt_cipher_text.setPlainText(binascii.hexlify(ciphertext).decode())

    def decrypt_message(self):
        if not self.private_key:
            return
        try:
           
            ciphertext = binascii.unhexlify(self.ui.txt_cipher_text.toPlainText())
            cipher_rsa = PKCS1_OAEP.new(self.private_key)
            plaintext = cipher_rsa.decrypt(ciphertext)
            
            self.ui.txt_plain_text.setPlainText(plaintext.decode())
        except Exception as e:
            self.ui.txt_information.setPlainText(f"Lỗi giải mã: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RSA_App()
    window.show()
    sys.exit(app.exec_())