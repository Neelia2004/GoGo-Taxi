from PyQt6 import QtCore, QtGui, QtWidgets
import UI
import sys
from PyQt6.QtWidgets import QMessageBox
import sqlite3
import admin_dashboard


connection = sqlite3.connect('C:\\Users\\Aneelia Balraj\\Downloads\\taxi.db')
pointer = connection.cursor()
class admin_login_window(object):
    def __init__(self, Word):
        super().__init__()
        self.Word = Word
        self.start_administration_login(self.Word)

    def showing(self):
        self.Word.show()

    def closing(self):
        self.Word.close()

    def admin_button_clicked(self):
        if self.email_Information.text() in self.obtain_information().__str__():
            self.Word = QtWidgets.QDialog()
            admin_window = admin_dashboard.administration_dashboard(QtWidgets.QDialog())
            admin_window.showing()
            self.closing()

        else:
            self.error_message_login()

    def back_button_clicked(self):
        self.closing()
        self.Word = QtWidgets.QDialog
        mainPage = UI.Taxi_Main_Page_Ui(QtWidgets.QDialog())
        mainPage.showing()

    def obtain_information(self):
        pointer.execute("SELECT * FROM Admin WHERE password =:password",
                  {'password': self.password_information.text()})

        return pointer.fetchall()

    def error_message_login(self):
        ret = QMessageBox.warning(self.Word, 'Forgot Password', "Invalid Email and/or Password?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,         QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Yes:
            print("Yes was clicked")
        elif ret == QMessageBox.StandardButton.Cancel:
            self.email_Information.clear()
            self.password_information.clear()
            print("Cancel was clicked and fields are now cleared")

    def start_administration_login(self, mainAdminPage):
        mainAdminPage.setObjectName("mainAdminPage")
        mainAdminPage.resize(400, 500)
        self.styling = QtWidgets.QGraphicsView(mainAdminPage)
        self.styling.setStyleSheet("background-color: rgb(117, 81, 57);")
        self.styling.setObjectName("styling")
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 500))

        self.administration_login_label = QtWidgets.QLabel(mainAdminPage)
        self.administration_login_label.setGeometry(QtCore.QRect(30, 20, 351, 101))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("Georgia")
        fontstyle.setWeight(75)
        fontstyle.setPointSize(48)
        fontstyle.setBold(True)
        self.administration_login_label.setFont(fontstyle)
        self.administration_login_label.setAutoFillBackground(False)
        self.administration_login_label.setStyleSheet("background-color: rgb(242, 237, 215); color: black;")
        self.administration_login_label.setWordWrap(True)
        self.administration_login_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.administration_login_label.setObjectName("administration_login_label")

        self.administration_login_button = QtWidgets.QPushButton(mainAdminPage, clicked=lambda: self.admin_button_clicked())
        self.administration_login_button.setGeometry(QtCore.QRect(150, 330, 113, 32))
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("STIX Two Text")
        self.administration_login_button.setFont(fontstyle)
        self.administration_login_button.setStyleSheet("border-radius: 25px;\n"
                                                       "border: 2px solid #73AD21;\n"
                                                       "background-color: rgb(242, 237, 215);\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "border-color: rgb(4, 4, 4);")
        self.administration_login_button.setObjectName("administration_login_button")

        self.password_information = QtWidgets.QLineEdit(mainAdminPage)
        self.password_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);\n"
                                                "\n""\n""\n")
        self.password_information.setGeometry(QtCore.QRect(110, 270, 200, 20))
        self.password_information.setObjectName("password_information")

        self.password_information.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.emailLabel = QtWidgets.QLabel(mainAdminPage)
        self.emailLabel.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                             "color: rgb(56, 56, 56);")
        self.emailLabel.setGeometry(QtCore.QRect(110, 180, 80, 30))
        self.emailLabel.setObjectName("emailLabel")

        self.passwordLabel= QtWidgets.QLabel(mainAdminPage)
        self.passwordLabel.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                    "color: rgb(56, 56, 56);\n")
        self.passwordLabel.setGeometry(QtCore.QRect(120, 240, 80, 30))
        self.passwordLabel.setObjectName("passwordLabel")

        self.email_Information = QtWidgets.QLineEdit(mainAdminPage)
        self.email_Information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);\n"
                                                "\n""\n""\n")
        self.email_Information.setGeometry(QtCore.QRect(110, 210, 200, 20))
        self.email_Information.setObjectName("email_Information")

        self.forget_password_button = QtWidgets.QPushButton(mainAdminPage)
        self.forget_password_button.setGeometry(QtCore.QRect(110, 380, 200, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("STIX Two Text")
        self.forget_password_button.setFont(fontstyle)
        self.forget_password_button.setStyleSheet("border-radius: 25px;\n"
                                           "border: 2px solid #73AD21;\n"
                                           "background-color: rgb(242, 237, 215);\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-color: rgb(4, 4, 4);")
        self.forget_password_button.setObjectName("forget_password_button")

        self.Back_Button = QtWidgets.QPushButton(mainAdminPage, clicked=lambda: self.back_button_clicked())
        self.Back_Button.setGeometry(QtCore.QRect(10, 460, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setWeight(9)
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        self.Back_Button.setFont(fontstyle)
        self.Back_Button.setStyleSheet("border-radius: 65px;\n"
                                           "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                           "border: 2px solid #73AD21;\n"
                                           "background-color: rgb(242, 237, 215);\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-color: rgb(4, 4, 4);")

        self.Back_Button.setObjectName("Back_Button")

        self.updateUi(mainAdminPage)
        QtCore.QMetaObject.connectSlotsByName(mainAdminPage)

    def updateUi(self, mainAdminPage):
        update = QtCore.QCoreApplication.translate

        mainAdminPage.setWindowTitle(update("mainAdminPage", "Admin Login"))
        self.administration_login_label.setText(update("mainAdminPage", "<html><head/><body><p><span style =\" font-size:35pt;\">Admin Login</span></p></body></html>"))
        self.administration_login_button.setText(update("mainAdminPage", "Login"))
        self.emailLabel.setText(update("mainAdminPage", "<html><head/><body><p><span style =\" font-weight:600; color:#ffffff;\">Username</span></p></body></html>"))
        self.passwordLabel.setText(update("mainAdminPage", "<html><head/><body><p><span style =\" font-weight:600; color:#ffffff;\">Password</span></p></body></html>"))
        self.forget_password_button.setText(update("mainAdminPage", "Forget Password"))
        self.Back_Button.setText(update("mainAdminPage", "Back"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QDialog()
    ui = admin_login_window(mainPage)
    ui.showing()
    sys.exit(app.exec())



















