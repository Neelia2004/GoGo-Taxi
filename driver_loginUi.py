# Importing necessary modules
from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt6.QtWidgets import QMessageBox
import sys
import UI
import driver_dashboard

# Connecting to the SQLite Database
connection = sqlite3.connect('C:\\Users\\Aneelia Balraj\\Downloads\\taxi.db')
pointer = connection.cursor()

# Defining Driver_Login_Ui class
class Driver_Login_Ui(object):
    def __init__(self, Word):
        super().__init__()
        self.Word = Word
        self.start_Ui_driver_login(self.Word)

    # Showing the window
    def showing(self):
        self.Word.show()

    # Closing the window
    def closing(self):
        self.Word.close()

    # Clicking the login button
    def driver_login_button_clicked(self):
        if self.username_details.text() in self.obtain_information().__str__():
            self.Word = QtWidgets.QDialog()
            driver_window = driver_dashboard.driver_dashboard_Ui(QtWidgets.QDialog())
            driver_window.showing()
            self.closing()

        else:
            self.error_message_login()

    # Pulling information from the database
    def obtain_information(self):
        pointer.execute('SELECT * FROM TaxiDriver WHERE password = ?',
                        (self.password_details.text(),))

        return pointer.fetchall()

    # Login error message
    def error_message_login(self):
        ret = QMessageBox.warning(self.Word, 'Forgot Password', "Invalid Email and/or Password?",
                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
                                  QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Yes:
            print("Yes was clicked")
        elif ret == QMessageBox.StandardButton.Cancel:
            self.username_details.clear()
            self.password_details.clear()
            print("Cancel was clicked and fields are now cleared")

    # Clicking the back button
    def back_button_clicked(self):
        self.closing()
        self.Word = QtWidgets.QDialog()
        mainPage = UI.Taxi_Main_Page_Ui(QtWidgets.QDialog())
        mainPage.showing()

    # Setting up the UI Driver login page
    def start_Ui_driver_login(self, mainPage):

        # Styling
        mainPage.setObjectName("mainPage")
        mainPage.resize(400, 500)
        self.styling = QtWidgets.QGraphicsView(mainPage)
        self.styling.setStyleSheet("background-color: rgb(117, 81, 57);")
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.styling.setObjectName("graphicsView")


        # Driver login label
        self.driver_login_label = QtWidgets.QLabel(mainPage)
        self.driver_login_label.setGeometry(QtCore.QRect(30, 20, 351, 101))
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(48)
        fontstyle.setWeight(75)
        fontstyle.setBold(True)
        fontstyle.setFamily("Georgia")
        self.driver_login_label.setFont(fontstyle)
        self.driver_login_label.setAutoFillBackground(False)
        self.driver_login_label.setStyleSheet("background-color: rgb(242, 237, 215); color: black;")
        self.driver_login_label.setWordWrap(True)
        self.driver_login_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.driver_login_label.setObjectName("driver_login_label")

        # Driver login button
        self.driver_login_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.driver_login_button_clicked())
        self.driver_login_button.setGeometry(QtCore.QRect(150, 330, 113, 32))
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("STIX Two Text")
        self.driver_login_button.setFont(fontstyle)
        self.driver_login_button.setStyleSheet("border-radius: 25px;\n"
                                            "border: 2px solid #73AD21;\n"
                                            "background-color: rgb(242, 237, 215);\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "border-color: rgb(4, 4, 4);")
        self.driver_login_button.setObjectName("driver_login_button")

        # Back button
        self.back_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.back_button_clicked())
        self.back_button.setGeometry(QtCore.QRect(10, 460, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("STIX Two Text")
        self.back_button.setFont(fontstyle)
        self.back_button.setStyleSheet("border-radius: 25px;\n"
                                               "border: 2px solid #73AD21;\n"
                                               "background-color: rgb(242, 237, 215);\n"
                                               "color: rgb(0, 0, 0);\n"
                                               "border-color: rgb(4, 4, 4);")
        self.back_button.setObjectName("back_button")


        # Password text area
        self.password_details = QtWidgets.QLineEdit(mainPage)
        self.password_details.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);n")
        self.password_details.setGeometry(QtCore.QRect(110, 270, 200, 20))
        self.password_details.setObjectName("password_details")

        self.password_details.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Password label
        self.password_label = QtWidgets.QLabel(mainPage)
        self.password_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                    "color: rgb(56, 56, 56);")
        self.password_label.setGeometry(QtCore.QRect(110, 240, 80, 30))
        self.password_label.setObjectName("password_label")

        # Driver username label
        self.dusername_label = QtWidgets.QLabel(mainPage)
        self.dusername_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                           "color: rgb(56, 56, 56);")
        self.dusername_label.setGeometry(QtCore.QRect(110, 180, 80, 30))
        self.dusername_label.setObjectName("dusername_label")

        # Driver username area
        self.username_details = QtWidgets.QLineEdit(mainPage)
        self.username_details.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.username_details.setGeometry(QtCore.QRect(110, 210, 200, 20))
        self.username_details.setObjectName("username_details")

        # Forget Password Button
        self.forget_password_button = QtWidgets.QPushButton(mainPage)
        self.forget_password_button.setGeometry(QtCore.QRect(110, 375, 200, 30))
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

        self.updateUi(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)

    # Making the information visible in the GUI
    def updateUi(self, mainPage):
            update = QtCore.QCoreApplication.translate

            mainPage.setWindowTitle(update("mainPage", "Driver Login"))
            self.driver_login_label.setText(update("mainPage", "<html><head/><body><p>"
                                "<span style =\" font-size:35pt;\">Driver Login</span></p></body></html>"))
            self.forget_password_button.setText(update("mainPage", "Forget Password"))
            self.driver_login_button.setText(update("mainPage", "Login"))
            self.back_button.setText(update("mainPage", "Back"))
            self.dusername_label.setText(update("mainPage", "<html><head/><body><p>"
                                "<span style =\" font-weight:600; color:#ffffff;\">User ID</span></p></body></html>"))
            self.password_label.setText(update("mainPage", "<html><head/><body><p>"
                                "<span style =\" font-weight:600; color:#ffffff;\">Password</span></p></body></html>"))

# Creating the entry point of the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QDialog()
    ui = Driver_Login_Ui(mainPage)
    ui.showing()
    sys.exit(app.exec())











