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
        self.register_button = QPushButton('Register')

        layout.addWidget(QLabel('Username:'))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel('Password:'))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.login_button.clicked.connect(self.on_login)
        self.register_button.clicked.connect(self.show_register_dialog)

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

    def show_register_dialog(self):
        register_dialog = RegisterDialog(self)
        if register_dialog.exec() == QDialog.accepted:
            # Implement your logic to handle successful registration if needed
            pass


class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Register')

        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton('Register')

        layout.addWidget(QLabel('Username:'))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel('Password:'))
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)

        self.register_button.clicked.connect(self.on_register)

        self.setLayout(layout)

    def on_register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Add your registration logic here. For example, store the user credentials.
        # For demonstration purposes, we just close the register dialog with QDialog.Accepted.
        self.accept()


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
    if login_dialog.exec() == QDialog.accepted:
        main_window = MainWindow()
        main_window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
