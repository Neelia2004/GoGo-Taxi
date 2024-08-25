import sqlite3
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import driver_loginUi
import UI



join = sqlite3.connect('Yellow_Express.db') # Creates the actual database
sql = join.cursor() # Takes data to and from database
sql.execute(""" CREATE TABLE if not exists Booking(
trip_iD text ,
pick_up_date text,
pick_up_time text,
pick_up_address text,
drop_off_address text,
pay_method text,
status text
)""")

class driver_dashboard_Ui(object):

    def __init__(self, Word):
        self.Word = QtWidgets.QDialog()
        self.start_driver_dashboard(self.Word)


    def showing(self):
        self.Word.show()

    def closing(self):
        self.Word.close()

    def obtain_booking_information(self):
        sql.execute("SELECT * FROM Booking WHERE trip_id =:trip_id",
                  {'trip_id': self.travel_ID_information.text()})
        return sql.fetchall()

    def search_button_clicked(self):
        if self.travel_ID_information.text() in self.obtain_booking_information().__str__():
            self.enter_information()

    def enter_information(self):
            insert = self.obtain_booking_information()
            print(insert[0][0])
            self.travel_Id.setText((insert[0][0]))
            self.Date_of_pickup_information.setText((insert[0][1]))
            self.Time_of_pickup_information.setText((insert[0][2]))
            self.Address_of_pickup_information.setText((insert[0][3]))
            self.Address_of_dropoff_information.setText((insert[0][4]))
            self.payment_information.setText((insert[0][5]))
            self.status_information.setText((insert[0][6]))

    def update_booking_information(self):
        sql.execute(""" UPDATE Booking SET trip_id = :trip_id, pick_up_date = :pick_up_date, pick_up_time =:pick_up_time,pick_up_address =:pick_up_address, drop_off_address =:drop_off_address,
    pay_method =:pay_method,
    status =:status WHERE
    travel_Id =:trip_id""",
    {'trip_id': self.travel_Id.text(), 'pick_up_date': self.Date_of_pickup.text(),'pick_up_time': self.Time_of_pickup_information.text(),'pick_up_address': self.Address_of_pickup_information.text(), 'drop_off_address':self.Address_of_dropoff_information.text(),'pay_method': self.payment_information.text(),'status': self.status_information.text()})

    def update_button_clicked(self):
        self.update_booking_information()
        join.commit()
        # join.close()
        # self.clearupdate_Txt()

    def back_button_clicked(self):
        self.word = QtWidgets.QDialog()
        previous_screen = driver_loginUi.Driver_Login_Ui(QtWidgets.QDialog())
        previous_screen.showing()
        self.closing()

    def combobox_selected(self):
        word2 = self.combobox_status_changed().currentText()

        self.status_information.setText(word2)
        # self.status_cBox.count()

    def start_driver_dashboard(self, mainPage):
        mainPage.setObjectName("mainFrame")

        mainPage.resize(400, 520)
        self.styling = QtWidgets.QGraphicsView(mainPage)
        self.styling.setGeometry(QtCore.QRect(0, 0, 400, 520))
        self.styling.setStyleSheet("background-color: rgb(117, 81, 57);")
        self.styling.setObjectName("styling")

        self.label_booking = QtWidgets.QLabel(mainPage)
        self.label_booking.setGeometry(QtCore.QRect(30, 30, 351, 40))
        fontstyle = QtGui.QFont()
        fontstyle.setFamily("Georgia")
        fontstyle.setPointSize(48)
        fontstyle.setBold(True)
        fontstyle.setWeight(75)
        self.label_booking.setFont(fontstyle)
        self.label_booking.setAutoFillBackground(False)
        self.label_booking.setStyleSheet("background-color: rgb(242, 237, 215);color: black;")
        self.label_booking.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_booking.setWordWrap(True)
        self.label_booking.setObjectName("label_booking")


        #back button
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

        self.pickup_time_label = QtWidgets.QLabel(mainPage)
        self.pickup_time_label.setGeometry(QtCore.QRect(30, 233, 101, 30))
        self.pickup_time_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                            "color: rgb(56, 56, 56);")
        self.pickup_time_label.setObjectName("pickup_time_label")

        self.pickup_address_label = QtWidgets.QLabel(mainPage)
        self.pickup_address_label.setGeometry(QtCore.QRect(30, 263, 121, 30))
        self.pickup_address_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                      "color: rgb(56, 56, 56);")
        self.pickup_address_label.setObjectName("pickup_address_label")

        self.Time_of_pickup_information = QtWidgets.QLineEdit(mainPage)
        self.Time_of_pickup_information.setGeometry(QtCore.QRect(160, 240, 200, 20))
        self.Time_of_pickup_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                         "color: rgb(56, 56, 56);\n"
                                         "background-color: rgb(242, 237, 215);\n"
                                         "\n""\n""\n""")
        self.Time_of_pickup_information.setObjectName("Time_of_pickup_information")
        self.Time_of_pickup_information.setEnabled(False)

        self.Address_of_pickup_information = QtWidgets.QLineEdit(mainPage)
        self.Address_of_pickup_information.setGeometry(QtCore.QRect(160, 270, 200, 20))
        self.Address_of_pickup_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                        "color: rgb(56, 56, 56);\n"
                                        "background-color: rgb(242, 237, 215);\n"
                                        "\n""\n""\n""")
        self.Address_of_pickup_information.setObjectName("Address_of_pickup_information")
        self.Address_of_pickup_information.setEnabled(False)

        self.pickup_date_label = QtWidgets.QLabel(mainPage)
        self.pickup_date_label.setGeometry(QtCore.QRect(30, 200, 101, 30))
        self.pickup_date_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                        "color: rgb(56, 56, 56);")
        self.pickup_date_label.setObjectName("pickup_date_label")

        self.Date_of_pickup = QtWidgets.QLineEdit(mainPage)
        self.Date_of_pickup.setGeometry(QtCore.QRect(160, 210, 200, 20))
        self.Date_of_pickup.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                         "color: rgb(56, 56, 56);\n"
                                         "background-color: rgb(242, 237, 215);\n"
                                         "\n""\n""\n""")
        self.Date_of_pickup.setObjectName("Date_of_pickup")
        self.Date_of_pickup.setEnabled(False)

        self.label_of_address = QtWidgets.QLabel(mainPage)
        self.label_of_address.setGeometry(QtCore.QRect(30, 293, 121, 30))
        self.label_of_address.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                       "color: rgb(56, 56, 56);")
        self.label_of_address.setObjectName("address_Lab")

        self.Address_of_dropoff_information = QtWidgets.QLineEdit(mainPage)
        self.Address_of_dropoff_information.setGeometry(QtCore.QRect(160, 300, 200, 20))
        self.Address_of_dropoff_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                        "color: rgb(56, 56, 56);\n"
                                        "background-color: rgb(242, 237, 215);\n"
                                        "\n""\n""\n""")
        self.Address_of_dropoff_information.setObjectName("Address_of_dropoff_information")
        self.Address_of_dropoff_information.setEnabled(False)

        self.status_information = QtWidgets.QLineEdit(mainPage)
        self.status_information.setGeometry(QtCore.QRect(160, 330, 100, 20))
        self.status_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                      "color: rgb(56, 56, 56);\n"
                                      "background-color: rgb(242, 237, 215);\n"
                                      "\n""\n""\n""")
        self.status_information.setObjectName("status_information")
        self.status_information.setEnabled(False)


        ###
        self.status_dropdown_box = QtWidgets.QComboBox(mainPage)
        self.status_dropdown_box.setGeometry(QtCore.QRect(30, 330, 91, 20))
        self.status_dropdown_box.setObjectName("status_dropdown_box")
        self.status_dropdown_box.setStyleSheet("background-color:  rgb(242, 237, 215); color: black; ")
        self.status_dropdown_box.addItem("")
        self.status_dropdown_box.addItem("")
        self.status_dropdown_box.addItem("")
        self.status_dropdown_box.addItem("")
        self.status_dropdown_box.activated.connect(self.on_combobox_changed)

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

        ###

        self.search_button = QtWidgets.QPushButton(mainPage, clicked=lambda:self.search_button_clicked())
        self.search_button.setGeometry(QtCore.QRect(300, 120, 91, 31))
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

        self.travel_id_label = QtWidgets.QLabel(mainPage)
        self.travel_id_label.setGeometry(QtCore.QRect(60, 100, 40, 25))
        self.travel_id_label.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255, 255, 255);")
        self.travel_id_label.setObjectName("travel_id_label")

        self.travel_id_label2 = QtWidgets.QLabel(mainPage)
        self.travel_id_label2.setGeometry(QtCore.QRect(30, 160, 101, 40))
        self.travel_id_label2.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                           "font: 10pt \"MS Shell Dlg 2\";\n"
                                           "color: rgb(255, 255, 255);")
        self.travel_id_label2.setObjectName("travel_id_label")

        self.search_trip_id_information = QtWidgets.QLineEdit(mainPage)
        self.search_trip_id_information.setGeometry(QtCore.QRect(30, 120, 91, 31))
        self.search_trip_id_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
        "color: rgb(56, 56, 56);\n"
        "background-color: rgb(242, 237, 215);\n"
        "\n"
        "\n"
        "\n"
        "")
        self.search_trip_id_information.setObjectName("search_trip_id_information")
        self.search_trip_id_information.setEnabled(True)

        # Update Button
        self.update_button = QtWidgets.QPushButton(mainPage, clicked=lambda:self.update_button_clicked())
        self.update_button.setGeometry(QtCore.QRect(160, 390, 100, 30))
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
        self.update_button.setObjectName("update_Btn")

        self.payment_information = QtWidgets.QLineEdit(mainPage)
        self.payment_information.setGeometry(QtCore.QRect(260, 330, 100, 20))
        self.payment_information.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";\n"
                                   "color: rgb(56, 56, 56);\n"
                                   "background-color: rgb(242, 237, 215);\n"
                                   "\n""\n""\n""")
        self.payment_information.setObjectName("pay_Txt")
        self.payment_information.setEnabled(False)

        self.update(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)

###
    def on_combobox_changed(self):
        content = self.status_dropdown_box.currentText()

        self.status_information.setText(content)

        # self.status_cBox.count()
    def update(self, mainPage):
        update_information = QtCore.QCoreApplication.translate

        mainPage.setWindowTitle(update_information("mainPage", "Driver Dashboard"))
        self.label_booking.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; font-size:20pt;\">Driver Trip Details</span></p></body></html>"))
        self.travel_id_label.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; font-size:11pt;\">T ID</span></p></body></html>"))
        self.travel_id_label2.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; font-size:11pt;\">Travel ID</span></p></body></html>"))
        self.search_button.setText(update_information("mainPage", "Search"))
        self.update_button.setText(update_information("mainPage", "Update"))
        self.back_button.setText(update_information("mainPage", "Go Back"))
        self.pickup_time_label.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">Pick up Time</span></p></body></html>"))
        self.pickup_address_label.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">Pick up Address</span></p></body></html>"))
        self.pickup_date_label.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">Pick up Date</span></p></body></html>"))
        self.label_of_address.setText(update_information("mainPage", "<html><head/><body><p><span style =\" font-weight:550; color:#ffffff;\">Drop-off Address</span></p></body></html>"))
        self.status_dropdown_box.setItemText(0, update_information("mainPage", "Status"))
        self.status_dropdown_box.setItemText(1, update_information("mainPage", "Active"))
        self.status_dropdown_box.setItemText(2, update_information("mainPage", "Completed"))
        self.status_dropdown_box.setItemText(3, update_information("mainPage", "Cancel"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QDialog()
    ui = driver_dashboard_Ui(mainPage)
    ui.showing()
    sys.exit(app.exec())







