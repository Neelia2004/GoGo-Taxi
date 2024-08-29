# Importing necessary modules
import sqlite3
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import customer_login_Ui

# Connecting to the SQLite Database
join = sqlite3.connect('C:\\Users\\Aneelia Balraj\\Downloads\\taxi.db')
pointer = join.cursor()

# Defining customer_registration_Ui class
class customer_registration_Ui(object):
    def __init__(self, Word):
        super().__init__()
        self.Word = Word
        self.start_customer_dashboard(self.Word)

    # Showing the window
    def showing(self):
        self.Word.show()

    # Closing the window
    def closing(self):
        self.Word.close()


    # Inserting data into the database
    def enter_registration_data(self):
            pointer.execute(
            "INSERT INTO Customer (CustomerID, Password, FirstName, LastName, Address,  Email, ContactNumber,"
                     "PaymentMethod, Ccnumber ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
                    self.username_information.text(),
                    self.password_information.text(),
                    self.f_name_information.text(),
                    self.l_name_information.text(),
                    self.address_information.text(),
                    self.email_information.text(),
                    self.phoneno_information.text(),
                    self.payment_information.text(),
                    self.payment_information2.text()
                )
            )

            join.commit()
            self.successful_register_message()

    # Clicking submit button
    def submit_button_clicked(self):

            self.enter_registration_data()
            self.clear_information()

    # Display successful registration message
    def successful_register_message(self):
        QMessageBox.information(self.Word, 'Registration', "Successfully Registered", QMessageBox.StandardButton.Ok)

    # Clear populated fields
    def clear_information(self):
        self.username_information.clear()
        self.password_information.clear()
        self.f_name_information.clear()
        self.l_name_information.clear()
        self.address_information.clear()
        self.email_information.clear()
        self.phoneno_information.clear()
        self.payment_information.clear()
        self.payment_information2.clear()

    # Clicking the back button
    def back_button_clicked(self):
        self.closing()
        self.word = QtWidgets.QDialog()
        previous_screen = customer_login_Ui.Customer_Login_Ui(QtWidgets.QDialog())
        previous_screen.showing()

    # Selecting a combox
    def selecting_combobox(self):
        data = self.pay_dropdown_box.currentText()

        self.payment_information.setText(data)
        # self.status_box.count()

    # Setting up the UI Customer Registration page
    def start_customer_dashboard(self, mainPage):

        # Styling
        mainPage.setObjectName("mainPage")
        mainPage.resize(400, 520)
        self.styling = QtWidgets.QGraphicsView(mainPage)
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 580))
        self.styling.setStyleSheet("background-color: rgb(117, 81, 57);")
        self.styling.setObjectName("styling")

        # Customer registration label
        self.label_registration = QtWidgets.QLabel(mainPage)
        self.label_registration.setGeometry(QtCore.QRect(30, 30, 351, 40))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("Georgia")
        fontstyle.setPointSize(48)
        fontstyle.setBold(True)
        fontstyle.setWeight(75)
        self.label_registration.setFont(fontstyle)
        self.label_registration.setAutoFillBackground(False)
        self.label_registration.setStyleSheet("background-color: rgb(242, 237, 215);color: black;")
        self.label_registration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_registration.setWordWrap(True)
        self.label_registration.setObjectName("label_registration")

        # Submit button
        self.submit_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.submit_button_clicked())
        self.submit_button.setGeometry(QtCore.QRect(150, 370, 113, 32))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.submit_button.setFont(fontstyle)
        self.submit_button.setStyleSheet("border-radius: 25px;\n"
                                         "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                         "border: 2px solid #73AD21;\n"
                                         "background-color: rgb(242, 237, 215);\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border-color: rgb(4, 4, 4);")
        self.submit_button.setObjectName("submit_button")


        # Back button
        self.back_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.back_button_clicked())
        self.back_button.setGeometry(QtCore.QRect(20, 440, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.back_button.setFont(fontstyle)
        self.back_button.setStyleSheet("border-radius: 65px;\n"
                                       "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                       "border: 2px solid #73AD21;\n"
                                       "background-color: rgb(242, 237, 215);\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "border-color: rgb(4, 4, 4);")
        self.back_button.setObjectName("back_button")

        # Password label
        self.password_label = QtWidgets.QLabel(mainPage)
        self.password_label.setGeometry(QtCore.QRect(30, 137, 200, 30))
        self.password_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                        "color: rgb(56, 56, 56);")
        self.password_label.setObjectName("password_label")

        # Password text area
        self.password_information = QtWidgets.QLineEdit(mainPage)
        self.password_information.setGeometry(QtCore.QRect(160, 142, 200, 20))
        self.password_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.password_information.setObjectName("password_information")

        # Customer username label
        self.username_label = QtWidgets.QLabel(mainPage)
        self.username_label.setGeometry(QtCore.QRect(30, 105, 200, 30))
        self.username_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                             "color: rgb(56, 56, 56);")
        self.username_label.setObjectName("username_label")

        # Customer username area
        self.username_information = QtWidgets.QLineEdit(mainPage)
        self.username_information.setGeometry(QtCore.QRect(160, 110, 200, 20))
        self.username_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.username_information.setObjectName("username_information")

        # First name label
        self.f_name_label = QtWidgets.QLabel(mainPage)
        self.f_name_label.setGeometry(QtCore.QRect(30, 175, 200, 30))
        self.f_name_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                             "color: rgb(56, 56, 56);")
        self.f_name_label.setObjectName("f_name_label")

        # First name area
        self.f_name_information = QtWidgets.QLineEdit(mainPage)
        self.f_name_information.setGeometry(QtCore.QRect(160, 175, 200, 20))
        self.f_name_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.f_name_information.setObjectName("f_name_information")

        # Last name label
        self.l_name_label = QtWidgets.QLabel(mainPage)
        self.l_name_label.setGeometry(QtCore.QRect(30, 202, 200, 30))
        self.l_name_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                            "color: rgb(56, 56, 56);")
        self.l_name_label.setObjectName("l_name_label")

        # Last name area
        self.l_name_information = QtWidgets.QLineEdit(mainPage)
        self.l_name_information.setGeometry(QtCore.QRect(160, 207, 200, 20))
        self.l_name_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")

        # Address label
        self.address_label = QtWidgets.QLabel(mainPage)
        self.address_label.setGeometry(QtCore.QRect(30, 235, 200, 30))
        self.address_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                             "color: rgb(56, 56, 56);")
        self.address_label.setObjectName("address_label")

        # Address area
        self.address_information = QtWidgets.QLineEdit(mainPage)
        self.address_information.setGeometry(QtCore.QRect(160, 237, 200, 20))
        self.address_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")

        # Email label
        self.email_label = QtWidgets.QLabel(mainPage)
        self.email_label.setGeometry(QtCore.QRect(30, 266, 200, 30))
        self.email_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                             "color: rgb(56, 56, 56);")
        self.email_label.setObjectName("email_label")

        # Email area
        self.email_information = QtWidgets.QLineEdit(mainPage)
        self.email_information.setGeometry(QtCore.QRect(160, 268, 200, 20))
        self.email_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.email_information.setObjectName("email_information")

        # Phone number label
        self.phoneno_label = QtWidgets.QLabel(mainPage)
        self.phoneno_label.setGeometry(QtCore.QRect(30, 299, 101, 30))
        self.phoneno_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                       "color: rgb(56, 56, 56);")
        self.phoneno_label.setObjectName("phoneno_label")

        # Phone number area
        self.phoneno_information = QtWidgets.QLineEdit(mainPage)
        self.phoneno_information.setGeometry(QtCore.QRect(160, 300, 200, 20))
        self.phoneno_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.phoneno_information.setObjectName("phoneno_information")

        # Payment information area
        self.payment_information = QtWidgets.QLineEdit(mainPage)
        self.payment_information.setGeometry(QtCore.QRect(160, 332, 100, 20))
        self.payment_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.payment_information.setObjectName("payment_information")
        self.payment_information.setEnabled(False)

        # Payment information 2 area
        self.payment_information2 = QtWidgets.QLineEdit(mainPage)
        self.payment_information2.setGeometry(QtCore.QRect(260, 332, 100, 20))
        self.payment_information2.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                "color: rgb(56, 56, 56);\n"
                                                "background-color: rgb(242, 237, 215);")
        self.payment_information2.setObjectName("payment_information2")

        # Payment information dropdown box
        self.pay_dropdown_box = QtWidgets.QComboBox(mainPage)
        self.pay_dropdown_box.setGeometry(QtCore.QRect(30, 332, 91, 20))
        self.pay_dropdown_box.setObjectName("pay_dropdown_box")
        self.pay_dropdown_box.setStyleSheet("background-color:  rgb(242, 237, 215); color: black; ")
        self.pay_dropdown_box.addItem("")
        self.pay_dropdown_box.addItem("")
        self.pay_dropdown_box.activated.connect(self.selecting_combobox)
        self.update_text(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)

    # Making the information visible in the GUI
    def update_text(self, mainPage):
        update = QtCore.QCoreApplication.translate
        mainPage.setWindowTitle(update("mainPage", "Customer Registration"))
        self.label_registration.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\"font-weight:550; font-size:20pt;\">Customer Registration</span></p></body></html>"))
        self.password_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\" font-weight:550; color:#ffffff;\">Password</span></p></body></html>"))
        self.username_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\"font-weight:550;color:#ffffff\">Username</span></p></body></html>"))
        self.f_name_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\"font-weight:550; color:#ffffff;\">First Name</span></p></body></html>>"))
        self.l_name_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\"font-weight:550; color:#ffffff;\">Last Name</span></p></body></html>"))
        self.address_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\"font-weight:550; color:#ffffff;\">Address</span></p></body></html>"))
        self.email_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\" font-weight:550;color:#ffffff;\">Email</span></p></body></html>"))
        self.phoneno_label.setText(update("mainPage", "<html><head/><body><p>"
                    "<span style =\" font-weight:550; color:#ffffff;\">Phone No</span></p></body></html>"))
        self.address_label.setText(update("mainPage", "<html><head/><body><p>" 
                    "<span style =\" font-weight:550; color:#ffffff;\">Address</span></p></body></html>"))
        self.back_button.setText(update("mainPage", "Back"))
        self.submit_button.setText(update("mainPage", "Register"))
        self.pay_dropdown_box.setItemText(0, update("mainPage", "Credit"))
        self.pay_dropdown_box.setItemText(1, update("mainPage", "Debit"))

# Creating the entry point of the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QDialog()
    ui = customer_registration_Ui(mainPage)
    ui.showing()
    sys.exit(app.exec())
