import sys
from PyQt5 import QtWidgets
from railfence_cipher import RailFenceCipher 

class RailFenceApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.cipher = RailFenceCipher()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Rail Fence Cipher UI - May CHAN")
        self.resize(450, 350)
        layout = QtWidgets.QVBoxLayout()

        # Nhập văn bản
        layout.addWidget(QtWidgets.QLabel("Văn bản (Plain Text / Cipher Text):"))
        self.txt_input = QtWidgets.QTextEdit()
        layout.addWidget(self.txt_input)

        # Nhập số đường ray (Key)
        layout.addWidget(QtWidgets.QLabel("Số đường ray (Key/Rails):"))
        self.spin_key = QtWidgets.QSpinBox()
        self.spin_key.setRange(2, 10)
        self.spin_key.setValue(3)
        layout.addWidget(self.spin_key)

        # Các nút chức năng
        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_encrypt = QtWidgets.QPushButton("Mã hóa")
        self.btn_decrypt = QtWidgets.QPushButton("Giải mã")
        btn_layout.addWidget(self.btn_encrypt)
        btn_layout.addWidget(self.btn_decrypt)
        layout.addLayout(btn_layout)

        # Kết quả
        layout.addWidget(QtWidgets.QLabel("Kết quả:"))
        self.txt_output = QtWidgets.QTextEdit()
        self.txt_output.setReadOnly(True)
        layout.addWidget(self.txt_output)

        self.setLayout(layout)

        # Kết nối sự kiện
        self.btn_encrypt.clicked.connect(self.handle_encrypt)
        self.btn_decrypt.clicked.connect(self.handle_decrypt)

    def handle_encrypt(self):
        text = self.txt_input.toPlainText()
        key = self.spin_key.value()
        if text:
            result = self.cipher.rail_fence_encrypt(text, key)
            self.txt_output.setText(result)

    def handle_decrypt(self):
        text = self.txt_input.toPlainText()
        key = self.spin_key.value()
        if text:
            result = self.cipher.rail_fence_decrypt(text, key)
            self.txt_output.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())