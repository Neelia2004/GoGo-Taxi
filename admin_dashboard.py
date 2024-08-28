import sqlite3
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
import random
import string
import sys
import administration_login

join = sqlite3.connect('C:\\Users\\Aneelia Balraj\\Downloads\\taxi.db')
pointer = join.cursor()

class administration_dashboard(object):
    def __init__(self, Word):
        super().__init__()
        self.Word = Word
        self.start_admin_dashboard(self.Word)

    def showing(self):
        self.Word.show()

    def closing(self):
        self.Word.close()

    def enter_booking_data(self):
        join.execute("INSERT INTO Booking VALUES( :BookingID,:Date, "
                     ":PickupTime, :PickupAddress, :DropAddress, :Paid, :Status)",
                     {'BookingID': self.travel_Id.text(), 'Date': self.pickup_date_information.text(),
                      'PickupTime': self.Time_of_pickup_information.text(),
                      'PickupAddress': self.Address_of_pickup_information.text(), 'DropAddress':
                          self.Address_of_dropoff_information.text(), 'Paid': self.payment_information.text(),
                      'Status': self.status_information.text()})

    def add_button_clicked(self):
        self.enter_booking_data()
        join.commit()
        self.clear_information()
        join.close()

    def clear_information(self):
        self.travel_Id.clear()
        self.pickup_date_information.clear()
        self.Time_of_pickup_information.clear()
        self.Address_of_pickup_information.clear()
        self.Address_of_dropoff_information.clear()
        self.payment_information.clear()
        self.status_information.clear()
        self.booked_confirmation_message()

    def clear_updated_information(self):
        self.travel_Id.clear()
        self.pickup_date_information.clear()
        self.Time_of_pickup_information.clear()
        self.Address_of_pickup_information.clear()
        self.Address_of_dropoff_information.clear()
        self.payment_information.clear()
        self.status_information.clear()
        self.updated__confirmation_message()


    def clear_text(self):
        self.search_travel_id_text.clear()

    def booked_confirmation_message(self):
        QMessageBox.question(self.Word, 'Booking', "Booked Successfully!!",QMessageBox.Yes | QMessageBox.Yes)

    def updated__confirmation_message(self):
        QMessageBox.question(self.Word, 'Booking', "Updated Successfully",QMessageBox.Yes | QMessageBox.Yes)

    def obtain_booking_information(self):
        join.execute("SELECT * FROM Booking WHERE BookingID =:BookingID",
                  {'BookingID': self.search_travel_id_text.text()})

        return join.fetchall()

    def search_button_clicked(self):
        pass
        if self.search_travel_id_text.text() in self.obtain_booking_information().__str__():
            self.enter_text()

    def enter_text(self):
        give_it = self.obtain_booking_information()

        print(give_it[0][0])
        self.travel_Id.setText((give_it[0][0]))
        self.pickup_date_information.setText((give_it[0][1]))
        self.Time_of_pickup_information.setText((give_it[0][2]))
        self.Address_of_pickup_information.setText((give_it[0][3]))
        self.Address_of_dropoff_information.setText((give_it[0][4]))
        self.payment_information.setText((give_it[0][5]))
        self.status_information.setText((give_it[0][6]))
        self.clear_text()

    def deletebooking(self):
        join.execute("DELETE FROM Booking WHERE BookingID =:BookingID", {'BookingID': self.travel_Id.text()})

    def clear_deleted_information(self):
        self.travel_Id.clear()
        self.pickup_date_information.clear()
        self.Time_of_pickup_information.clear()
        self.Address_of_pickup_information.clear()
        self.Address_of_dropoff_information.clear()
        self.Address_of_dropoff_information.clear()
        self.status_information.clear()
        self.delete_information()

    def delete_information(self):
        QMessageBox.question(self.Word, 'Booking', "Deleted Successfully!!", QMessageBox.Yes | QMessageBox.Yes)

    def delete_button_clicked(self):
        self.deletebooking()

        join.commit()
        # join.close()
        self.clear_deleted_information()

    def update_booking(self):

        join.execute(""" UPDATE Booking SET Date = :Date,
            PickupTime =:PickupTime,
            PickupAddress =:PickupAddress, DropAddress =:DropAddress,
            Paid =:Paid,
            Status =:Status 
            WHERE BookingID =:BookingID""",
                     {'BookingID': self.travel_Id.text(),
                      'Date': self.pickup_date_information.text(),
                      'PickupTime': self.Time_of_pickup_information.text(),
                      'PickupAddress': self.Address_of_pickup_information.text(),
                      'DropAddress': self.Address_of_dropoff_information.text(),
                      'Paid': self.payment_information.text(),
                      'Status': self.status_information.text()})

    def updateBooking_button_clicked(self):
        self.update_booking()

        join.commit()
        # join.close()
        self.clear_updated_information()

    def back_button_clicked(self):
        self.closing()
        self.word = QtWidgets.QDialog()
        previous_screen = administration_login.admin_login_window(QtWidgets.QDialog())
        previous_screen.showing()

    def generate_travel_id_clicked(self):
        password = []
        for n in range(2):
            letter_random = random.choice(string.ascii_letters)
            nummer_random = random.choice(string.digits)
            password.append(letter_random)
            password.append(nummer_random)
            k = "".join(str(x) for x in password)
            self.travel_Id.setText(f"{k}")

    def selecting_combobox(self):
        data = self.status_combobox.currentText()

        self.status_information.setText(data)
        # self.status_box.count()

    def select_combobox(self):
        data = self.pay_dropdown_box.currentText()

        self.payment_information.setText(data)
        # self.status_cBox.count()

    def start_admin_dashboard(self, mainPage):
        mainPage.setObjectName("mainPage")

        mainPage.resize(400, 580)
        self.styling = QtWidgets.QGraphicsView(mainPage)
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 580))
        self.styling.setStyleSheet("background-color: rgb(117, 81, 57);")
        self.styling.setObjectName("styling")

        self.booking_label = QtWidgets.QLabel(mainPage)
        self.booking_label.setGeometry(QtCore.QRect(30, 30, 351, 40))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("Georgia")
        fontstyle.setPointSize(48)
        fontstyle.setBold(True)
        fontstyle.setWeight(75)
        self.booking_label.setFont(fontstyle)
        self.booking_label.setAutoFillBackground(False)
        self.booking_label.setStyleSheet("background-color: rgb(242, 237, 215); color:black;")
        self.booking_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.booking_label.setWordWrap(True)
        self.booking_label.setObjectName("booking_label")

        # add button
        self.add_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.add_button_clicked())
        self.add_button.setGeometry(QtCore.QRect(290, 400, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.add_button.setFont(fontstyle)
        self.add_button.setStyleSheet("border-radius: 25px;\n"
                                      "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                      "border: 2px solid #73AD21;\n"
                                      "background-color: rgb(242, 237, 215);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-color: rgb(4, 4, 4);")
        self.add_button.setObjectName("add_button")

        # Back Button
        self.back_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.back_button_clicked())
        self.back_button.setGeometry(QtCore.QRect(20, 540, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.back_button.setFont(fontstyle)
        self.back_button.setStyleSheet("border-radius: 65px;\n"
                                       "font: 75 16pt \"MS Shell Dlg 2\";\n"""
                                       "border: 2px solid #73AD21;\n"
                                       "background-color: rgb(242, 237, 215);\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "border-color: rgb(4, 4, 4);")
        self.back_button.setObjectName("back_button")

        self.first_name_label = QtWidgets.QLabel(mainPage)
        self.first_name_label.setGeometry(QtCore.QRect(30, 233, 101, 30))
        self.first_name_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                            "color: rgb(56, 56, 56);")
        self.first_name_label.setObjectName("first_name_label")

        self.last_name_label = QtWidgets.QLabel(mainPage)
        self.last_name_label.setGeometry(QtCore.QRect(30, 263, 121, 30))
        self.last_name_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                           "color: rgb(56, 56, 56);")
        self.last_name_label.setObjectName("last_name_label")

        self.Time_of_pickup_information = QtWidgets.QLineEdit(mainPage)
        self.Time_of_pickup_information.setGeometry(QtCore.QRect(160, 240, 200, 20))
        self.Time_of_pickup_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                      "color: rgb(56, 56, 56);\n"
                                                      "background-color: rgb(242, 237, 215);\n"
                                                      "\n""\n""\n")
        self.Time_of_pickup_information.setObjectName("Time_of_pickup_information")

        self.Address_of_pickup_information = QtWidgets.QLineEdit(mainPage)
        self.Address_of_pickup_information.setGeometry(QtCore.QRect(160, 270, 200, 20))
        self.Address_of_pickup_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                         "color: rgb(56, 56, 56);\n"
                                                         "background-color: rgb(242, 237, 215);\n"
                                                         "\n""\n""\n")
        self.Address_of_pickup_information.setObjectName("Address_of_pickup_information")

        self.username_label = QtWidgets.QLabel(mainPage)
        self.username_label.setGeometry(QtCore.QRect(30, 200, 101, 30))
        self.username_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                          "color: rgb(56, 56, 56);")
        self.username_label.setObjectName("username_label")

        self.pickup_date_information = QtWidgets.QLineEdit(mainPage)
        self.pickup_date_information.setGeometry(QtCore.QRect(160, 210, 200, 20))
        self.pickup_date_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                   "color: rgb(56, 56, 56);\n"
                                                   "background-color: rgb(242, 237, 215);\n"
                                                   "\n""\n""\n")
        self.pickup_date_information.setObjectName("pickup_date_information")

        self.address_label = QtWidgets.QLabel(mainPage)
        self.address_label.setGeometry(QtCore.QRect(30, 293, 121, 30))
        self.address_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                         "color: rgb(56, 56, 56);")
        self.address_label.setObjectName("address_label")

        self.Address_of_dropoff_information = QtWidgets.QLineEdit(mainPage)
        self.Address_of_dropoff_information.setGeometry(QtCore.QRect(160, 300, 200, 20))
        self.Address_of_dropoff_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                          "color: rgb(56, 56, 56);\n"
                                                          "background-color: rgb(242, 237, 215);\n"
                                                          "\n""\n""\n")
        self.Address_of_dropoff_information.setObjectName("Address_of_dropoff_information")

        self.status_information = QtWidgets.QLineEdit(mainPage)
        self.status_information.setGeometry(QtCore.QRect(160, 360, 100, 20))
        # self.status_Txt.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.status_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                              "color: rgb(56, 56, 56);\n"
                                              "background-color: rgb(242, 237, 215);\n"
                                              "\n""\n""\n""")
        self.status_information.setObjectName("status_information")
        self.status_information.setEnabled(False)

        # S Combo box
        self.status_combobox = QtWidgets.QComboBox(mainPage)
        self.status_combobox.setGeometry(QtCore.QRect(30, 360, 91, 20))
        self.status_combobox.setObjectName("status_combobox")
        self.status_combobox.setStyleSheet("background-color:  rgb(242, 237, 215); color: black; ")
        self.status_combobox.addItem("")
        self.status_combobox.addItem("")
        self.status_combobox.addItem("")
        self.status_combobox.addItem("")
        self.status_combobox.activated.connect(self.selecting_combobox)

        # G Button
        self.generate_travel_id_button = QtWidgets.QPushButton(mainPage,clicked=lambda: self.generate_travel_id_clicked())
        self.generate_travel_id_button.setGeometry(QtCore.QRect(30, 173, 120, 20))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(11)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.generate_travel_id_button.setFont(fontstyle)
        self.generate_travel_id_button.setStyleSheet("border-radius: 25px;\n"
                                                     "border: 2px solid #73AD21;\n"
                                                     "background-color: rgb(242, 237, 215);\n"
                                                     "color: rgb(0, 0, 0);\n"
                                                     "border-color: rgb(4, 4, 4);\n"
                                                     "font: 75 11pt \"MS Shell Dlg 2\";")
        self.generate_travel_id_button.setObjectName("generate_travel_id_button")

        self.travel_Id = QtWidgets.QLineEdit(mainPage)
        self.travel_Id.setGeometry(QtCore.QRect(160, 173, 120, 20))
        self.travel_Id.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                     "color: rgb(56, 56, 56);\n"
                                     "background-color: rgb(242, 237, 215);\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "")
        self.travel_Id.setObjectName("travel_Id")
        self.travel_Id.setEnabled(False)

        # Search Button
        self.search_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.search_button_clicked())
        self.search_button.setGeometry(QtCore.QRect(300, 90, 91, 31))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(11)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.search_button.setFont(fontstyle)
        self.search_button.setStyleSheet("border-radius: 25px;\n"
                                         "border: 2px solid #73AD21;\n"
                                         "background-color: rgb(242, 237, 215);\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border-color: rgb(4, 4, 4);\n"
                                         "font: 75 11pt \"MS Shell Dlg 2\";")
        self.search_button.setObjectName("search_button")

        self.trip_id_label = QtWidgets.QLabel(mainPage)
        self.trip_id_label.setGeometry(QtCore.QRect(320, 120, 40, 25))
        self.trip_id_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                         "font: 10pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(170, 0, 0);")
        self.trip_id_label.setObjectName("trip_id_label")

        self.search_travel_id_text = QtWidgets.QLineEdit(mainPage)
        self.search_travel_id_text.setGeometry(QtCore.QRect(300, 140, 91, 31))
        self.search_travel_id_text.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                                 "color: rgb(56, 56, 56);\n"
                                                 "background-color: rgb(242, 237, 215);\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.search_travel_id_text.setObjectName("search_travel_id_text")

        # D Button
        self.delete_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.delete_button_clicked())
        self.delete_button.setGeometry(QtCore.QRect(290, 470, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.delete_button.setFont(fontstyle)
        self.delete_button.setStyleSheet("border-radius: 65px;\n"
                                         "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                         "border: 2px solid #73AD21;\n"
                                         "background-color: rgb(242, 237, 215);\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border-color: rgb(4, 4, 4);")
        self.delete_button.setObjectName("delete_button")

        # U Button
        self.update_button = QtWidgets.QPushButton(mainPage, clicked=lambda: self.updateBooking_button_clicked())
        self.update_button.setGeometry(QtCore.QRect(290, 435, 100, 30))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("MS Shell Dlg 2")
        fontstyle.setPointSize(16)
        fontstyle.setBold(False)
        fontstyle.setItalic(False)
        fontstyle.setWeight(9)
        self.update_button.setFont(fontstyle)
        self.update_button.setStyleSheet("border-radius: 65px;\n"
                                         "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                         "border: 2px solid #73AD21;\n"
                                         "background-color: rgb(242, 237, 215);\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border-color: rgb(4, 4, 4);")
        self.update_button.setObjectName("update_button")

        self.payment_information = QtWidgets.QLineEdit(mainPage)
        self.payment_information.setGeometry(QtCore.QRect(160, 330, 100, 20))
        self.payment_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                               "color: rgb(56, 56, 56);\n"
                                               "background-color: rgb(242, 237, 215);\n"
                                               "\n""\n""\n""")
        self.payment_information.setObjectName("pay_Txt")
        self.payment_information.setEnabled(False)

        # Payment
        self.pay_dropdown_box = QtWidgets.QComboBox(mainPage)
        self.pay_dropdown_box.setGeometry(QtCore.QRect(30, 330, 91, 20))
        self.pay_dropdown_box.setObjectName("pay_dropdown_box")
        self.pay_dropdown_box.setStyleSheet("background-color:  rgb(242, 237, 215); color: black; ")
        self.pay_dropdown_box.addItem("")
        self.pay_dropdown_box.addItem("")
        self.pay_dropdown_box.activated.connect(self.select_combobox)
        self.update_booking()
        QtCore.QMetaObject.connectSlotsByName(mainPage)

        self.update_text(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)

    def update_text(self, mainPage):
        update = QtCore.QCoreApplication.translate

        mainPage.setWindowTitle(update("mainPage", "Admin Dashboard"))
        self.booking_label.setText(update("mainPage",
                                          "<html><head/><body><p><span style =\"font-weight:550; font-size:20pt;\">Admin Dashboard</span></p></body></html>"))
        self.add_button.setText(update("mainPage", "Add"))
        self.back_button.setText(update("mainPage", "Back"))
        self.first_name_label.setText(update("mainPage",
                                             "<html><head/><body><p><span style =\"font-weight:550; color:#ffffff;\">Pick up Time</span></p></body></html>"))
        self.last_name_label.setText(update("mainPage",
                                            "<html><head/><body><p><span style =\" font-weight:550;color:#ffffff;\">Pick up Address</span></p></body></html>"))
        self.username_label.setText(update("mainPage",
                                           "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">Pick up Date</span></p></body></html>"))
        self.address_label.setText(update("mainPage",
                                          "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">Drop off Address</span></p></body></html>"))
        self.status_combobox.setItemText(0, update("mainPage", "Status"))
        self.status_combobox.setItemText(1, update("mainPage", "Active"))
        self.status_combobox.setItemText(2, update("mainPage", "Completed"))
        self.status_combobox.setItemText(3, update("mainPage", "Cancel"))
        self.generate_travel_id_button.setText(update("mainPage", "Get Travel ID"))
        self.search_button.setText(update("mainPage", "Search"))
        self.trip_id_label.setText(update("mainPage",
                                          "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">T ID</span></p></body></html>"))
        self.delete_button.setText(update("mainPage", "Delete"))
        self.update_button.setText(update("mainPage", "Update"))
        self.pay_dropdown_box.setItemText(0, update("mainPage", "Credit"))
        self.pay_dropdown_box.setItemText(1, update("mainPage", "Debit"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QDialog()
    ui = administration_dashboard(mainPage)
    ui.showing()
    sys.exit(app.exec())