import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')

        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton('Login')

        layout.addWidget(QLabel('Username:'))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel('Password:'))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.on_login)

        self.setLayout(layout)

    def on_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Add your login logic here. Check if the credentials are valid.
        # For example:
        if username == 'admin' and password == 'password':
            self.accept()  # Closes the dialog with QDialog.Accepted
        else:
            self.username_input.clear()
            self.password_input.clear()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Secondary Window')
        self.layout = QVBoxLayout()
        self.label = QLabel('Welcome to the secondary window!')
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


def main():
    app = QApplication(sys.argv)

    login_dialog = LoginDialog()
    if login_dialog.exec() == QDialog.Accepted:
        main_window = MainWindow()
        main_window.show()
        login_dialog.close()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
