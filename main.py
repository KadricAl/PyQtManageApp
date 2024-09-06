import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QWidget, QTableWidget, QTableWidgetItem
from PyQt6.uic import loadUi
import mysql.connector as mc
import datetime


conn = mc.connect(database= 'btstest',
                  host= 'localhost',
                  username= 'root',
                  password= 'root')


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi('logReg.ui', self)
        self.login_btn.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.register_btn.clicked.connect(self.gotoregister)
        self.register = Register()
        self.window = MainWidget()


    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        cur = conn.cursor()
        query = (f'select email,password from editors where email = "{email}" and password = "{password}"')
        cur.execute(query)
        result = cur.fetchone()
        print(result)
        if result == None:
            dialog = QMessageBox(text="Incorrect email or password")
            dialog.setWindowTitle("Message")
            dialog.exec()
        else:
            dialog = QMessageBox(text="Logged successfully")
            dialog.setWindowTitle("Message")
            dialog.exec()

            self.close()
            self.window.show()




    def gotoregister(self):
        self.register.show()
        self.close()



class Register(QDialog):
    def __init__(self):
        super(Register,self).__init__()
        loadUi('Reg.ui', self)
        self.register_btn.clicked.connect(self.registerfunction)



    def registerfunction(self):
        fname = self.fname.text()
        lname = self.lname.text()
        email = self.email.text()
        self.login = Login()

        if self.password.text() == self.password2.text():
            password = self.password.text()
            cur = conn.cursor()
            query = (f'select email from editors where email = "{email}"')
            cur.execute(query)
            result = cur.fetchall()


            if str(result) == '[]':

                query = ('insert into editors(username, name, last_name, email, password) values(%s, %s, %s, %s, %s)')
                cur.execute(query, (fname, fname, lname, email, password))
                conn.commit()

                dialog = QMessageBox(text="Registered successfully")
                dialog.setWindowTitle("Message")
                dialog.exec()

                self.login.show()
                self.close()

            else:
                dialog = QMessageBox(text="User already exist")
                dialog.setWindowTitle("Message")
                dialog.exec()
        else:
            dialog = QMessageBox(text="Password Do Not Match")
            dialog.setWindowTitle("Message")
            dialog.exec()


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        loadUi('MainWidget.ui', self)
        self.show_btn.clicked.connect(self.show_all_func)
        self.show_table.clicked.connect(self.get_item)
        self.search_btn.clicked.connect(self.search_func)


    def get_item(self):
        row = self.show_table.currentRow()

        row_item_datum = self.show_table.item(row, 0).text()
        row_item_ibfu = self.show_table.item(row, 1).text()
        row_item_ibfm = self.show_table.item(row, 2).text()
        row_item_korisnik = self.show_table.item(row, 3).text()
        row_item_pj = self.show_table.item(row, 4).text()
        row_item_adresa = self.show_table.item(row, 5).text()
        row_item_grad = self.show_table.item(row, 6).text()
        row_item_datumzfm = self.show_table.item(row, 7).text()
        row_item_operater = self.show_table.item(row, 8).text()
        row_item_mail = self.show_table.item(row, 9).text()
        row_item_telefon = self.show_table.item(row, 10).text()
        row_item_id = self.show_table.item(row, 11).text()
        row_item_pdv = self.show_table.item(row, 12).text()
        row_item_iccid = self.show_table.item(row, 13).text()
        row_item_datumzif = self.show_table.item(row, 14).text()


        self.ibfu.setText(row_item_ibfu)
        self.ibfm.setText(row_item_ibfm)
        self.korisnik.setText(row_item_korisnik)
        self.poslovna_j.setText(row_item_pj)
        self.adresa.setText(row_item_adresa)
        self.datum.setText(row_item_datum)
        self.grad.setText(row_item_grad)
        self.datum_zfm.setText(row_item_datumzfm)
        self.operater.setText(row_item_operater)
        self.korisnik_mail.setText(row_item_mail)
        self.telefon.setText(row_item_telefon)
        self.id_num.setText(row_item_id)
        self.pdv_num.setText(row_item_pdv)
        self.iccid.setText(row_item_iccid)
        self.datum_zif.setText(row_item_datumzif)





    def show_all_func(self):
        cur = conn.cursor()
        query = ('select * from uredjaji')
        cur.execute(query)
        result = cur.fetchall()
        row = 0
        print(result)
        print(len(result[0]))
        self.show_table.setRowCount(len(result))
        for r in result:
            d = r[1]
            d = d.strftime('%d.%m.%Y')
            self.show_table.setItem(row, 0, QtWidgets.QTableWidgetItem(d))
            self.show_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r[2])))
            self.show_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r[3])))
            self.show_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r[15])))
            self.show_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(r[4])))
            self.show_table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(r[5])))
            self.show_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(r[6])))
            d2 = r[10]
            d2 = d2.strftime('%d.%m.%Y')
            self.show_table.setItem(row, 7, QtWidgets.QTableWidgetItem(d2))
            self.show_table.setItem(row, 8, QtWidgets.QTableWidgetItem(str(r[14])))
            self.show_table.setItem(row, 9, QtWidgets.QTableWidgetItem(str(r[8])))
            self.show_table.setItem(row, 10, QtWidgets.QTableWidgetItem(str(r[7])))
            self.show_table.setItem(row, 11, QtWidgets.QTableWidgetItem(str(r[12])))
            self.show_table.setItem(row, 12, QtWidgets.QTableWidgetItem(str(r[13])))
            self.show_table.setItem(row, 13, QtWidgets.QTableWidgetItem(str(r[9])))
            d3 = r[11]
            d3 = d3.strftime('%d.%m.%Y')
            self.show_table.setItem(row, 14, QtWidgets.QTableWidgetItem(d3))
            row += 1



    def search_func(self):
        search_word = self.search_lbl.text()
        cur = conn.cursor()
        query = (f'select * from uredjaji where ibfu like "%{search_word}%" or korisnik like "%{search_word}%"')
        cur.execute(query)
        result = cur.fetchall()
        row = 0
        print(result)
        print(len(result[0]))
        self.show_table.setRowCount(len(result))
        for r in result:
            d = r[1]
            d = d.strftime('%d.%m.%Y')
            self.show_table.setItem(row, 0, QtWidgets.QTableWidgetItem(d))
            self.show_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r[2])))
            self.show_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r[3])))
            self.show_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r[15])))
            self.show_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(r[4])))
            self.show_table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(r[5])))
            self.show_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(r[6])))
            d2 = r[10]
            d2 = d2.strftime('%d.%m.%Y')
            self.show_table.setItem(row, 7, QtWidgets.QTableWidgetItem(d2))
            self.show_table.setItem(row, 8, QtWidgets.QTableWidgetItem(str(r[14])))
            self.show_table.setItem(row, 9, QtWidgets.QTableWidgetItem(str(r[8])))
            self.show_table.setItem(row, 10, QtWidgets.QTableWidgetItem(str(r[7])))
            self.show_table.setItem(row, 11, QtWidgets.QTableWidgetItem(str(r[12])))
            self.show_table.setItem(row, 12, QtWidgets.QTableWidgetItem(str(r[13])))
            self.show_table.setItem(row, 13, QtWidgets.QTableWidgetItem(str(r[9])))
            d3 = r[11]
            d3 = d3.strftime('%d.%m.%Y')
            self.show_table.setItem(row, 14, QtWidgets.QTableWidgetItem(d3))
            row += 1


app = QApplication(sys.argv)

login = Login()
login.show()

sys.exit(app.exec())















