import sys
from PyQt6 import QtCore, QtGui, QtWidgets

import customer_login_Ui
import administration_login
import driver_loginUi

class Taxi_Main_Page_Ui(QtWidgets.QDialog):
    def __init__(self, Word):
        super().__init__()
        self.Word = Word
        self.begin_Ui_creation(self.Word)

# creating constructors to open and close screen
    def showing(self):
        self.Word.show()

    def closing(self):
        self.Word.close()

# clicking the customer button
    def customer_button_clicked(self):
        self.closing()
        self.Word = QtWidgets.QDialog()
        customer_page = customer_login_Ui.Customer_Login_Ui(QtWidgets.QDialog())
        customer_page.showing()


# clicking admin button
    def admin_button_clicked(self):
        self.closing()
        self.Word = QtWidgets.QDialog()
        administration_login_page = administration_login.admin_login_window(QtWidgets.QDialog())
        administration_login_page.showing()



# clicking driver button
    def driver_button_clicked(self):
        self.closing()
        self.Word = QtWidgets.QDialog()
        driver_window = driver_loginUi.Driver_Login_Ui(QtWidgets.QDialog())
        driver_window.showing()

    def begin_Ui_creation(self, mainPage):
        mainPage.setObjectName("mainPage")
        mainPage.resize(400, 360)
        self.styling = QtWidgets.QGraphicsView(mainPage)
        self.styling.setStyleSheet("background-color:rgb(117, 81, 57);")
        self.styling.setObjectName("Styling")
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 360))


        self.Title = QtWidgets.QLabel(mainPage)
        self.Title.setGeometry(QtCore.QRect(30, 20, 351, 101))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("Georgia")
        fontstyle.setBold(True)
        fontstyle.setWeight(75)
        fontstyle.setPointSize(48)
        self.Title.setFont(fontstyle)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("background-color:rgb(242, 237, 215); color: black;")
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setWordWrap(True)
        self.Title.setObjectName("Title")

    # administrator button
        self.administrator_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.admin_button_clicked())
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("Trebuchet MS")
        self.administrator_button.setFont(fontstyle)
        self.administrator_button.setGeometry(QtCore.QRect(145, 240, 113, 32))
        self.administrator_button.setStyleSheet("border-radius: 25px;\n"
                                                "border: 2px solid #404040;\n"
                                                "color: rgb(0, 0, 0);\n"
                                                "border-color: rgb(4, 4, 4);"
                                                "background-color: rgb(242, 237, 215);\n")
        self.administrator_button.setObjectName("administrator_button")

    # customer button
        self.customer_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.customer_button_clicked())
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("Trebuchet MS")
        self.customer_button.setFont(fontstyle)
        self.customer_button.setGeometry(QtCore.QRect(145, 190, 113, 32))
        self.customer_button.setStyleSheet("border-radius: 25px;\n"
                                                "border: 2px solid #73AD21;\n"
                                                "color: rgb(0, 0, 0);\n"
                                                "border-color: rgb(4, 4, 4);"
                                                "background-color: rgb(242, 237, 215);\n")
        self.customer_button.setObjectName("customer_button")

    # driver button
        self.driver_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.driver_button_clicked())
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(18)
        fontstyle.setFamily("Trebuchet MS")
        self.driver_button.setFont(fontstyle)
        self.driver_button.setGeometry(QtCore.QRect(145, 290, 113, 32))
        self.driver_button.setStyleSheet("border-radius: 25px;\n"
                                                "border: 2px solid #73AD21;\n"
                                                "color: rgb(0, 0, 0);\n"
                                                "border-color: rgb(4, 4, 4);"
                                                "background-color: rgb(242, 237, 215);\n")
        self.driver_button.setObjectName("driver_button")

        self.Title_2 = QtWidgets.QLabel(mainPage)
        fontstyle = QtGui.QFont()
        fontstyle.setPointSize(48)
        fontstyle.setFamily("Trebuchet MS")
        fontstyle.setBold(True)
        fontstyle.setWeight(75)
        self.Title_2.setFont(fontstyle)
        self.Title_2.setAutoFillBackground(False)
        self.Title_2.setGeometry(QtCore.QRect(70, 130, 260, 30))
        self.Title_2.setStyleSheet("border-radius: 25px;\n"
                                    "border: 0px solid #73AD21;\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(242, 237, 215);\n")
        self.Title_2.setWordWrap(True)
        self.Title_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title_2.setObjectName("Title_2")

        self.update_ui(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)

    def update_ui(self, mainPage):
        update_titles = QtCore.QCoreApplication.translate
        mainPage.setWindowTitle(update_titles("mainPage", "Welcome to the GoGoTaxi System!!!"))
        self.Title.setText(update_titles("mainPage", "<html><head/><body><p><span style=\" font - size: 20pt;\">GoGoTaxi!</span></p></body></html>"))
        self.administrator_button.setText(update_titles("mainPage", "Admin"))
        self.customer_button.setText(update_titles("mainPage", "Customer"))
        self.driver_button.setText(update_titles("mainPage", "Driver"))
        self.Title_2.setText(update_titles("mainPage", "<html><head/><body><p><span style=\" font-size:20pt; color: black;\ font-weight:400;\">Login or Register</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QDialog()
    ui = Taxi_Main_Page_Ui(mainPage)
    ui.showing()
    sys.exit(app.exec())